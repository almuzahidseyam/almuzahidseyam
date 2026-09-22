import io
with io.open('README.md', 'r', encoding='utf-8') as f:
    text = f.read()

injection = '''
<p align="center">
  <img src="https://skillicons.dev/icons?i=cpp,python,javascript,react,nodejs,flutter,dart,git,github,docker,linux&perline=12" />
</p>
'''

# Find the exact marker to insert before
marker = '---'
idx = text.find(marker)
if idx != -1:
    new_text = text[:idx] + injection + '\n' + text[idx:]
    with io.open('README.md', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print('Injected successfully before the first ---')
