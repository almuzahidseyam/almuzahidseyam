import io
import re

with io.open('README.md', 'r', encoding='utf-8') as f:
    text = f.read()

# We need to replace the entire <p align="center"> block containing Sponsor_Me
pattern = r'<p align="center">\s*<a href="https://www\.buymeacoffee\.com[^>]*>\s*<img src="[^"]*Sponsor_Me[^>]*>\s*</a>\s*<a href="[^"]*software-engineer-cv\.pdf[^>]*>\s*<img src="[^"]*Download[^>]*>\s*</a>\s*</p>'

clean_block = '''<p align="center">
  <a href="https://www.buymeacoffee.com/almuzahidseyam" target="_blank"><img src="https://img.shields.io/badge/Sponsor_Me-EA4AAA?style=for-the-badge&logo=githubsponsors&logoColor=white" alt="Sponsor" /></a>&nbsp;&nbsp;&nbsp;<a href="https://github.com/almuzahidseyam/almuzahidseyam/blob/main/assets/software-engineer-cv.pdf" target="_blank"><img src="https://img.shields.io/badge/Download%20Software%20Engineer%20CV-PDF-7c3aed?style=for-the-badge&logo=adobeacrobatreader&logoColor=white" alt="Resume Download" /></a>
</p>'''

new_text = re.sub(pattern, clean_block, text)

with io.open('README.md', 'w', encoding='utf-8') as f:
    f.write(new_text)
print("Regex replaced!")
