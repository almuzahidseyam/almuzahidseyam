import re

with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

# Let's completely revamp the "## 🏆 Competitive Programming" section
new_cp_section = """## 🏆 Competitive Programming

<p align="center">
  <img src="https://codeforces-readme-stats.vercel.app/api/card?username=brainsoft&bg_color=00000000&title_color=7c3aed&text_color=a855f7&icon_color=c084fc&hide_border=true" alt="Codeforces Stats" />
  <img src="https://leetcard.jacoblin.cool/brainsoft?theme=transparent&font=Fira%20Code&ext=activity" alt="LeetCode Stats" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/CodeChef-3_Star_(1745)-7c3aed?style=for-the-badge&logo=codechef&logoColor=white" alt="CodeChef Stats" />
  <img src="https://img.shields.io/badge/AtCoder-Rating_456-7c3aed?style=for-the-badge&logo=atcoder&logoColor=white" alt="AtCoder Stats" />
  <img src="https://img.shields.io/badge/BeeCrowd-Top_1%25_Global-7c3aed?style=for-the-badge&logo=codeforces&logoColor=white" alt="BeeCrowd Stats" />
</p>

**Achievements:**
- ICPC Asia Dhaka Regionalist (2023, 2024, 2025)
- NCPC Finalist (2023)
- 3rd place, PSTU Independence Day Programming Contest (2024)
- National Undergraduate Mathematics Olympiad Awardee"""

content = re.sub(r"## 🏆 Competitive Programming.*?---", new_cp_section + "\n\n---", content, flags=re.DOTALL)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)
