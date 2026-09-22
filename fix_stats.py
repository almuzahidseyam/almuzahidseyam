import re

with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

# Replace the entire GitHub Activity & Stats section
new_stats_section = """## 📈 GitHub Activity

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/almuzahidseyam/almuzahidseyam/output/github-contribution-grid-snake-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/almuzahidseyam/almuzahidseyam/output/github-contribution-grid-snake.svg">
    <img alt="almuzahidseyam's GitHub contribution grid snake animation" src="https://raw.githubusercontent.com/almuzahidseyam/almuzahidseyam/output/github-contribution-grid-snake.svg">
  </picture>
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/almuzahidseyam/almuzahidseyam/output/streak.svg" alt="GitHub Streak" />
</p>

<p align="center">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=almuzahidseyam&bg_color=00000000&color=a855f7&line=9333ea&point=c084fc&hide_border=true" alt="GitHub Activity Graph" />
</p>

---"""

# Find everything from "## 📈 GitHub Activity & Stats" to the "---" before "Connect With Me"
content = re.sub(r"## 📈 GitHub Activity & Stats.*?---", new_stats_section, content, flags=re.DOTALL)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)
