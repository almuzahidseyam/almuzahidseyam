import re

with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

# Define the new cards with custom colors
profile_details = "https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=almuzahidseyam&bg_color=ffffff&title_color=7c3aed&text_color=a855f7&icon_color=7c3aed&hide_border=true"
stats_card = "https://github-profile-summary-cards.vercel.app/api/cards/stats?username=almuzahidseyam&bg_color=ffffff&title_color=7c3aed&text_color=a855f7&icon_color=7c3aed&hide_border=true"
productive_time = "https://github-profile-summary-cards.vercel.app/api/cards/productive-time?username=almuzahidseyam&bg_color=ffffff&title_color=7c3aed&text_color=a855f7&icon_color=7c3aed&utcOffset=6&hide_border=true"

new_cards_html = f"""<p align="center">
  <img src="{profile_details}" alt="Profile Details" width="48%" />
  <img src="{stats_card}" alt="Stats" width="48%" />
</p>
<p align="center">
  <img src="{productive_time}" alt="Productive Time" width="97%" />
</p>"""

# Replace the old activity graph with these new cards
# Wait, let's keep the activity graph if possible, or just replace it since these are better.
# The user asked to "update these in my readme nicely". Let's insert them right after the streak.svg.

def replace_stats(match):
    original_text = match.group(0)
    # Append the new cards HTML before the closing --- of the activity section
    return original_text + "\n\n" + new_cards_html + "\n\n"

# Find the end of the GitHub Activity section
content = re.sub(r'(<img src="https://raw.githubusercontent.com/almuzahidseyam/almuzahidseyam/output/streak.svg" alt="GitHub Streak" />\s*</p>)', r'\1' + "\n\n" + new_cards_html, content)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)
