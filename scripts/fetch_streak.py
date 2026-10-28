"""Keep profile animation publishing even when the streak service is unavailable."""

import os
from pathlib import Path
import time
from urllib.error import URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from xml.etree import ElementTree


def fetch_svg(url):
    with urlopen(Request(url, headers={"User-Agent": "github-profile"}), timeout=20) as response:
        data = response.read(2_000_001)
    if len(data) > 2_000_000:
        raise ValueError("SVG exceeds size limit")
    if ElementTree.fromstring(data).tag != "{http://www.w3.org/2000/svg}svg":
        raise ValueError("Response is not an SVG")
    return data


def streak_svg(repository):
    query = urlencode({
        "user": repository.split("/")[0], "background": "00000000",
        "fire": "9333ea", "ring": "c084fc", "currStreakLabel": "a855f7",
        "sideNums": "a855f7", "currStreakNum": "9333ea", "dates": "c084fc",
        "hide_border": "true",
    })
    for attempt in range(3):
        try:
            return fetch_svg("https://streak-stats.demolab.com/?" + query)
        except (OSError, URLError, ValueError, ElementTree.ParseError):
            if attempt < 2:
                time.sleep(2 * (attempt + 1))
    print("::warning::Streak service unavailable; using the last published SVG.")
    try:
        return fetch_svg(f"https://raw.githubusercontent.com/{repository}/output/streak.svg")
    except (OSError, URLError, ValueError, ElementTree.ParseError):
        print("::warning::Cached streak SVG unavailable; publishing an unavailable message.")
        return (b'<svg xmlns="http://www.w3.org/2000/svg" width="495" height="80" '
                b'viewBox="0 0 495 80" role="img" aria-label="Streak stats temporarily unavailable">'
                b'<text x="247.5" y="44" text-anchor="middle" fill="#a855f7" '
                b'font-family="sans-serif" font-size="16">Streak stats temporarily unavailable</text></svg>')


if __name__ == "__main__":
    output = Path("dist/streak.svg")
    data = streak_svg(os.environ["PROFILE_REPOSITORY"])
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes(data)
