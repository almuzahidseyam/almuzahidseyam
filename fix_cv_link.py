import re

with open("D:\\GitHub\\almuzahidseyam\\README.md", "r", encoding="utf-8") as f:
    content = f.read()

# Replace the private URL with the public URL
content = content.replace(
    "https://github.com/almuzahidseyam/almuzahidseyam-portfolio/blob/main/public/assets/cv/software-engineer-cv.pdf",
    "https://github.com/almuzahidseyam/almuzahidseyam/blob/main/assets/software-engineer-cv.pdf"
)

with open("D:\\GitHub\\almuzahidseyam\\README.md", "w", encoding="utf-8") as f:
    f.write(content)
