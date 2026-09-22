import re

with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

# Social icons table to replace the flat-square badges
social_table = """<table align="center">
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
</table>"""

# Replace the first social links block (between <p align="center"> and --- before About Me)
# Actually, I will just build the top section and replace everything up to "## 👨‍💻 About Me"
top_section = f"""<p align="center">
  <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMjdoZHA4czd1dWV0enh4dDE5MXdhZ3dvNmxieW05ZXdmODRsMWlqNiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/QpVUMRUJGokfqXyfa1/giphy.gif" alt="Matrix Coding" width="100%" />
</p>

<p align="center">
    <a href="https://github.com/almuzahidseyam/almuzahidseyam"><img src="https://img.shields.io/badge/status-updating-brightgreen.svg" alt="status"></a>
    <a href="https://github.com/almuzahidseyam?tab=followers"><img src="https://img.shields.io/github/followers/almuzahidseyam?color=blue&logo=github&style=flat" alt="followers"></a>
    <a href="https://github.com/almuzahidseyam?tab=repositories"><img src="https://img.shields.io/github/stars/almuzahidseyam?color=yellow&logo=github&style=flat" alt="stars"></a>
    <img src="https://komarev.com/ghpvc/?username=almuzahidseyam&label=Profile%20Views&color=7c3aed&style=flat" alt="Profile Views" />
</p>

<p align="center">
  <a href="https://git.io/typing-svg">
    <img src="https://readme-typing-svg.demolab.com/?lines=Hi+there+👋,+I+am+Muhammad+Al-Muzahid;Software+Engineer+%7C+AI+%26+ML+Researcher;Competitive+Programmer+(CodeChef+3★);Exploring+Systems+Design+%26+Deep+Learning&font=Fira%20Code&center=true&width=800&height=50&duration=4000&pause=1000&color=7C3AED" alt="Typing SVG" />
  </a>
</p>

{social_table}

---

## 👨‍💻 About Me
<p><img width="28%" align="right" alt="Cherry Blossom Spinner" src="https://openclipart.org/download/231263/cherry-blossom-spinner.svg"/></p>
"""

# Replace the top part
content = re.sub(r"^.*?## 👨‍💻 About Me\n", top_section, content, flags=re.DOTALL)

# Also replace the bottom "Connect With Me" social links
content = re.sub(r"## 📬 Connect With Me\n\n<p>.*?</p>", f"## 📬 Connect With Me\n\n{social_table}", content, flags=re.DOTALL)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)

print("Updated README.md")
