import re

with open('/Users/matheussegantine/Desktop/Site Jobler/index2.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Revert internal cards
content = content.replace('card-grid-bg transition-all', 'bg-neutral-950/50 hover:bg-neutral-900 transition-all')

# 2. Update CSS for the grid bg (remove the group hover that was meant for inner cards)
# It looks like this:
#                     .group\/card:hover .card-grid-bg {
#                         background-color: #0e0f15;
#                     }
old_hover_css = '''                    .group\/card:hover .card-grid-bg {
                        background-color: #0e0f15;
                    }'''
content = content.replace(old_hover_css, '')

# 3. Apply the class to the outer wrapper card
# The wrapper string is:
# <div class="rounded-3xl border border-white/[0.08] p-6 sm:p-8 relative backdrop-blur-xl bg-white/[0.03] shadow-[0_8px_32px_rgba(0,0,0,0.4),inset_0_1px_0_rgba(255,255,255,0.06)]">
wrapper_target = '<div class="rounded-3xl border border-white/[0.08] p-6 sm:p-8 relative backdrop-blur-xl bg-white/[0.03]'
wrapper_replacement = '<div class="rounded-3xl border border-white/[0.08] p-6 sm:p-8 relative backdrop-blur-xl card-grid-bg'
content = content.replace(wrapper_target, wrapper_replacement)

# Also apply it to the "Modelos" outer wrapper if the user wants it for "cards principais"?
# "fundo dos cards principais" - wait, he said "dos cards principais" (plural).
# But Sprint Hire is one big card. "O efeito ... foi feito nos 3 cards menores e não no card maior e principal do Sprint hire"
# So he definitely means the wrapper of Sprint Hire.
# Does he also mean the wrappers of the "Modelos" cards? Modelos are 3 separate cards.
# Wait, "dos cards principais" might refer to the 3 main Modelos cards as well?
# The user's first prompt was: "Dê uma melhorada nos tons de fundo dos cards principais para que eles se destaquem um pouco mais"
# And then: "O efeito e tom mais claro foi feito nos 3 cards menores e não no card maior e principal do Sprint hire."
# This implies he considers the outer wrapper of Sprint Hire as the "card maior e principal".
# Let's just fix the Sprint Hire one for now, as that's explicitly mentioned as wrong.
# Actually, I should probably apply the `card-grid-bg` to Modelos as well? "Setores e Os Modelos" were the previous request.
# Let's just stick to what he explicitly pointed out: Sprint Hire's main wrapper.

with open('/Users/matheussegantine/Desktop/Site Jobler/index2.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed Sprint Hire outer wrapper successfully.")
