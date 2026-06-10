from bs4 import BeautifulSoup
import re

with open('/Users/matheussegantine/Desktop/Site Jobler/index2.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, 'html.parser')

# Find all partner cards
partner_cards = soup.find_all('div', class_=re.compile(r'partner-card'))

# Extract data from existing cards to build a dictionary by name
partners_dict = {}
for card in partner_cards:
    name_tag = card.find('h4', class_='text-white')
    if name_tag:
        name = name_tag.text.strip()
        partners_dict[name] = card

# Define the new order and the new roles
new_data = [
    {"name": "Matheus Segantine", "role": "Co-Founder"},
    {"name": "Eduardo Rached", "role": "Co-Founder"},
    {"name": "Guilherme Valle", "role": "Co-Founder"},
    {"name": "Bruno Marafon", "role": "Industrial & Manufacturing"}, # Assumed unchanged
    {"name": "Aline Nogueira", "role": "Technology & SaaS", "old_name": "Aline Marafon"}, # Name updated, role unchanged
    {"name": "Enzo Davila", "role": "Wellness & Fitness"}, # Assumed unchanged
    {"name": "Juliany Elisa", "role": "Banking & Financial Services"}, # Assumed unchanged
    {"name": "Carlos Silveira", "role": "Commodities, Trade & Logistics"}, # Assumed unchanged
    {"name": "Isabella Romanelli", "role": "Healthcare & Life Sciences"}, # Assumed unchanged
    {"name": "Letícia Silva", "role": "Construction & Energy"}, # Assumed unchanged
    {"name": "Leandro Feitosa", "role": "Ops Manager"}, # Role updated
    {"name": "Daniele Blanco", "role": "Sales B2B"}, # Role updated
    {"name": "Ednei Fibla", "role": "Team Ops"}, # Assumed unchanged
    {"name": "Laryssa Souza", "role": "Team Ops"}, # Assumed unchanged
    {"name": "Ana Laura Barros", "role": "Team Ops"}, # Assumed unchanged
    {"name": "Maria Eduarda de Queiroz", "role": "Team Ops"} # Assumed unchanged
]

# We need to recreate the grid. Let's find the grid container.
# It should be the parent of the partner cards.
grid_container = None
if partner_cards:
    grid_container = partner_cards[0].parent

if grid_container:
    # Clear the current contents of the grid container
    grid_container.clear()
    
    delays = ["", " delay-100", " delay-200", " delay-300", " delay-400", " delay-500"]
    
    for i, data in enumerate(new_data):
        # Find the original card using either new name or old name
        original_name = data.get("old_name", data["name"])
        # Wait, Letícia Silva in the dict might be "Letícia Silva" or "Letícia Silva" (normalization issues)
        # We will match by part of the name to be safe
        matching_card = None
        for key in partners_dict.keys():
            # Basic normalization for matching
            if original_name.split()[0].lower() in key.lower() and original_name.split()[-1].lower() in key.lower():
                matching_card = partners_dict[key]
                break
        
        if not matching_card:
            print(f"Warning: Could not find card for {original_name}")
            continue
            
        # Update name
        name_tag = matching_card.find('h4', class_='text-white')
        if name_tag:
            name_tag.string = data["name"]
            
        # Update role
        role_tag = matching_card.find('p', class_='text-neutral-400')
        if role_tag:
            role_tag.string = data["role"]
            
        # Update image alt text
        img_tag = matching_card.find('img', class_='partner-photo')
        if img_tag:
            img_tag['alt'] = data["name"]
            # Important: we don't change the src file name unless asked. 
            # Aline Marafon -> Aline Nogueira. The image file is likely still "Aline Marafon.png".
            # We keep the old src.
            
        # Update animation delay class based on column (6 columns lg)
        col_index = i % 6
        delay_class = delays[col_index]
        
        # Remove old delay classes
        classes = matching_card.get('class', [])
        new_classes = [c for c in classes if not c.startswith('delay-')]
        if delay_class:
            new_classes.append(delay_class.strip())
        matching_card['class'] = new_classes
        
        # Add a newline before the card
        grid_container.append("\n                        ")
        grid_container.append(matching_card)
        
    grid_container.append("\n                    ")

# Write back to file using minimal formatting changes
# BeautifulSoup can sometimes mess up formatting, so we'll just replace the grid HTML
# Wait, replacing the whole file with prettify might ruin GSAP scripts formatting.
# Better to convert grid_container to string and replace the original grid container string.

# We need the original HTML string of the grid container to replace it.
# We'll use regex to replace the content of the grid container.
import re
grid_pattern = r'(<div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-4">)(.*?)(</div>\s*</div>\s*</section>)'
# Since the grid is nested, regex with .*? might fail.
# Instead, we will write out the modified HTML entirely using soup.decode(formatter="html").
with open('/Users/matheussegantine/Desktop/Site Jobler/index2.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))
print("Successfully reordered partners and updated details.")
