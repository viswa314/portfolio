import re

file_path = r'c:\My Web Sites\Portfolio\qu.ai\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Redesign Footer Blocks
# Replace 'Developers' block with 'Profiles'
developers_block = r'<div class="footer__block">.*?<span>&gt; Developers</span>.*?<ul role="menubar" aria-label="Developer links" class="list-unstyled">.*?<li class="js-button no-scramble">.*?<a class="t-nowrap@md t-lh-18 t-lh-20@sm t-lh-30@smallDesk" href="https://shorturl.at/dhnz7".*?role="menuitem" target="_blank" rel="noopener noreferrer">Docs \+</a>.*?</li>.*?<li class="js-button no-scramble">.*?<a class="t-nowrap@md t-lh-18 t-lh-20@sm t-lh-30@smallDesk".*?href="https://github.com/viswa314" role="menuitem" target="_blank".*?rel="noopener noreferrer">Code \+</a>.*?</li>.*?</ul>.*?</div>'

profiles_block = """
              <div class="footer__block">
                <span>&gt; Profiles</span>
                <ul role="menubar" aria-label="Profile links" class="list-unstyled">
                  <li class="js-button no-scramble">
                    <a class="t-nowrap@md t-lh-18 t-lh-20@sm t-lh-30@smallDesk" href="https://github.com/viswa314"
                      role="menuitem" target="_blank" rel="noopener noreferrer">GitHub +</a>
                  </li>
                  <li class="js-button no-scramble">
                    <a class="t-nowrap@md t-lh-18 t-lh-20@sm t-lh-30@smallDesk"
                      href="https://de.linkedin.com/in/viswa-gandamalla-2064101b4" role="menuitem" target="_blank"
                      rel="noopener noreferrer">LinkedIn +</a>
                  </li>
                </ul>
              </div>
"""

content = re.sub(developers_block, profiles_block.strip(), content, flags=re.DOTALL)

# Replace 'Network' block with 'Connect'
network_block = r'<div class="footer__block pt-0 pt-30@sm pt-0@smallDesk">.*?<span>&gt; Certifications</span>.*?<ul role="menubar" aria-label="Certification links" class="list-unstyled">.*?</ul>.*?</div>'
# Wait, I previously changed it to Certifications. The user's screenshot still shows 'Network'. 
# Maybe my previous edit didn't stick or it's a different block. 
# Let's target strictly what's in the file now.
# In the file it says 'Certifications'. I will change it to 'Connect'.

content = content.replace('<span>&gt; Certifications</span>', '<span>&gt; Connect</span>')
content = content.replace('aria-label="Certification links"', 'aria-label="Connect links"')

# Add Address and Phone to Connect block (currently it has Certs)
connect_content = """
              <div class="footer__block pt-0 pt-30@sm pt-0@smallDesk">
                <span>&gt; Connect</span>
                <ul role="menubar" aria-label="Connect links" class="list-unstyled">
                  <li role="none" class="js-button no-scramble">
                    <a class="t-nowrap@md t-lh-18 t-lh-20@sm t-lh-30@smallDesk" href="mailto:viswagandamalla@gmail.com"
                      role="menuitem" target="_blank" rel="noopener noreferrer">Email +</a>
                  </li>
                  <li role="none" class="js-button no-scramble">
                    <a class="t-nowrap@md t-lh-18 t-lh-20@sm t-lh-30@smallDesk" href="tel:+4915758074771"
                      role="menuitem" target="_blank" rel="noopener noreferrer">Phone +</a>
                  </li>
                  <li role="none" class="js-button no-scramble">
                    <a class="t-nowrap@md t-lh-18 t-lh-20@sm t-lh-30@smallDesk" href="#"
                       role="menuitem">Address +</a>
                  </li>
                </ul>
              </div>
"""
# Replacing the block I just tried to edit
content = re.sub(r'<div class="footer__block pt-0 pt-30@sm pt-0@smallDesk">.*?<span>&gt; Connect</span>.*?</ul>.*?</div>', connect_content.strip(), content, flags=re.DOTALL)

# 2. Fix 3D Label Hallucinations
content = content.replace('All Viswa Gandamalla blockchains', 'All autonomous systems')
content = content.replace('Viswa allows anyone to participate', 'Our frameworks allow seamless participation')
content = content.replace('Every Viswa transaction', 'Every data process')
content = content.replace('Viswa\'s many high-speed sub networks', 'Distributed sensor networks')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Footer redesign and label correction complete.")
