import sys
import re

partners = [
    {'name': 'Matheus Segantine', 'file': 'Matheus Segantine.png', 'sub': 'Media, Gaming & Creator Economy', 'linkedin': 'https://www.linkedin.com/in/sega/'},
    {'name': 'Eduardo Rached', 'file': 'Eduardo Rached.png', 'sub': 'Startups & Early Stages', 'linkedin': 'https://www.linkedin.com/in/rached-eduardo/'},
    {'name': 'Guilherme Valle', 'file': 'Guilherme Valle.png', 'sub': 'Consumer Markets & Franchising', 'linkedin': 'https://www.linkedin.com/in/gui-valle/'},
    {'name': 'Bruno Marafon', 'file': 'Bruno Marafon.png', 'sub': 'Industrial & Manufacturing', 'linkedin': 'https://www.linkedin.com/in/bruno-marafon/'},
    {'name': 'Aline Marafon', 'file': 'Aline Marafon.png', 'sub': 'Technology & SaaS', 'linkedin': 'https://www.linkedin.com/in/aline-nogueira-a78161103/'},
    {'name': 'Enzo Davila', 'file': 'Enzo Davila.png', 'sub': 'Wellness & Fitness', 'linkedin': 'https://www.linkedin.com/in/enzo-davila-983808181/'},
    {'name': 'Juliany Elisa', 'file': 'Juliany Elisa.png', 'sub': 'Banking & Financial Services', 'linkedin': 'https://www.linkedin.com/in/julianyelisa/'},
    {'name': 'Leandro Feitosa', 'file': 'Leandro Feitosa.png', 'sub': 'Startups & Early Stages', 'linkedin': 'https://www.linkedin.com/in/leandro-marques-feitosa-a0a63723/'},
    {'name': 'Carlos Silveira', 'file': 'Carlos Silveira.png', 'sub': 'Commodities, Trade & Logistics', 'linkedin': 'https://www.linkedin.com/in/carlos-silveira-b6975416/'},
    {'name': 'Isabella Romanelli', 'file': 'Isabella Romanelli.png', 'sub': 'Healthcare & Life Sciences', 'linkedin': 'https://www.linkedin.com/in/isabella-romanelli-60019567/'},
    {'name': 'Letícia Silva', 'file': 'Letícia Silva.png', 'sub': 'Construction & Energy', 'linkedin': 'https://www.linkedin.com/in/leeticiasilva89/'},
    {'name': 'Ednei Fibla', 'file': 'Ednei Fibla.png', 'sub': 'Team Ops', 'linkedin': 'https://www.linkedin.com/in/edneifibla/'},
    {'name': 'Laryssa Souza', 'file': 'Laryssa Souza.png', 'sub': 'Team Ops', 'linkedin': 'https://www.linkedin.com/in/lasoouza/'},
    {'name': 'Daniele Blanco', 'file': 'Daniele Blanco.png', 'sub': 'Team Ops', 'linkedin': 'https://www.linkedin.com/in/daniele-blanco/'},
    {'name': 'Maria Eduarda de Queiroz', 'file': 'Maria Eduarda de Queiroz.png', 'sub': 'Team Ops', 'linkedin': 'https://www.linkedin.com/in/dudamachadoqueiroz/'},
    {'name': 'Ana Laura Barros', 'file': 'Ana Laura Barros.png', 'sub': 'Team Ops', 'linkedin': 'https://www.linkedin.com/in/ana-laura-parada-barros-224205198/'}
]

html_parts = []
html_parts.append('                    <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 xl:grid-cols-6 gap-3 md:gap-4 mt-8">')

for i, p in enumerate(partners):
    delay = ''
    if i > 0:
        if i % 6 != 0:
            delay = f' delay-{(i % 6) * 100}'
            
    card = f'''
                        <!-- {i+1}. {p['name']} -->
                        <div class="partner-card st-fade-up{delay}">
                            <div class="partner-photo-wrap">
                                <img src="Assets/Imagens/Sócios/{p['file']}" alt="{p['name']}" class="partner-photo" loading="lazy">
                                <div class="partner-overlay flex items-end">
                                    <a href="{p['linkedin']}" target="_blank" class="partner-badge inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-blue-600 hover:bg-blue-500 border border-blue-500/50 text-[10px] font-semibold text-white uppercase tracking-wider transition-colors shadow-[0_0_15px_rgba(37,99,235,0.4)] cursor-pointer">
                                        <i data-lucide="linkedin" class="w-3.5 h-3.5 text-white"></i> LinkedIn
                                    </a>
                                </div>
                            </div>
                            <div class="px-3 py-2.5">
                                <h4 class="text-xs font-semibold text-white tracking-tight">{p['name']}</h4>
                                <p class="text-[10px] text-neutral-500 mt-0.5">{p['sub']}</p>
                            </div>
                        </div>'''
    html_parts.append(card)

html_parts.append('                    </div>\n                </div>\n            </div>')
new_grid_html = '\n'.join(html_parts)

with open('index2.html', 'r') as f:
    content = f.read()

start_pattern = '<div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 xl:grid-cols-6 gap-3 md:gap-4 mt-8">'
end_pattern = '<!-- END PARTNERS -->'

start_idx = content.find(start_pattern)
if start_idx == -1:
    print("Start pattern not found!")
    sys.exit(1)

# The end pattern doesn't exist, we need to find the ending tags of the section.
# Let's find </section> after the start_idx
end_section_idx = content.find('</section>', start_idx)

# Then we find the last 3 closing divs before </section>
# Actually, the easiest is to just find 'Letícia Silva' and find the closing divs after it.
leticia_idx = content.find('Letícia Silva', start_idx)
after_leticia = content[leticia_idx:end_section_idx]
# find the last </div> before the end of the section?
# Instead of guessing, I'll just use regex to replace everything between the grid start and the 3 closing divs.
pattern = r'<div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 xl:grid-cols-6 gap-3 md:gap-4 mt-8">.*?(?=</section>)'
match = re.search(pattern, content, re.DOTALL)
if match:
    # we need to keep the closing tags if they belong to the section or container.
    # The new_grid_html has 3 closing divs at the end.
    # So we replace the match with new_grid_html.
    new_content = content[:match.start()] + new_grid_html + '\n        ' + content[match.end():]
    with open('index2.html', 'w') as f:
        f.write(new_content)
    print("Successfully replaced partners section!")
else:
    print("Pattern not found!")
