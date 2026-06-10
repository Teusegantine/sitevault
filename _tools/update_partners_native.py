import re

with open('/Users/matheussegantine/Desktop/Site Jobler/index2.html', 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = '<div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 xl:grid-cols-6 gap-3 md:gap-4 mt-8">'
start_idx = content.find(start_marker)
if start_idx == -1:
    print("Could not find the start of the grid.")
    exit(1)

grid_content_start = start_idx + len(start_marker)
end_marker = '</div>\n                </div>\n            </div>\n        </section>'
end_idx = content.find(end_marker, grid_content_start)

if end_idx == -1:
    print("Could not find end of grid")
    exit(1)

grid_html = content[grid_content_start:end_idx]

parts = grid_html.split('<div class="partner-card')
cards = []

for p in parts[1:]:
    card_html = '<div class="partner-card' + p
    
    # Extract name. Note: it's inside <h4 class="text-xs font-semibold text-white tracking-tight">...</h4>
    name_match = re.search(r'<h4 class="text-xs font-semibold text-white tracking-tight">([^<]+)</h4>', card_html)
    if name_match:
        name = name_match.group(1).strip()
        cards.append({'name': name, 'html': card_html})
    else:
        print("Warning: Could not extract name from a card.")
        print("Card preview:", card_html[:100])

new_data = [
    {"name": "Matheus Segantine", "role": "Co-Founder"},
    {"name": "Eduardo Rached", "role": "Co-Founder"},
    {"name": "Guilherme Valle", "role": "Co-Founder"},
    {"name": "Bruno Marafon", "role": "Industrial & Manufacturing"}, 
    {"name": "Aline Nogueira", "role": "Technology & SaaS", "old_name": "Aline Marafon"}, 
    {"name": "Enzo Davila", "role": "Wellness & Fitness"}, 
    {"name": "Juliany Elisa", "role": "Banking & Financial Services"}, 
    {"name": "Carlos Silveira", "role": "Commodities, Trade & Logistics"}, 
    {"name": "Isabella Romanelli", "role": "Healthcare & Life Sciences"}, 
    {"name": "Letícia Silva", "role": "Construction & Energy", "alt_names": ["Letícia Silva", "Letícia Silva"]}, 
    {"name": "Leandro Feitosa", "role": "Ops Manager"}, 
    {"name": "Daniele Blanco", "role": "Sales B2B"}, 
    {"name": "Ednei Fibla", "role": "Team Ops"}, 
    {"name": "Laryssa Souza", "role": "Team Ops"}, 
    {"name": "Ana Laura Barros", "role": "Team Ops"}, 
    {"name": "Maria Eduarda de Queiroz", "role": "Team Ops"}
]

new_grid_html = ""
delays = ["", " delay-100", " delay-200", " delay-300", " delay-400", " delay-500"]

for i, data in enumerate(new_data):
    target_name = data.get("old_name", data["name"])
    alt_names = data.get("alt_names", [])
    
    matched_card = None
    for c in cards:
        if target_name.lower() in c['name'].lower() or any(alt.lower() in c['name'].lower() for alt in alt_names):
            matched_card = c
            break
            
    if not matched_card:
        print(f"Error: Could not find card for {target_name}")
        continue
        
    html = matched_card['html']
    
    # Replace name
    html = re.sub(r'<h4 class="text-xs font-semibold text-white tracking-tight">[^<]+</h4>', f'<h4 class="text-xs font-semibold text-white tracking-tight">{data["name"]}</h4>', html)
    
    # Replace role
    html = re.sub(r'<p class="text-\[10px\] text-neutral-500 mt-0\.5">[^<]+</p>', f'<p class="text-[10px] text-neutral-500 mt-0.5">{data["role"]}</p>', html)
    
    # Replace img alt tag
    html = re.sub(r'alt="[^"]+"', f'alt="{data["name"]}"', html)
    
    # Fix the delay classes for animation
    col_idx = i % 6
    delay_class = delays[col_idx]
    
    html = re.sub(r' delay-\d+', '', html, count=1)
    html = re.sub(r'st-fade-up', f'st-fade-up{delay_class}', html, count=1)
    
    # Add comment header for clarity (optional, but nice)
    new_grid_html += f'\n                        <!-- {i+1}. {data["name"]} -->\n                        ' + html

final_content = content[:grid_content_start] + new_grid_html + '\n                    ' + content[end_idx:]

with open('/Users/matheussegantine/Desktop/Site Jobler/index2.html', 'w', encoding='utf-8') as f:
    f.write(final_content)

print("Updated grid successfully!")
