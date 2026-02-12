import re

file_path = r'c:\My Web Sites\Portfolio\qu.ai\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Project Panels (TurtleBot3, ROS2, RAG)
# Panel 0: Computer Vision -> Object Detection for TurtleBot3
content = content.replace('Computer Vision</h3>', 'Object Detection for TurtleBot3 (Master Thesis)</h3>')
content = content.replace('Implementation of real-time object detection and segmentation for autonomous driving.', 
                          'Design and evaluation of AI workflows using YOLOv8, RT-DETR, and HOG+SVM on TurtleBot3 (RealSense D405). Achieved 88.7% mAP with YOLOv8.')

# Panel 1: Robotics (ROS2) -> Autonome Feldrobotik mit ROS 2
content = content.replace('Robotics (ROS2)</h3>', 'Autonome Feldrobotik mit ROS 2</h3>')
content = content.replace('Developing robust robot control systems and sensor fusion algorithms using ROS2 and C++.', 
                          'Implementing an autonomous robotics stack with ROS 2 Humble and Gazebo: Custom Controller, Nav2 Stack, and SLAM Toolbox.')

# Panel 2: Deep Learning -> RAG Chatbot
content = content.replace('Deep Learning</h3>', 'End-to-End Conversational RAG Chatbot</h3>')
content = content.replace('Advanced neural network architectures for predictive modeling and pattern recognition.', 
                          'LangChain-based RAG chatbot integrating OpenAI LLMs, Hugging Face embeddings, and AstraDB for document-aware Q&A.')

# 2. Cleanup Panel 2 links (removing block explorer remnants)
block_removal = r'<ul class="list-unstyled mb-0 mt-30@md">.*?</ul>'
content = re.sub(block_removal, '<p class="mt-20">Stack: Python, LangChain, OpenAI API, Hugging Face, AstraDB, Streamlit.</p>', content, flags=re.DOTALL)

# 3. Research section cleanup (removing old blog links and syncing names)
content = content.replace('Object Detection in Adverse Weather Conditions: A Deep Learning Approach for Autonomous Vehicles', 
                          'Leveraging BERT for High-Precision Authorship Attribution Across Diverse Texts (Accepted at IEEE ICACT 2025)')
content = content.replace('Path Planning for Mobile Robots in Dynamic Environments using ROS2 and SLAM', 
                          'Monokulare Visuelle Odometrie (ORB-SLAM3 Integration) - Real-time trajectory estimation on EuroC dataset')
content = content.replace('A Comparative Study of CNN Architectures for Real-time Pedestrian Detection', 
                          'Powerline-Erkennung aus 3D-LiDAR-Punktwolken (Toronto-3D) - Geometrie-basierte Erkennung mittels PCA and RANSAC')

# 4. Correcting the project dates in research subtitles
content = content.replace('01/07/2026', 'ICACT 2025')
content = content.replace('12/18/2025', 'Feb 2026')
content = content.replace('12/12/2025', 'Feb 2026')

# 5. Skills list final polish (matching exactly)
content = content.replace('innovative ai systems', 'ADAS Systems')
content = content.replace('sustainable automotive tech', 'ROS2 Robotics')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Final project alignment complete.")
