import re

file_path = r'c:\My Web Sites\Portfolio\qu.ai\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix Research Article Titles
content = re.sub(
    r'Introducing StratumX: Fast, Non-Custodial, Non-KYC, Zero-Fee Solo Mining Infrastructure\s+Optimized for Quai Network',
    'Object Detection in Adverse Weather Conditions: A Deep Learning Approach for Autonomous Vehicles',
    content
)

content = re.sub(
    r'Project SOAP Launches on Quai Network: Turning Merge-Mining Into Continuous QUAI Buybacks',
    'Path Planning for Mobile Robots in Dynamic Environments using ROS2 and SLAM',
    content
)

content = re.sub(
    r'Project SOAP Mainnet Launch: Date Announcement and Next Steps for Miners',
    'A Comparative Study of CNN Architectures for Real-time Pedestrian Detection',
    content
)

# 2. Fix Footer Link "Media +" to "Research +"
content = content.replace('href="index.html#articles" role="menuitem">Media +</a>', 'href="index.html#articles" role="menuitem">Research +</a>')

# 3. Fix WebGL Labels
labels_map = {
    'Security': 'Python & AI',
    'Proof of Work': 'Deep Learning',
    'Scalability': 'Computer Vision',
    'Programmability': 'Robotics (ROS2)',
    'Interoperability': 'C++ & Embedded',
    'Efficiency': 'Autonomous Systems',
    'Decentralization': 'Path Planning',
    'Accessibility': 'Sensor Fusion'
}

for old, new in labels_map.items():
    # Attempt to match with potential whitespace/tags
    content = re.sub(f'<span>{old}</span>', f'<span>{new}</span>', content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Replacement complete.")
