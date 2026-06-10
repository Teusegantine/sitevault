import re
import os

# Files
index_html = '/Users/matheussegantine/Desktop/Site Jobler/index2.html'
design_system = '/Users/matheussegantine/Desktop/Site Jobler/assets/design_system.html'
out_html = '/Users/matheussegantine/Desktop/Site Jobler/index.html'
css_file = '/Users/matheussegantine/Desktop/Site Jobler/css/styles.css'
js_file = '/Users/matheussegantine/Desktop/Site Jobler/js/main.js'

with open(index_html, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Extract Styles
styles = []
def style_replacer(match):
    styles.append(match.group(1))
    return ''

content = re.sub(r'<style>(.*?)</style>', style_replacer, content, flags=re.DOTALL)

with open(css_file, 'w', encoding='utf-8') as f:
    f.write('\n\n'.join(styles))

# Add the link tag right before </head>
link_tag = '    <link rel="stylesheet" href="css/styles.css">\n</head>'
content = content.replace('</head>', link_tag)


# 2. Extract Scripts (only those with content, not external src unless it's a specific one we want to move)
scripts = []
def script_replacer(match):
    # match.group(0) is full tag, match.group(1) is attributes, match.group(2) is content
    attrs = match.group(1)
    script_content = match.group(2).strip()
    
    # We don't extract Tailwind config script or external scripts
    if 'tailwind.config' in script_content or 'src=' in attrs:
        return match.group(0)
    
    if script_content:
        scripts.append(script_content)
        return ''
    return match.group(0)

content = re.sub(r'<script([^>]*)>(.*?)</script>', script_replacer, content, flags=re.DOTALL)

with open(js_file, 'w', encoding='utf-8') as f:
    f.write('\n\n'.join(scripts))

# Add script src right before </body>
script_tag = '    <script src="js/main.js"></script>\n</body>'
content = content.replace('</body>', script_tag)


# 3. Path Replacements
path_replacements = {
    'Assets/Imagens/Logo': 'assets/images/logo',
    'Assets/Imagens/Personagens': 'assets/images/characters',
    'Assets/Imagens/Referências': 'assets/images/references',
    'Assets/Imagens/Referências': 'assets/images/references', # NFD encoding
    'Assets/Imagens/Sócios': 'assets/images/partners',
    'Assets/Imagens/Sócios': 'assets/images/partners', # NFD encoding
    'Assets/Vídeos': 'assets/videos',
    'Assets/Vídeos': 'assets/videos', # NFD encoding
    'Assets/Templates': 'assets/templates',
    'Assets/': 'assets/',
}

for old_path, new_path in path_replacements.items():
    content = content.replace(old_path, new_path)

with open(out_html, 'w', encoding='utf-8') as f:
    f.write(content)

# Update design system paths as well
if os.path.exists(design_system):
    with open(design_system, 'r', encoding='utf-8') as f:
        ds_content = f.read()
    
    for old_path, new_path in path_replacements.items():
        ds_content = ds_content.replace(old_path, new_path)
        
    with open(design_system, 'w', encoding='utf-8') as f:
        f.write(ds_content)

print("Extraction and path updates complete.")
