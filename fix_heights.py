import re

with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

# Currently they have width="49%"
# Let's replace width="49%" with height="200" to ensure they are the exact same height!
# Actually, the LeetCode heatmap card is quite tall (500x399).
# Setting both to height="220" will make them identically tall and scale their widths proportionally.

content = re.sub(
    r'<img src="(https://codeforces-readme-stats[^"]+)" alt="Codeforces Stats" width="49%" />',
    r'<img src="\1" alt="Codeforces Stats" height="220" />',
    content
)

content = re.sub(
    r'<img src="(https://leetcard[^"]+)" alt="LeetCode Stats" width="49%" />',
    r'<img src="\1" alt="LeetCode Stats" height="220" />',
    content
)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)
