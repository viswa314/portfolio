import re

file_path = r'c:\My Web Sites\Portfolio\qu.ai\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Secondary Footer Links
content = content.replace('href="https://wellfound.com/company/dominant-strategies" role="menuitem" target="_blank"\n                      rel="noopener noreferrer">Careers +</a>', 'href="blog/index.html" role="menuitem">Resume +</a>')
content = content.replace('href="disclaimers/index.html"\n                      role="menuitem">Disclaimers +</a>', 'href="disclaimers/index.html" role="menuitem">Photography +</a>')
content = content.replace('href="privacy-policy/index.html"\n                      role="menuitem">Privacy Policy +</a>', 'href="privacy-policy/index.html" role="menuitem">Hiking +</a>')
content = content.replace('href="terms-and-conditions/index.html"\n                      role="menuitem">T&amp;C&#039;s +</a>', 'href="terms-and-conditions/index.html" role="menuitem">Chess +</a>')

# 2. Connect With Us -> Find Me Online
content = content.replace('Connect With Us:', 'Find Me Online:')

# 3. Social Links (Specific URLs)
content = re.sub(r'https://twitter\.com/QuaiNetwork', 'https://github.com/viswa314', content)
content = re.sub(r'https://discord\.com/invite/ngw88VXXnV', 'https://de.linkedin.com/in/viswa-gandamalla-2064101b4', content)
content = re.sub(r'https://www\.reddit\.com/r/quainetwork/', 'mailto:viswagandamalla@gmail.com', content)
content = re.sub(r'https://www\.youtube\.com/channel/UCA7wfK91O1CmwHm4LELnNHw', 'https://github.com/viswa314', content)
content = re.sub(r'https://www\.instagram\.com/quainetwork', 'https://de.linkedin.com/in/viswa-gandamalla-2064101b4', content)
content = re.sub(r'https://www\.tiktok\.com/@quainetwork', 'mailto:viswagandamalla@gmail.com', content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Final cleanup complete.")
