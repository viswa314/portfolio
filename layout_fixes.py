import re

file_path = r'c:\My Web Sites\Portfolio\qu.ai\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Rebrand Top-Left Logo (Header and Nav Overlay)
# Replace Quai logo SVGs with custom text-based Branding "VG"
logo_replacement = """
      <div class="header__logo__vg z-1 js-header:logo" style="font-family: 'Yapari-SemiBold', sans-serif; font-size: 24px; color: white; border: 2px solid white; padding: 5px 10px; line-height: 1;">VG</div>
      <div class="js-header:logoMask">
        <div class="header__logo__name d-none d-block@sm pl-15 js-header:logoText" style="font-family: 'Monorama-Regular', sans-serif; font-size: 18px; color: white; letter-spacing: 2px; text-transform: uppercase;">Viswa Gandamalla</div>
      </div>
"""

# Header Logo
content = re.sub(r'<svg aria-hidden="true" class=\'header__logo__circle \| z-1 \| js-header:logo\'>.*?</svg>.*?<div class="js-header:logoMask">.*?<svg aria-hidden="true" class=\'header__logo__text d-none d-block@sm pl-15 \| js-header:logoText\'>.*?</svg>.*?</div>', 
                 logo_replacement.strip(), content, flags=re.DOTALL)

# Nav Overlay Logo (Simplified)
nav_logo_replacement = """
          <div class="header__logo__vg" style="font-family: 'Yapari-SemiBold', sans-serif; font-size: 24px; color: white; border: 2px solid white; padding: 5px 10px; line-height: 1;">VG</div>
          <div class="header__logo__name d-none d-block@sm pl-15" style="font-family: 'Monorama-Regular', sans-serif; font-size: 18px; color: white; letter-spacing: 2px; text-transform: uppercase;">Viswa Gandamalla</div>
"""
content = re.sub(r'<a href="index.html" aria-label="Back to homepage" class="d-flex items-center logo opacity-0 absolute relative@smallDesk l-10 l-20@sm l-0@smallDesk">.*?<svg aria-hidden="true" class=\'header__logo__circle\'>.*?</svg>.*?<svg aria-hidden="true" class=\'header__logo__text d-none d-block@sm pl-15\'>.*?</svg>.*?</a>',
                 f'<a href="index.html" aria-label="Back to homepage" class="d-flex items-center logo opacity-0 absolute relative@smallDesk l-10 l-20@sm l-0@smallDesk">{nav_logo_replacement.strip()}</a>', content, flags=re.DOTALL)

# Footer Logo
footer_logo_replacement = """
                <div class="header__logo__vg" style="font-family: 'Yapari-SemiBold', sans-serif; font-size: 24px; color: white; border: 2px solid white; padding: 5px 10px; line-height: 1;">VG</div>
                <div class="header__logo__name d-none d-block@sm pl-15" style="font-family: 'Monorama-Regular', sans-serif; font-size: 18px; color: white; letter-spacing: 2px; text-transform: uppercase;">Viswa Gandamalla</div>
"""
content = re.sub(r'<a href="index.html" aria-label="Back to homepage" class="d-flex items-center logo absolute relative@smallDesk l-10 l-20@sm l-0@smallDesk center-x">.*?<svg aria-hidden="true" class=\'header__logo__circle\'>.*?</svg>.*?<svg aria-hidden="true" class=\'header__logo__text\'>.*?</svg>.*?</a>',
                 f'<a href="index.html" aria-label="Back to homepage" class="d-flex items-center logo absolute relative@smallDesk l-10 l-20@sm l-0@smallDesk center-x">{footer_logo_replacement.strip()}</a>', content, flags=re.DOTALL)

# 2. Fix Education Section Layout (Overlapping items)
# I will change the flex configuration and add more vertical spacing and clear width constraints.
content = content.replace('class="partners__container d-flex flex-column flex-row@md items-center justify-center@md flex-wrap@md"', 
                          'class="partners__container d-flex flex-column items-center justify-center"')

# Add more margin and reduce width to prevent side-by-side overlap on certain breakpoints
content = content.replace('class="partners__block d-flex flex-column items-center  mb-40 mb-80@sm "', 
                          'class="partners__block d-flex flex-column items-center mb-80 w-1/1 max-w-600px"')
content = content.replace('class="partners__block d-flex flex-column items-center "', 
                          'class="partners__block d-flex flex-column items-center mb-80 w-1/1 max-w-600px"')

# Shorten THI title in the H3 and place dates in description or span
content = content.replace('<span class="t-nowrap">University of Rostock (Oct 2025 - Present)</span>', 
                          '<span class="t-nowrap">University of Rostock</span><br><span style="font-size: 14px; opacity: 0.8;">Oct 2025 - Present</span>')
content = content.replace('<span class="t-nowrap">Technische Hochschule Ingolstadt (Oct 2021 - Sep 2025)</span>', 
                          '<span class="t-nowrap">TH Ingolstadt</span><br><span style="font-size: 14px; opacity: 0.8;">Oct 2021 - Sep 2025</span>')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Layout fixes and rebranding complete.")
