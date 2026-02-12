import re

file_path = r'c:\My Web Sites\Portfolio\qu.ai\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Technical Expertise Paragraph Update
# Precise match from the latest view
old_p = """My technical arsenal includes Python, C/C++, and specialized libraries like OpenCV, TensorFlow, and
                  PyTorch.
                  I am proficient in ROS2 for robotics integration and have deep experience in Automotive SPICE, ISO
                  26262,
                  and ISTQB testing methodologies. My research interests lie in the intersection of Computer Vision
                  and real-time autonomous systems."""

new_p = """My technical arsenal includes Python, C, C++, ROS2, and CAPL, with expertise in Deep Learning (PyTorch, TensorFlow) and Computer Vision (OpenCV). 
                  I am proficient in Automotive Standards like ISO 26262 and AUTOSAR, and experienced in Simulation tools such as MATLAB/Simulink and CANoe. 
                  My research focuses on real-time autonomous systems and object detection. I hold an EU Class B Driver's License and Audi FFZ certification."""

content = content.replace(old_p, new_p)

# 2. Hobby Projects / Marquee alignment - Double checking names
content = content.replace('t-600">Payment</p>', 't-600">Computer Vision</p>')
content = content.replace('t-600">Gaming</p>', 't-600">Deep Learning</p>')
content = content.replace('t-600">NFTs</p>', 't-600">ROS2 Robotics</p>')
content = content.replace('t-600">Social</p>', 't-300">ADAS Systems</p>')

# 3. Work Experience section final check
content = content.replace('Graduate Research Assistant at ZF Group', 'Student Assistant at CARISSMA')
content = content.replace('System Test Engineer at Bosch Global Software Technologies', 'Master Thesis Student at Akkodis')

# 4. Final corporate residue check
content = content.replace('Dominant Strategies', 'Viswa Gandamalla')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Meticulous synchronization complete.")
