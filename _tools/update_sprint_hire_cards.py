import re

with open('/Users/matheussegantine/Desktop/Site Jobler/index2.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add style block right after <section id="engine" ...>
style_block = '''
                <style>
                    .card-grid-bg {
                        background-color: #0c0d12;
                        background-image: 
                            linear-gradient(rgba(255, 255, 255, 0.02) 1px, transparent 1px),
                            linear-gradient(90deg, rgba(255, 255, 255, 0.02) 1px, transparent 1px);
                        background-size: 24px 24px;
                    }
                    .group\/card:hover .card-grid-bg {
                        background-color: #0e0f15;
                    }
                </style>'''

section_engine = '<section id="engine" class="py-32 px-6 bg-[#050505] relative overflow-hidden">'
if section_engine in content and 'card-grid-bg' not in content:
    content = content.replace(section_engine, section_engine + style_block)

# Replace 'bg-neutral-950/50 hover:bg-neutral-900' with 'card-grid-bg' on the Sprint Hire cards
# Notice the original string: 'bg-neutral-950/50 hover:bg-neutral-900 transition-all'
content = content.replace('bg-neutral-950/50 hover:bg-neutral-900 transition-all', 'card-grid-bg transition-all')

with open('/Users/matheussegantine/Desktop/Site Jobler/index2.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Added card-grid-bg and replaced background classes successfully.")
