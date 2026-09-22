import re

with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

# Currently the Profile Details image has no width attribute.
# We will add width="100%" to make it align with the 49% + 49% row below it.
content = re.sub(
    r'(<img src="https://github-profile-summary-cards\.vercel\.app/api/cards/profile-details[^>]+)( alt="Profile Details" />)',
    r'\1\2',  # Wait, let me just replace the exact tag
    content
)

content = content.replace(
    'alt="Profile Details" />',
    'alt="Profile Details" width="100%" />'
)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)
