import re
import os

filepath = '/Users/matheussegantine/Desktop/Site Jobler/index2.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update HTML tag to include dark mode by default
if '<html lang="pt-BR">' in content:
    content = content.replace('<html lang="pt-BR">', '<html lang="pt-BR" class="dark scroll-smooth">')
if '<html>' in content:
    content = content.replace('<html>', '<html class="dark scroll-smooth">')

# 2. Update tailwind config to include darkMode: 'class'
# Find the tailwind config block
tw_config_search = "tailwind.config = {"
tw_config_replace = "tailwind.config = {\n            darkMode: 'class',"
if tw_config_search in content and "darkMode: 'class'" not in content:
    content = content.replace(tw_config_search, tw_config_replace)

# 3. Add the theme toggle script
theme_script = """
    <script>
        // Theme Toggle Logic
        function toggleTheme() {
            const html = document.documentElement;
            if (html.classList.contains('dark')) {
                html.classList.remove('dark');
                localStorage.setItem('theme', 'light');
            } else {
                html.classList.add('dark');
                localStorage.setItem('theme', 'dark');
            }
        }
        
        // Load theme on start
        if (localStorage.theme === 'light') {
            document.documentElement.classList.remove('dark');
        }
    </script>
"""
if 'toggleTheme()' not in content:
    content = content.replace('</body>', theme_script + '\n</body>')

# 4. Add the toggle button to the footer
# The footer links are inside: <div class="flex gap-4"> ... </div> right after copyright.
footer_target = """<div class="flex gap-4">
                            <a href="#" class="hover:text-neutral-400 transition-colors">Termos de Uso</a>
                            <a href="#" class="hover:text-neutral-400 transition-colors">Política de Privacidade</a>
                        </div>"""

footer_replacement = """<div class="flex gap-4 items-center">
                            <a href="#" class="hover:text-neutral-900 dark:hover:text-neutral-400 transition-colors">Termos de Uso</a>
                            <a href="#" class="hover:text-neutral-900 dark:hover:text-neutral-400 transition-colors">Política de Privacidade</a>
                            <div class="w-px h-4 bg-neutral-300 dark:bg-white/10 mx-2"></div>
                            <button onclick="toggleTheme()" class="text-neutral-500 hover:text-blue-600 dark:text-neutral-400 dark:hover:text-white transition-colors p-1 rounded-md hover:bg-neutral-100 dark:hover:bg-white/5 flex items-center justify-center">
                                <i data-lucide="sun" class="w-4 h-4 hidden dark:block"></i>
                                <i data-lucide="moon" class="w-4 h-4 block dark:hidden"></i>
                            </button>
                        </div>"""
if footer_target in content:
    content = content.replace(footer_target, footer_replacement)

# 5. Mass regex replacements for classes
replacements = {
    r'\btext-white\b': 'text-neutral-900 dark:text-white',
    r'\btext-neutral-400\b': 'text-neutral-600 dark:text-neutral-400',
    r'\btext-neutral-300\b': 'text-neutral-700 dark:text-neutral-300',
    r'\bbg-\[\#050505\]\b': 'bg-gray-50 dark:bg-[#050505]',
    r'\bbg-neutral-950\b': 'bg-gray-50 dark:bg-neutral-950',
    r'\bbg-\[\#0a0a0c\]\b': 'bg-white dark:bg-[#0a0a0c]',
    r'\border-white/5\b': 'border-neutral-200 dark:border-white/5',
    r'\border-white/10\b': 'border-neutral-200 dark:border-white/10',
    r'\border-white/20\b': 'border-neutral-300 dark:border-white/20',
    r'\border-white/\[0\.08\]\b': 'border-neutral-200 dark:border-white/[0.08]',
    r'\border-white\b': 'border-neutral-200 dark:border-white',
    r'\bbg-white/5\b': 'bg-neutral-100 dark:bg-white/5',
    r'\bbg-white/10\b': 'bg-neutral-200 dark:bg-white/10',
    r'\bbg-white/\[0\.03\]\b': 'bg-white dark:bg-white/[0.03]',
    r'\bbg-white/\[0\.02\]\b': 'bg-white dark:bg-white/[0.02]',
    r'\bhover:text-white\b': 'hover:text-blue-600 dark:hover:text-white',
    r'\bbg-neutral-950/50\b': 'bg-white/80 dark:bg-neutral-950/50',
    r'\bbg-neutral-900\b': 'bg-neutral-100 dark:bg-neutral-900',
    r'\bhover:bg-neutral-900\b': 'hover:bg-neutral-50 dark:hover:bg-neutral-900',
}

# We need to be careful not to replace classes that already have dark: prefix
# A safe way is to split by class="..." and replace inside
def replace_classes(match):
    cls_str = match.group(1)
    # Check if we should process this class string
    if 'dark:' in cls_str and 'dark:text-white' in cls_str:
        return f'class="{cls_str}"' # already processed
        
    for pattern, replacement in replacements.items():
        # Negative lookbehind for dark: to avoid double replacing
        regex = r'(?<!dark:)' + pattern
        cls_str = re.sub(regex, replacement, cls_str)
    
    return f'class="{cls_str}"'

content = re.sub(r'class="([^"]+)"', replace_classes, content)

# 6. Update Custom CSS for card-grid-bg
old_css = """
                    .card-grid-bg {
                        background-color: #0c0d12;
                        background-image: 
                            linear-gradient(rgba(255, 255, 255, 0.02) 1px, transparent 1px),
                            linear-gradient(90deg, rgba(255, 255, 255, 0.02) 1px, transparent 1px);
                        background-size: 24px 24px;
                    }
"""

new_css = """
                    .card-grid-bg {
                        background-color: #ffffff;
                        background-image: 
                            linear-gradient(rgba(0, 0, 0, 0.03) 1px, transparent 1px),
                            linear-gradient(90deg, rgba(0, 0, 0, 0.03) 1px, transparent 1px);
                        background-size: 24px 24px;
                    }
                    .dark .card-grid-bg {
                        background-color: #0c0d12;
                        background-image: 
                            linear-gradient(rgba(255, 255, 255, 0.02) 1px, transparent 1px),
                            linear-gradient(90deg, rgba(255, 255, 255, 0.02) 1px, transparent 1px);
                    }
"""
if old_css in content:
    content = content.replace(old_css, new_css)

# Also fix the model-card hover background which is currently:
# background: rgba(255,255,255,0.03); 
# and hover: background-color: rgba(30,58,138,0.2);
old_model_card = """
                    .model-card {
                        position: relative;
                        border-radius: 1.5rem;
                        background: rgba(255,255,255,0.03);
"""
new_model_card = """
                    .model-card {
                        position: relative;
                        border-radius: 1.5rem;
                        background: rgba(0,0,0,0.02);
                    }
                    .dark .model-card {
                        background: rgba(255,255,255,0.03);
"""
if old_model_card in content:
    content = content.replace(old_model_card, new_model_card)
    
old_model_card_hover = """
                    .model-card:hover {
                        transform: translateY(-8px);
                        border-color: #60a5fa;
                        box-shadow: 0 0 80px rgba(59,130,246,0.8);
                        background-color: rgba(30,58,138,0.2);
                    }
"""
new_model_card_hover = """
                    .model-card:hover {
                        transform: translateY(-8px);
                        border-color: #60a5fa;
                        box-shadow: 0 4px 20px rgba(59,130,246,0.15);
                        background-color: rgba(30,58,138,0.05);
                    }
                    .dark .model-card:hover {
                        box-shadow: 0 0 80px rgba(59,130,246,0.8);
                        background-color: rgba(30,58,138,0.2);
                    }
"""
if old_model_card_hover in content:
    content = content.replace(old_model_card_hover, new_model_card_hover)

# Save
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Light mode refactor script executed successfully.")
