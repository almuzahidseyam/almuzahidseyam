import re

with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

projects_section = """<details open>
<summary><h2>🚀 Featured Software Engineering Projects</h2></summary>
<br>

<table>
  <tr>
    <td width="50%" valign="top">
      <a href="https://github.com/almuzahidseyam/TurboCache-Cpp">
        <img src="https://img.shields.io/badge/⚡_TurboCache--Cpp-7c3aed?style=for-the-badge&logo=github&logoColor=white" alt="TurboCache-Cpp" />
      </a>
      <br><br>
      A high-performance, multi-threaded in-memory caching system (a Mini Redis) built entirely from scratch. Custom TCP server handling concurrent connections efficiently.
      <br><br>
      <img src="https://img.shields.io/badge/C++17-ffffff?style=flat-square&logo=c%2B%2B&logoColor=7c3aed" /> 
      <img src="https://img.shields.io/badge/Winsock2-ffffff?style=flat-square&logo=windows&logoColor=7c3aed" />
    </td>
    <td width="50%" valign="top">
      <a href="https://github.com/almuzahidseyam/multi-agent-dev-team">
        <img src="https://img.shields.io/badge/🤖_Multi--Agent_Dev_Team-7c3aed?style=for-the-badge&logo=github&logoColor=white" alt="Multi-Agent Dev Team" />
      </a>
      <br><br>
      An autonomous TypeScript CLI platform where three AI agents (Planner, Coder, Reviewer) collaboratively build software projects in the terminal natively.
      <br><br>
      <img src="https://img.shields.io/badge/TypeScript-ffffff?style=flat-square&logo=typescript&logoColor=7c3aed" /> 
      <img src="https://img.shields.io/badge/Gemini_API-ffffff?style=flat-square&logo=google&logoColor=7c3aed" />
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <a href="https://github.com/almuzahidseyam/profemail-saas">
        <img src="https://img.shields.io/badge/📧_ProfEmail_SaaS-7c3aed?style=for-the-badge&logo=github&logoColor=white" alt="ProfEmail SaaS" />
      </a>
      <br><br>
      A modern SaaS web platform designed to help researchers parse their CVs and automatically generate highly tailored cold emails for university professors.
      <br><br>
      <img src="https://img.shields.io/badge/Next.js-ffffff?style=flat-square&logo=next.js&logoColor=7c3aed" /> 
      <img src="https://img.shields.io/badge/Tailwind-ffffff?style=flat-square&logo=tailwindcss&logoColor=7c3aed" />
    </td>
    <td width="50%" valign="top">
      <a href="https://github.com/almuzahidseyam/cf-ai-analyzer">
        <img src="https://img.shields.io/badge/📊_CF_AI_Analyzer-7c3aed?style=for-the-badge&logo=github&logoColor=white" alt="CF AI Analyzer" />
      </a>
      <br><br>
      An AI-powered Codeforces assistant that intelligently analyzes a user's failed submissions to recommend targeted algorithmic practice and roadmaps.
      <br><br>
      <img src="https://img.shields.io/badge/React-ffffff?style=flat-square&logo=react&logoColor=7c3aed" /> 
      <img src="https://img.shields.io/badge/Codeforces_API-ffffff?style=flat-square&logo=codeforces&logoColor=7c3aed" />
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <a href="https://github.com/almuzahidseyam/Brainsoft-OJ">
        <img src="https://img.shields.io/badge/💻_Brainsoft--OJ-7c3aed?style=for-the-badge&logo=github&logoColor=white" alt="Brainsoft-OJ" />
      </a>
      <br><br>
      A remarkable, local-first Online Judge platform for competitive programming and algorithm practice featuring real-time sandboxed code execution.
      <br><br>
      <img src="https://img.shields.io/badge/SQLite-ffffff?style=flat-square&logo=sqlite&logoColor=7c3aed" /> 
      <img src="https://img.shields.io/badge/Java_21-ffffff?style=flat-square&logo=java&logoColor=7c3aed" />
      <img src="https://img.shields.io/badge/Python-ffffff?style=flat-square&logo=python&logoColor=7c3aed" />
    </td>
    <td width="50%" valign="top">
      <a href="https://github.com/almuzahidseyam?tab=repositories&sort=stargazers">
        <img src="https://img.shields.io/badge/📂_View_All_Projects-ffffff?style=for-the-badge&logo=github&logoColor=7c3aed" alt="View All Projects" />
      </a>
      <br><br>
      <i>Explore my other repositories, competitive programming solutions, algorithm implementations, and open-source contributions on GitHub.</i>
    </td>
  </tr>
</table>

</details>"""

# Replace the current projects section
# From "## 🚀 Featured Software Engineering Projects" to "--- \n\n## 🏆 Competitive Programming"
content = re.sub(r"## 🚀 Featured Software Engineering Projects.*?---", projects_section + "\n\n---", content, flags=re.DOTALL)

# Let's also wrap Research in details like DenverCoder1
research_section = """<details open>
<summary><h2>🔬 Research & Thesis</h2></summary>
<br>

> ### 📄 DASS: Density-Adaptive Synthetic Sampling for Improved Imbalanced Classification
> *Published in IEEE Xplore at the 6th International Conference on Sustainable Technologies for Industry 5.0.*
> - **DOI:** [10.1109/STI64222.2024.10951098](https://doi.org/10.1109/STI64222.2024.10951098)
> - **Domain:** Machine Learning, Computer Vision, Synthetic Sampling.

> ### 🎓 M.Sc. Thesis
> *Attention-Driven Hierarchical Active Learning Framework for Robust Imbalanced Classification.*
> - **Domain:** Deep Learning, Active Learning, Attention Mechanisms.

</details>"""

content = re.sub(r"## 🔬 Research & Thesis.*?---", research_section + "\n\n---", content, flags=re.DOTALL)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)
