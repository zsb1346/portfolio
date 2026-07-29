import os
import re

base = r'F:\L练习\网站'
base_url = 'https://media-1460494365.cos.ap-guangzhou.myqcloud.com'
html_files = ['index.html', 'webtoolsai.html', 'shunqie.html', 'kuaijie-ai.html']
media_dirs = ['视觉作品/', '快捷AI/', '瞬贴展示/', 'webToolsAI/']

for html in html_files:
    path = os.path.join(base, html)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    modified = False
    for d in media_dirs:
        pattern = r'(src=["\'])(' + re.escape(d) + r')'
        replacement = r'\1' + base_url + r'/\2'
        new_content, n = re.subn(pattern, replacement, content)
        if n > 0:
            print(f'{html}: replaced {n} references to {d}')
            content = new_content
            modified = True
    if modified:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
print('Done')
