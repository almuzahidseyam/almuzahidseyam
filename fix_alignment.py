import re

with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Fix LeetCode Theme and CF/LeetCode Alignment
# Current CP section has no width attributes on CF and Leetcode.
# We add width="49%" to both and change LeetCode theme to light so it matches the white background.
content = re.sub(
    r'<img src="(https://codeforces-readme-stats[^"]+)" alt="Codeforces Stats" />',
    r'<img src="\1" alt="Codeforces Stats" width="49%" />',
    content
)

content = re.sub(
    r'<img src="(https://leetcard[^"]+theme=)transparent([^"]+)" alt="LeetCode Stats" />',
    r'<img src="\1light\2" alt="LeetCode Stats" width="49%" />',
    content
)

# 2. Fix Activity Cards Alignment and Font scaling
# Remove the percentage widths from the summary cards so their native SVG viewBox is respected.
# This prevents fonts from getting squished or stretched.
content = re.sub(
    r'<img src="(https://github-profile-summary-cards\.vercel\.app/api/cards/[^"]+)" alt="([^"]+)" width="[^"]+" />',
    r'<img src="\1" alt="\2" />',
    content
)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)
