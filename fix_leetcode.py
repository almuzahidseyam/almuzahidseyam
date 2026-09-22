import re

with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

# Replace the ext=activity with ext=heatmap on leetcard
content = content.replace("ext=activity", "ext=heatmap")

with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)
