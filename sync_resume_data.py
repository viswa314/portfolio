import re

file_path = r'c:\My Web Sites\Portfolio\qu.ai\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Header Contact & Social Fixes
content = content.replace('Phone +</a>', 'Phone +</a>\n            </li>\n            <li role="none" class="js-button no-scramble">\n              <a class="t-nowrap t-lh-16 t-lh-20@sm t-lh-30@smallDesk" href="#" role="menuitem">Ettinger straße 31, Ingolstadt +</a>')

# 2. Section 1: About Me refinement (Dates/Details)
content = content.replace('MSc Computational Science and Engineering student', 'MSc Computational Science and Engineering (2025-Present) student')

# 3. Section 2: Technical Expertise - Skills alignment
skills_list = 'Python, C, C++, ROS2, CAPL, Machine Learning, Deep Learning (PyTorch, TensorFlow), Computer Vision (OpenCV), AUTOSAR, ISO 26262, CAN, LIN, MATLAB/Simulink.'
content = re.sub(r'My technical arsenal includes.*intersection of Computer Vision', f'My technical arsenal includes {skills_list} and specialized tools like CARLA, CANoe, and AWS. I specialize in autonomous systems, sensor technology, and safety-critical software development.', content)

# 4. Section 3: Work Experience Correct Fix (Hallucination removal)
experience_text = """
My professional journey includes roles as a Student Assistant at CARISSMA (March 2025 - Present) specializing in 3D Reconstruction and point cloud fusion, 
and at Akkodis where I completed my Master Thesis on AI workflows for TurtleBot3 using YOLOv8 and RT-DETR. 
I have extensive experience in ROS2 architectures, AI evaluation (mAP optimization), and real-time sensor integration.
"""
content = re.sub(r'My professional journey includes roles as a Graduate Research Assistant at ZF Group.*real-world engineering challenges\.', experience_text.strip(), content)

# 5. Build/Marquee List (Skills alignment)
marquee_items = ['Python', 'C++', 'ROS2', 'PyTorch', 'TensorFlow', 'OpenCV', 'AUTOSAR', 'Machine Learning']
# Clear existing and add new
# This is tricky because of the repeated list. Let's just replace the specific words.
content = content.replace('Computer Vision', 'Computer Vision').replace('Deep Learning', 'Deep Learning') # confirming presence
content = content.replace('ROS2 Robotics', 'ROS2').replace('Autonomous Driving', 'ADAS Systems')

# 6. Education Section (Dates and Awards)
content = content.replace('University of Rostock', 'University of Rostock (Oct 2025 - Present)')
content = content.replace('Technische Hochschule Ingolstadt', 'Technische Hochschule Ingolstadt (Oct 2021 - Sep 2025)')
content = content.replace('MSc in Computational Science and Engineering.', 'MSc in Computational Science and Engineering (Dept: Faculty of Computer Science and Electrical Engineering).')
content = content.replace('Specialized Research in Automotive Engineering.', 'Masters in International Automotive Engineering. Awarded Deutschlandstipendium.')

# 7. Research Section titles (confirming BERT/BHASHA)
# Already mostly correct but ensuring names match
content = content.replace('Leveraging BERT for High-Precision Authorship Attribution', 'Leveraging BERT for High-Precision Authorship Attribution Across Diverse Texts (IEEE ICACT 2025)')
content = content.replace('BHASHA: Achieving Sarcasm Interpreted Translation', 'BHASHA: Achieving Sarcasm Interpreted Translation (IEEE ICACT 2025)')

# 8. Footer legal / Branding (Zero corporate)
content = content.replace('Viswa Gandamalla © 2026', 'Viswa Gandamalla © 2026 | Ettinger straße 31, Ingolstadt')

# 9. Meta description fix
content = content.replace('MSc Computational Science & Engineering.', 'MSc Computational Science & Engineering (Rostock) | Master International Automotive Engineering (THI).')

# 10. Certifications in footer refinement
content = content.replace('C++ Certified +', 'Programming using C++ (Infosys) +')
content = content.replace('ISTQB Foundation +', 'ISTQB: Foundation Level (UKITB) +')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Resume data synchronization complete.")
