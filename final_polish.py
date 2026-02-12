import re

file_path = r'c:\My Web Sites\Portfolio\qu.ai\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Final comprehensive string cleanup (aggressive)
# Some might have escaped due to case or slightly different attribute names
content = content.replace('quai-logo', 'vg-logo-placeholder')
content = content.replace('quai-text-logo', 'vg-text-placeholder')
content = content.replace('aria-label="Quai Network"', 'aria-label="Viswa Gandamalla"')
content = content.replace('title="Quai Network"', 'title="Viswa Gandamalla"')

# 2. Redesign Logos (Header, Nav, Footer) to match site aesthetic
# The site uses Yapari-SemiBold and Monorama-Regular.
# Let's use a cleaner design without the heavy border if it's "weird".
# We'll use a stylized "V" and "G" with specific spacing.

refined_logo = """
      <div class="header__logo__vg z-1 js-header:logo" style="font-family: 'Yapari-SemiBold', sans-serif; font-size: 28px; color: white; letter-spacing: -2px; line-height: 1; font-weight: 600;">VG</div>
      <div class="js-header:logoMask">
        <div class="header__logo__name d-none d-block@sm pl-20 js-header:logoText" style="font-family: 'Monorama-Regular', sans-serif; font-size: 16px; color: white; letter-spacing: 4px; text-transform: uppercase; opacity: 0.9;">Viswa Gandamalla</div>
      </div>
"""

# Header Logo
# We need to target the messy state I left it in or the original state.
# Since I already ran a script, it might look like my previous replacement.
# Let's just target the specific container.
content = re.sub(r'<a href="index.html" class="header__logo d-flex items-center \| js-home-btn">.*?</a>', 
                 f'<a href="index.html" class="header__logo d-flex items-center | js-home-btn">{refined_logo.strip()}</a>', 
                 content, flags=re.DOTALL)

# Navigation Menu Logo
nav_logo = """
          <div class="header__logo__vg" style="font-family: 'Yapari-SemiBold', sans-serif; font-size: 28px; color: white; letter-spacing: -2px; line-height: 1; font-weight: 600;">VG</div>
          <div class="header__logo__name d-none d-block@sm pl-20" style="font-family: 'Monorama-Regular', sans-serif; font-size: 16px; color: white; letter-spacing: 4px; text-transform: uppercase; opacity: 0.9;">Viswa Gandamalla</div>
"""
content = re.sub(r'<a href="index.html" aria-label="Back to homepage" class="d-flex items-center logo opacity-0 absolute relative@smallDesk l-10 l-20@sm l-0@smallDesk">.*?</a>',
                 f'<a href="index.html" aria-label="Back to homepage" class="d-flex items-center logo opacity-0 absolute relative@smallDesk l-10 l-20@sm l-0@smallDesk">{nav_logo.strip()}</a>', 
                 content, flags=re.DOTALL)

# Footer Logo
footer_logo = """
                <div class="header__logo__vg" style="font-family: 'Yapari-SemiBold', sans-serif; font-size: 28px; color: white; letter-spacing: -2px; line-height: 1; font-weight: 600;">VG</div>
                <div class="header__logo__name d-none d-block@sm pl-20" style="font-family: 'Monorama-Regular', sans-serif; font-size: 16px; color: white; letter-spacing: 4px; text-transform: uppercase;">Viswa Gandamalla</div>
"""
content = re.sub(r'<a href="index.html" aria-label="Back to homepage" class="d-flex items-center logo absolute relative@smallDesk l-10 l-20@sm l-0@smallDesk center-x">.*?</a>',
                 f'<a href="index.html" aria-label="Back to homepage" class="d-flex items-center logo absolute relative@smallDesk l-10 l-20@sm l-0@smallDesk center-x">{footer_logo.strip()}</a>', 
                 content, flags=re.DOTALL)

# 3. Last check for specific branding strings
content = content.replace('Quai Network', 'Viswa Gandamalla')
content = content.replace('Quai', 'Viswa')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Final cleanup and logo polish complete.")
