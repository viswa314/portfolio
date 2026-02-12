import re

file_path = r'c:\My Web Sites\Portfolio\qu.ai\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Loader Persisting Text (Lines 418+)
content = content.replace('js-loader:mainText d-block t-14">/ launching_quai_network</p>', 'js-loader:mainText d-block t-14">/ Initialising Portfolio...</p>')
content = content.replace('js-loader:mainText d-block t-14">/ sequence_initiated</p>', 'js-loader:mainText d-block t-14">/ sequence_initiated</p>')

# 2. WebGL Panel Titles & Descriptions
replacements = {
    'Decentralization': 'Expertise: Python & AI',
    'governance by running a node or miner. With thousands of participants distributed across the globe, there is no\\s+single party with the ability to modify or turn off the network, ensuring zero network downtime.': 'Building advanced AI solutions using Python and Deep Learning frameworks. Focused on creating robust, scalable models for real-world applications in computer vision and data analysis.',
    'Scalability': 'Scalable Systems',
    'Quai Network automatically expands with demand to\\s+upwards of 50,000 TPS while keeping fees under \$0.01.': 'Designing high-performance systems capable of handling massive data throughput and real-time processing requirements for autonomous driving and robotics.',
    'Consensus': 'Core Competency: C++',
    'Transactions in Quai Network can be locally\\s+confirmed prior to global confirmation, offering high throughput with the shortest possible time to economic\\s+finality.': 'Developing efficient, low-level software solutions in C++. Expertise in memory management, performance optimization, and embedded systems architecture.',
    'Shared Security': 'Robotics & ROS2',
    'All blockchains within Quai Network share\\s+Proof-of-Work security through merged mining. Every Quai transaction is eventually confirmed by 100% of network\\s+hash power.': 'Extensive experience with Robot Operating System (ROS2). Designing sensor fusion algorithms and control systems for mobile robotics and autonomous platforms.',
    'Merge-Mined Parachains': 'Computer Vision',
    'Parachains inherit security and interoperability\\s+by merged mining with Quai Network, and create new incentives for miners and users.': 'Specializing in object detection, image segmentation, and scene understanding. Implementing state-of-the-art CNNs and Transformers for automotive safety.',
    'The Prime Chain': 'Path Planning',
    'The Prime blockchain acts as the &quot;knot&quot;\\s+tying all Quai Network chains together. The Prime blockchain braids sub networks together, facilitating the\\s+transfer of data across chains.': 'Implementing intelligent navigation and path planning algorithms. Expertise in SLAM, A*, and dynamic obstacle avoidance for mobile robots.',
    'Sub Networks': 'Deep Learning',
    'Quai&#039;s many high-speed sub networks\\s+independently and asynchronously process transactions. All sub networks are braided together by the Prime chain,\\s+ensuring shared security and interoperability across the network.': 'Mastery of neural network architectures, from GANs to RNNs. Applying deep learning to solve complex perception and prediction tasks in automotive engineering.'
}

for old, new in replacements.items():
    content = re.sub(old, new, content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Comprehensive cleanup complete.")
