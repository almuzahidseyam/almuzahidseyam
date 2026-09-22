import re

with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

# The activity graph is inside a <p align="center"> block, right before the summary cards we added recently.
# Let's remove the block containing github-readme-activity-graph
content = re.sub(
    r'<p align="center">\s*<a href="https://github.com/ashutosh00710/github-readme-activity-graph">\s*<img src="https://github-readme-activity-graph\.vercel\.app/graph\?username=almuzahidseyam[^>]+>\s*</a>\s*</p>',
    '',
    content,
    flags=re.DOTALL
)

# Just in case it's not wrapped in an <a> tag anymore (as it might just be the img)
content = re.sub(
    r'<p align="center">\s*<img src="https://github-readme-activity-graph\.vercel\.app/graph\?username=almuzahidseyam[^>]+>\s*</p>',
    '',
    content,
    flags=re.DOTALL
)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(content.strip() + "\n")
