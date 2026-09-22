import re

with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Remove the top social table
# The top social table is right before "--- \n\n## 👨‍💻 About Me"
# Let's find the first table and remove it.
content = re.sub(r"<table align=\"center\">\s*<tbody>.*?</tr>\s*</tbody>\s*</table>\s*\n*", "", content, count=1, flags=re.DOTALL)

# 2. Update the flower spinner source
content = content.replace("https://openclipart.org/download/231263/cherry-blossom-spinner.svg", "./assets/flower-spinner.svg")

# 3. Update the Matrix Coding banner height
content = content.replace('alt="Matrix Coding" width="100%"', 'alt="Matrix Coding" width="100%" height="150"')

with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)
