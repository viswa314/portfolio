import re

file_path = r'c:\My Web Sites\Portfolio\qu.ai\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    orig_content = f.read()

content = orig_content

# 1. Clean up lingering "Quai" in IDs and class-like strings
content = content.replace('quai-logo', 'vg-logo')
content = content.replace('quai-text-logo', 'vg-text')
content = content.replace('wp-theme-quai', 'wp-theme-personal')
content = content.replace('vg-logo-placeholder', 'vg-logo')
content = content.replace('vg-text-placeholder', 'vg-text')

# 2. Aggressive string replacement for all visible and attribute text
content = content.replace('Quai Network', 'Viswa Gandamalla')
content = content.replace('Quai network', 'Personal portfolio')
content = content.replace('Quai', 'Viswa')

# 3. Logo Redesign (Header, Nav, Footer) 
# Goal: Match the futuristic, professional aesthetic.
# We will use Yapari for the initials and Monorama for the full name.

# Definition for the logo container contents
def get_personal_logo(include_name=True):
    name_html = f'<div class="header__logo__name d-none d-block@sm pl-20 js-header:logoText" style="font-family: \'Monorama-Regular\', sans-serif; font-size: clamp(14px, 1.5vw, 18px); color: white; letter-spacing: 0.3em; text-transform: uppercase; font-weight: 400; white-space: nowrap;">Viswa Gandamalla</div>' if include_name else ''
    return f"""
      <div class="header__logo__vg z-1 js-header:logo" style="font-family: 'Yapari-SemiBold', sans-serif; font-size: clamp(24px, 2.5vw, 32px); color: white; line-height: 0.8; font-weight: 600; text-transform: uppercase;">VG</div>
      <div class="js-header:logoMask">
        {name_html}
      </div>
"""

# Header Logo
content = re.sub(r'<a href="index.html" class="header__logo d-flex items-center \| js-home-btn">.*?</a>', 
                 f'<a href="index.html" class="header__logo d-flex items-center | js-home-btn">{get_personal_logo().strip()}</a>', 
                 content, flags=re.DOTALL)

# Nav Overlay Logo
content = re.sub(r'<a href="index.html" aria-label="Back to homepage" class="d-flex items-center logo opacity-0 absolute relative@smallDesk l-10 l-20@sm l-0@smallDesk">.*?</a>',
                 f'<a href="index.html" aria-label="Back to homepage" class="d-flex items-center logo opacity-0 absolute relative@smallDesk l-10 l-20@sm l-0@smallDesk">{get_personal_logo().strip()}</a>', 
                 content, flags=re.DOTALL)

# Footer Logo
content = re.sub(r'<a href="index.html" aria-label="Back to homepage" class="d-flex items-center logo absolute relative@smallDesk l-10 l-20@sm l-0@smallDesk center-x">.*?</a>',
                 f'<a href="index.html" aria-label="Back to homepage" class="d-flex items-center logo absolute relative@smallDesk l-10 l-20@sm l-0@smallDesk center-x">{get_personal_logo().strip()}</a>', 
                 content, flags=re.DOTALL)

# 4. Correcting any missed titles or labels
content = re.sub(r'aria-label=".*?Viswa.*?"', 'aria-label="Back to homepage"', content) # reset generic

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Final aggressive sweep and typographic polish complete.")
