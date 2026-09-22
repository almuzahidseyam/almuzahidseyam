import re

with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

# Define the resume HTML
resume_html = """
<p align="center">
  <a href="https://github.com/almuzahidseyam/almuzahidseyam-portfolio/blob/main/public/assets/cv/software-engineer-cv.pdf" target="_blank">
    <img src="https://img.shields.io/badge/Download%20Software%20Engineer%20CV-PDF-7c3aed?style=for-the-badge&logo=adobeacrobatreader&logoColor=white" alt="Resume Download" />
  </a>
</p>
"""

# Insert right after the Typing SVG paragraph
content = re.sub(
    r'(<img src="https://readme-typing-svg[^>]+>\s*</a>\s*</p>)',
    r'\1\n' + resume_html,
    content
)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)
