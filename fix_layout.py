import re

with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

# Current setup:
# <p align="center">
#   <img src="...profile-details..." alt="Profile Details" />
#   <img src="...stats..." alt="Stats" />
# </p>
# <p align="center">
#   <img src="...productive-time..." alt="Productive Time" />
# </p>

new_layout = """<p align="center">
  <img src="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=almuzahidseyam&bg_color=ffffff&title_color=7c3aed&text_color=a855f7&icon_color=7c3aed&hide_border=true" alt="Profile Details" />
</p>
<p align="center">
  <img src="https://github-profile-summary-cards.vercel.app/api/cards/stats?username=almuzahidseyam&bg_color=ffffff&title_color=7c3aed&text_color=a855f7&icon_color=7c3aed&hide_border=true" alt="Stats" width="49%" />
  <img src="https://github-profile-summary-cards.vercel.app/api/cards/productive-time?username=almuzahidseyam&bg_color=ffffff&title_color=7c3aed&text_color=a855f7&icon_color=7c3aed&utcOffset=6&hide_border=true" alt="Productive Time" width="49%" />
</p>"""

# Using regex to replace the old layout with the new layout
content = re.sub(
    r'<p align="center">\s*<img src="https://github-profile-summary-cards\.vercel\.app/api/cards/profile-details[^>]+>\s*<img src="https://github-profile-summary-cards\.vercel\.app/api/cards/stats[^>]+>\s*</p>\s*<p align="center">\s*<img src="https://github-profile-summary-cards\.vercel\.app/api/cards/productive-time[^>]+>\s*</p>',
    new_layout,
    content,
    flags=re.DOTALL
)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)
