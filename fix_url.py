import urllib.parse
import re

lines = [
    "Hi there 👋, I am Muhammad Al-Muzahid",
    "Software Engineer | AI & ML Researcher",
    "Competitive Programmer (CodeChef 3★)",
    "Exploring Systems Design & Deep Learning"
]
encoded_lines = ";".join([urllib.parse.quote(line) for line in lines])
typing_url = f"https://readme-typing-svg.demolab.com/?lines={encoded_lines}&font=Fira%20Code&center=true&width=800&height=50&duration=4000&pause=1000&color=7C3AED"

with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

# Fix the broken URL in the file
content = re.sub(r"https://readme-typing-svg\.demolab\.com/\?lines=[^&]*", f"https://readme-typing-svg.demolab.com/?lines={encoded_lines}", content)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)
