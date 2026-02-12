import re

file_path = r'c:\My Web Sites\Portfolio\qu.ai\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Marquee items cleanup (Crypto/Blockchain terms -> Engineering terms)
marquee_replacements = {
    'Payment': 'Computer Vision',
    'Gaming': 'Deep Learning',
    'NFTs': 'ROS2 Robotics',
    'Social': 'Autonomous Driving',
    'DeFi': 'Sensor Fusion',
    'Metaverse': 'AI Engineering',
    'Identity': 'C++ Development',
    'DAOs': 'Embedded Systems'
}

for old, new in marquee_replacements.items():
    content = content.replace(f't-600">{old}</p>', f't-600">{new}</p>')

# 2. VC firm link removal (Education section)
content = content.replace('href="https://polychain.capital/"', 'href="#"')
content = content.replace('href="https://www.av.vc/"', 'href="#"')
content = content.replace('href="https://www.linkedin.com/company/zero1-capital/"', 'href="#"')

# 3. GitHub/Company link removal
content = content.replace('href="https://github.com/dominant-strategies"', 'href="https://github.com/viswa314"')
content = content.replace('Dominant Strategies', 'Viswa Gandamalla')

# 4. Loader initialization text refinement
content = content.replace('/ launching_quai_network', '/ initializing_cv_system')
content = content.replace('/ sequence_initiated', '/ sequence_initiated') # Already restored but confirming structure

# 5. WebGL Panel descriptions - final scrub of networking terms
content = content.replace('all blockchains within Quai Network', 'all automotive systems')
content = content.replace('Every Quai transaction', 'Every algorithmic process')
content = content.replace('Quai transaction', 'System event')
content = content.replace('Prime blockchain', 'Central Controller')
content = content.replace('Quai\'s many high-speed sub networks', 'Distributed sensor nodes')
content = content.replace('the Prime chain', 'the core backbone')
content = content.replace('braided networks', 'integrated systems')

# 6. Meta/Head cleanup
content = re.sub(r'Mirrored from qu\.ai/.*GMT', 'Personal Portfolio', content)
content = content.replace('name="generator" content="Portfolio Website"', 'name="generator" content="Viswa Gandamalla Portfolio"')

# 7. Discard corporate spec rules/prefetching
# Removing the speculationrules or making it neutral
content = re.sub(r'"\/wp-content\/themes\/quai\/\*"', '"/wp-content/*"', content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Final branding scrub complete.")
