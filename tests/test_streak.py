import importlib.util
import io
from pathlib import Path
import unittest
from unittest.mock import patch
from xml.etree import ElementTree

spec = importlib.util.spec_from_file_location("streak", Path(__file__).parents[1] / "scripts/fetch_streak.py")
streak = importlib.util.module_from_spec(spec)
spec.loader.exec_module(streak)
SVG = b'<svg xmlns="http://www.w3.org/2000/svg"><text>stats</text></svg>'


class StreakTests(unittest.TestCase):
    def test_timeout_uses_previous_svg(self):
        with patch.object(streak, "fetch_svg", side_effect=[TimeoutError()] * 3 + [SVG]) as fetch, patch.object(streak.time, "sleep"):
            self.assertEqual(streak.streak_svg("owner/profile"), SVG)
        self.assertEqual(fetch.call_args.args[0], "https://raw.githubusercontent.com/owner/profile/output/streak.svg")

    def test_all_sources_down_produces_valid_unavailable_svg(self):
        with patch.object(streak, "fetch_svg", side_effect=TimeoutError()), patch.object(streak.time, "sleep"):
            result = streak.streak_svg("owner/profile")
        self.assertEqual(ElementTree.fromstring(result).tag, "{http://www.w3.org/2000/svg}svg")
        self.assertIn(b"temporarily unavailable", result)

    def test_rejects_html_error_page(self):
        with patch.object(streak, "urlopen", return_value=io.BytesIO(b"<html>error</html>")), self.assertRaises(ValueError):
            streak.fetch_svg("https://example.test")

    def test_success_does_not_use_cache(self):
        with patch.object(streak, "fetch_svg", return_value=SVG) as fetch:
            self.assertEqual(streak.streak_svg("owner/profile"), SVG)
        self.assertEqual(fetch.call_count, 1)


if __name__ == "__main__":
    unittest.main()
