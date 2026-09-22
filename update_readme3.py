import re

with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

social_table = """## 📬 Connect With Me

<table align="center">
  <tbody>
    <tr>
      <td style="text-align: center;">
        <a href="https://github.com/almuzahidseyam" title="GitHub" target="_blank">
          <img src="https://img.icons8.com/fluency/48/000000/github.png" alt="GitHub" title="GitHub">
        </a>
      </td>
      <td style="text-align: center;">
        <a href="https://www.linkedin.com/in/almuzahid/" title="LinkedIn" target="_blank">
          <img src="https://img.icons8.com/fluency/48/000000/linkedin.png" alt="LinkedIn" title="LinkedIn">
        </a>
      </td>
      <td style="text-align: center;">
        <a href="mailto:almuzahid16@gmail.com" title="Email" target="_blank">
          <img src="https://img.icons8.com/fluency/48/000000/mail.png" alt="Email" title="Email">
        </a>
      </td>
      <td style="text-align: center;">
        <a href="https://www.facebook.com/muhammadalmuzahid/" title="Facebook" target="_blank">
          <img src="https://img.icons8.com/fluency/48/000000/facebook-new.png" alt="Facebook" title="Facebook">
        </a>
      </td>
      <td style="text-align: center;">
        <a href="https://codeforces.com/profile/brainsoft" title="Codeforces" target="_blank">
          <img src="https://img.icons8.com/external-tal-revivo-color-tal-revivo/48/000000/external-codeforces-programming-competitions-and-contests-programming-community-logo-color-tal-revivo.png" alt="Codeforces" title="Codeforces">
        </a>
      </td>
    </tr>
  </tbody>
</table>

"""

content = content.replace("---", "---" + "\n\n" + social_table, 1)  # Only inject once at the top if needed? No, wait. I want to inject it before the final line.

# Let's just find the last "---" and replace it
parts = content.rsplit("---", 1)
new_content = parts[0] + "---\n\n" + social_table + parts[1]

with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_content)
