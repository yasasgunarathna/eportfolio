import streamlit as st
from streamlit_option_menu import option_menu

# Set up the page configuration
st.set_page_config(page_title="Yasas Gunarathne - ICT Professional ePortfolio", layout="wide")

# Define CSS for custom styling
st.markdown("""
    <style>
        .main-title {
            font-size: 3.5rem;
            color: #FF0000; /* Red theme */
            font-weight: bold;
            text-align: center;
        }
        .section-title {
            font-size: 2.8rem;
            color: #FF4500; /* Slightly darker red */
            font-weight: bold;
            margin-bottom: 20px;
        }
        .content {
            font-size: 1.4rem;
            line-height: 2;
            color: #333;
        }
        .contact-info {
            font-size: 1.4rem;
            line-height: 2.5;
            color: #000;
        }
        .custom-menu {
            background-color: #FFF0F0; /* Light red background */
            padding: 10px;
            border-radius: 8px;
        }
        .streamlit-option-menu > div {
            font-size: 1.3rem;
        }
        ul {
            line-height: 1.8;
        }
    </style>
""", unsafe_allow_html=True)

# Horizontal navigation menu with red theme
selected = option_menu(
    menu_title=None,
    options=["Home", "About Me", "Résumé", "Work Samples", "Skills", "Future Goals", "Contact"],
    icons=["house", "person", "briefcase", "folder", "tool", "target", "envelope"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#FFF0F0"},  # Light red
        "icon": {"color": "red", "font-size": "20px"},
        "nav-link": {"font-size": "18px", "text-align": "center", "margin": "0px", "--hover-color": "#FFE4E1"},
        "nav-link-selected": {"background-color": "#FF4500", "color": "white"},
    },
)
# Home Section
if selected == "Home":
    st.markdown("<h1 class='main-title'>Welcome to My ICT Professional ePortfolio</h1>", unsafe_allow_html=True)
    
    # Introduction Section
    st.markdown("""
    <div class='content'>
        <p>I’m <strong>Yasas Gunarathne</strong>, an ICT Professional with a passion for creating innovative, user-centered 
        technological solutions. My expertise spans software engineering, network troubleshooting, and project management, 
        with a strong focus on delivering impactful results in the ICT industry.</p>
    </div>
    <hr style="border:1px solid #FF4500; margin: 20px 0;"> <!-- Divider -->
    """, unsafe_allow_html=True)
    
    # Professional Journey Section
    st.markdown("""
    <div class='content'>
        <h2 style='color: #FF0000;'>Professional Journey</h2>
        <p>Over the years, I have honed my skills through academic achievements and hands-on experience. With a solid foundation 
        in software development and ICT infrastructure management, I am committed to leveraging my technical expertise to solve 
        real-world challenges. My journey has taken me from academic research to professional roles in government and private sectors, 
        where I successfully collaborated on projects requiring advanced problem-solving and leadership.</p>
    </div>
    <hr style="border:1px solid #FF4500; margin: 20px 0;"> <!-- Divider -->
    """, unsafe_allow_html=True)
    
    # Highlights Section
    st.markdown("""
    <div class='content'>
        <h2 style='color: #FF0000;'>Key Highlights</h2>
        <ul style='line-height: 1.8;'>
            <li><strong>Development of an Indigenous Travel App</strong>: Integrated cutting-edge features to promote cultural awareness.</li>
            <li><strong>Research on Mobile Banking Optimization</strong>: Improved user engagement and accessibility through data analysis.</li>
            <li><strong>ICT Infrastructure Projects</strong>: Contributed to projects that enhanced organizational efficiency.</li>
        </ul>
    </div>
    <hr style="border:1px solid #FF4500; margin: 20px 0;"> <!-- Divider -->
    """, unsafe_allow_html=True)
    
    # Goals Section
    st.markdown("""
    <div class='content'>
        <h2 style='color: #FF0000;'>Looking Ahead</h2>
        <p>Beyond my professional pursuits, I am deeply interested in emerging technologies such as cloud computing, artificial 
        intelligence, and sustainable ICT practices. My short-term goal is to secure a specialized role in software development 
        or network engineering, while my long-term aspiration is to lead transformative ICT projects that drive innovation and sustainability.</p>
    </div>
    <hr style="border:1px solid #FF4500; margin: 20px 0;"> <!-- Divider -->
    """, unsafe_allow_html=True)
    
    # Call-to-Action Section
    st.markdown("""
    <div class='content'>
        <h2 style='color: #FF0000;'>Explore and Connect</h2>
        <p>I invite you to explore my portfolio and learn more about my academic journey, professional experiences, and aspirations. 
        Feel free to reach out for collaboration, networking, or professional opportunities.</p>
    </div>
    """, unsafe_allow_html=True)

# About Me Section
if selected == "About Me":
    st.markdown("<h1 class='section-title'>About Me</h1>", unsafe_allow_html=True)
    
    # Professional Overview
    st.markdown("""
    <div class='content'>
        <h2 style='color: #FF0000;'>Professional Background</h2>
        <p>I am a highly motivated ICT professional with a rich blend of academic and practical experience in software development, 
        network management, and project leadership. My journey in technology began with a strong academic foundation, and I have 
        continuously built on this with hands-on roles in diverse settings, including both public and private sectors.</p>
    </div>
    <hr style="border:1px solid #FF4500; margin: 20px 0;"> <!-- Divider -->
    """, unsafe_allow_html=True)
    
    # Core Values and Philosophy
    st.markdown("""
    <div class='content'>
        <h2 style='color: #FF0000;'>Core Values and Philosophy</h2>
        <p>At the heart of my professional ethos is a commitment to innovation, ethics, and collaboration. I believe in leveraging 
        technology to create meaningful solutions that address real-world challenges while adhering to the highest standards of integrity.</p>
        <p>My work philosophy emphasizes:</p>
        <ul style='line-height: 1.8;'>
            <li>Collaborative teamwork and mutual respect</li>
            <li>Continuous learning and adaptability</li>
            <li>Delivering results with precision and accountability</li>
        </ul>
    </div>
    <hr style="border:1px solid #FF4500; margin: 20px 0;"> <!-- Divider -->
    """, unsafe_allow_html=True)

    # Skills and Expertise Highlights
    st.markdown("""
    <div class='content'>
        <h2 style='color: #FF0000;'>Skills and Expertise</h2>
        <table style="width: 100%; border-collapse: collapse;">
            <tr style="background-color: #FFEEEE;">
                <th style="padding: 10px; text-align: left; border: 1px solid #FF4500;">Skill</th>
                <th style="padding: 10px; text-align: left; border: 1px solid #FF4500;">Expertise Level</th>
            </tr>
            <tr>
                <td style="padding: 10px; border: 1px solid #FF4500;">Software Development</td>
                <td style="padding: 10px; border: 1px solid #FF4500;">Advanced</td>
            </tr>
            <tr>
                <td style="padding: 10px; border: 1px solid #FF4500;">Network Administration</td>
                <td style="padding: 10px; border: 1px solid #FF4500;">Advanced</td>
            </tr>
            <tr>
                <td style="padding: 10px; border: 1px solid #FF4500;">Project Management</td>
                <td style="padding: 10px; border: 1px solid #FF4500;">Intermediate</td>
            </tr>
            <tr>
                <td style="padding: 10px; border: 1px solid #FF4500;">Data Analysis</td>
                <td style="padding: 10px; border: 1px solid #FF4500;">Intermediate</td>
            </tr>
        </table>
    </div>
    <hr style="border:1px solid #FF4500; margin: 20px 0;"> <!-- Divider -->
    """, unsafe_allow_html=True)
    
    # Personal Interests
    st.markdown("""
    <div class='content'>
        <h2 style='color: #FF0000;'>Personal Interests</h2>
        <p>Outside of work, I am an advocate for sustainable technology and innovation. I enjoy exploring the intersection of 
        artificial intelligence and ethical computing, and I am passionate about mentoring aspiring tech enthusiasts.</p>
        <p>Additionally, I enjoy outdoor activities, reading about advancements in technology, and contributing to community-driven 
        ICT projects that make a tangible difference.</p>
    </div>
    """, unsafe_allow_html=True)
# Résumé Section
elif selected == "Résumé":
    # Title
    st.markdown("<h1 style='color: #FF4500; text-align: center; font-size: 36px;'>Résumé</h1>", unsafe_allow_html=True)

    # Tabbed Layout with Styled Tabs
    tab1, tab2, tab3, tab4 = st.tabs(["📘 Education", "💼 Experience", "📜 Certifications", "🏆 Achievements"])

    # Education Tab
    with tab1:
        st.markdown("""
        <div style="font-size: 18px; line-height: 1.8;">
        <h3 style="color: #FF4500;">Education</h3>
        - <b>Master’s Degree in Information Technology</b> (2023–2025) - <i>University of Southern Queensland</i><br>
          Building expertise in software development, AI integration, and cloud technologies.<br><br>
        - <b>BSc in Software Engineering</b> (2018–2021) - <i>Cardiff Metropolitan University</i><br>
          Conducted research on mobile banking and tea marketing industries in Sri Lanka.<br><br>
        - <b>Higher National Diploma in Software Engineering</b> (2018–2020) - <i>ICBT Campus</i><br>
          Focused on practical IT skills, including network engineering and database management.<br><br>
        - <b>Advanced Diploma in Computer Network Engineering</b> (2019–2020) - <i>IDM Nations Campus</i><br>
          Specialized in network diagnostics and administration.
        </div>
        """, unsafe_allow_html=True)

    # Experience Tab
    with tab2:
        st.markdown("""
        <div style="font-size: 18px; line-height: 1.8;">
        <h3 style="color: #FF4500;">Professional Experience</h3>
        <b>Government ICT Trainee (2022)</b><br>
        - Optimized ICT infrastructure across government departments.<br>
        - Improved system uptime and supported end-user issues.<br><br>

        <b>Network & Hardware Trainee (2022) - Metro Computer Services</b><br>
        - Installed and managed enterprise hardware systems.<br>
        - Enhanced network security and resolved technical issues efficiently.<br><br>

        <b>Computer Operator (2017–2018) - Hasitha Tyre Service Center</b><br>
        - Maintained and streamlined office IT operations.<br>
        - Ensured data integrity and system reliability.<br>
        </div>
        """, unsafe_allow_html=True)

    # Certifications Tab
    with tab3:
        st.markdown("""
        <div style="font-size: 18px; line-height: 1.8;">
        <h3 style="color: #FF4500;">Certifications</h3>
        - <b>Google IT Support Professional Certificate</b> - Google<br>
        - <b>Microsoft Certified: Azure Fundamentals</b> - Microsoft<br>
        - <b>Cisco Certified Network Associate (CCNA)</b> - In Progress<br>
        - <b>Scrum Fundamentals Certified</b> - Scrum Alliance<br>
        </div>
        """, unsafe_allow_html=True)

    # Achievements Tab
    with tab4:
        st.markdown("""
        <div style="font-size: 18px; line-height: 1.8;">
        <h3 style="color: #FF4500;">Key Achievements</h3>
        - Successfully led the development of the <b>Indigenous Travel App</b> integrating cutting-edge features.<br>
        - Conducted research on <b>Mobile Banking Optimization</b>, enhancing user engagement.<br>
        - Implemented network solutions that reduced downtime by 20% in government systems.<br>
        - Received "Best Trainee" award at Metro Computer Services.<br>
        </div>
        """, unsafe_allow_html=True)

# Work Samples Section
elif selected == "Work Samples":
    # Title
    st.markdown("<h1 style='color: #FF4500; text-align: center; font-size: 36px;'>Work Samples</h1>", unsafe_allow_html=True)
    
    # Create Cards for Each Work Sample
    st.markdown("""
    <style>
    .card {
        background-color: #f9f9f9;
        border: 1px solid #ddd;
        border-radius: 10px;
        padding: 20px;
        margin: 20px 0;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
    }
    .card-title {
        font-size: 22px;
        color: #FF4500;
        font-weight: bold;
    }
    .card-content {
        font-size: 18px;
        color: #333;
        line-height: 1.6;
    }
    </style>
    """, unsafe_allow_html=True)

    # Indigenous Travel App
    st.markdown("""
    <div class="card">
        <p class="card-title">Indigenous Travel App</p>
        <div class="card-content">
            <ul>
                <li>Developed an app to promote Indigenous culture and support local businesses.</li>
                <li>Integrated features like audio storytelling, dynamic maps with custom markers, and offline functionality.</li>
                <li>Received recognition for innovation in enhancing cultural awareness through technology.</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Mobile Banking Research
    st.markdown("""
    <div class="card">
        <p class="card-title">Mobile Banking Research</p>
        <div class="card-content">
            <ul>
                <li>Conducted research to optimize user experience in mobile banking systems.</li>
                <li>Utilized data analytics to identify pain points and improve functionality.</li>
                <li>Proposed innovative solutions to enhance security and accessibility in digital banking.</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Tea Marketing Optimization
    st.markdown("""
    <div class="card">
        <p class="card-title">Tea Marketing Optimization</p>
        <div class="card-content">
            <ul>
                <li>Analyzed supply chain processes in the Sri Lankan tea industry.</li>
                <li>Proposed actionable strategies to streamline logistics and increase profitability.</li>
                <li>Collaborated with industry experts to implement optimization techniques.</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Additional Work Sample: E-Learning Platform
    st.markdown("""
    <div class="card">
        <p class="card-title">E-Learning Platform Development</p>
        <div class="card-content">
            <ul>
                <li>Designed and developed an interactive e-learning platform for students and educators.</li>
                <li>Implemented features like live quizzes, progress tracking, and video lessons.</li>
                <li>Improved user engagement by 30% through intuitive design and gamification techniques.</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Additional Work Sample: Smart Home Automation System
    st.markdown("""
    <div class="card">
        <p class="card-title">Smart Home Automation System</p>
        <div class="card-content">
            <ul>
                <li>Developed a smart home system to control lighting, temperature, and security remotely.</li>
                <li>Integrated IoT devices with a user-friendly mobile application.</li>
                <li>Reduced energy consumption by 15% through efficient automation strategies.</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Closing Section
    st.markdown("""
    <div style="text-align: center; margin-top: 40px;">
        <p style="font-size: 18px; color: #333;">Explore my portfolio to see how I bring innovation and impact to every project. Feel free to reach out for collaboration opportunities!</p>
    </div>
    """, unsafe_allow_html=True)

# Skills Section
elif selected == "Skills":
    st.markdown("<h1 class='section-title' style='text-align: center; color: #FF4500;'>Skills</h1>", unsafe_allow_html=True)

    # Technical Skills
    st.markdown("""
        <div style='background-color: #F9F9F9; padding: 20px; margin-bottom: 20px; border-radius: 8px;'>
            <h3 style='color: #FF4500;'>Technical Skills</h3>
            <ul style='font-size: 16px; line-height: 1.6;'>
                <li>Networking and System Administration (Linux, Windows Server)</li>
                <li>Software Development (Flutter, Dart, Python, JavaScript)</li>
                <li>Cloud Computing (AWS, Azure Fundamentals)</li>
                <li>Database Management (MySQL, PostgreSQL)</li>
                <li>Hardware Troubleshooting and Maintenance</li>
                <li>Web Development (HTML, CSS, ReactJS)</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

    # Soft Skills
    st.markdown("""
        <div style='background-color: #F9F9F9; padding: 20px; margin-bottom: 20px; border-radius: 8px;'>
            <h3 style='color: #FF4500;'>Soft Skills</h3>
            <ul style='font-size: 16px; line-height: 1.6;'>
                <li>Critical Thinking and Problem Solving</li>
                <li>Team Collaboration and Communication</li>
                <li>Leadership and Initiative</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

    # Tools and Technologies
    st.markdown("""
        <div style='background-color: #F9F9F9; padding: 20px; margin-bottom: 20px; border-radius: 8px;'>
            <h3 style='color: #FF4500;'>Tools and Technologies</h3>
            <ul style='font-size: 16px; line-height: 1.6;'>
                <li>Version Control (Git, GitHub, GitLab)</li>
                <li>Project Management (Jira, Trello, Asana)</li>
                <li>Data Visualization Tools (Tableau, Power BI)</li>
                <li>DevOps Tools (Docker, Jenkins)</li>
                <li>Monitoring Tools (Nagios, Zabbix)</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

    # Conclusion
    st.markdown("""
        <div style='text-align: center; margin-top: 20px;'>
            <p style='font-size: 16px;'>Explore my diverse skill set and see how I can bring value to your projects.</p>
            <p style='font-size: 16px;'>Feel free to reach out for collaboration or professional opportunities!</p>
        </div>
    """, unsafe_allow_html=True)

# Future Goals Section
elif selected == "Future Goals":
    # Section Title with Animation
    st.markdown("""
        <h1 style="color: #FF4500; text-align: center; font-size: 48px; animation: fadeIn 2s;">
            🚀 Future Goals
        </h1>
        <style>
            @keyframes fadeIn {
                from { opacity: 0; }
                to { opacity: 1; }
            }
        </style>
    """, unsafe_allow_html=True)

    # Short-Term Goals - Card Style with Icons
    st.markdown("""
        <div style="background-color: #FFFAF0; padding: 20px; margin-bottom: 20px; border-radius: 8px; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);">
            <h3 style="color: #FF6347;">🎯 Short-Term Goals</h3>
            <ul style="font-size: 16px; line-height: 1.8;">
                <li><strong>Secure a role:</strong> Specialize in network engineering and software development.</li>
                <li><strong>Certifications:</strong> Earn Cisco CCNA and AWS credentials to advance technical skills.</li>
                <li><strong>Contribute:</strong> Enhance ICT infrastructure projects for improved performance.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

    # Mid-Term Goals - Timeline Style
    st.markdown("""
        <div style="background-color: #F0FFF0; padding: 20px; margin-bottom: 20px; border-radius: 8px; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);">
            <h3 style="color: #228B22;">📈 Mid-Term Goals</h3>
            <div style="margin-left: 10px; border-left: 3px solid #228B22; padding-left: 15px;">
                <p style="font-size: 16px; line-height: 1.8;"><strong>2025-2028:</strong></p>
                <ul style="font-size: 16px; line-height: 1.8;">
                    <li>Transition into technical project management, overseeing complex ICT projects.</li>
                    <li>Master cloud technologies, artificial intelligence, and DevOps practices.</li>
                    <li>Mentor junior team members and foster skill development in the organization.</li>
                </ul>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Long-Term Goals - Progress Indicators
    st.markdown("""
        <div style="background-color: #F0F8FF; padding: 20px; margin-bottom: 20px; border-radius: 8px; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);">
            <h3 style="color: #1E90FF;">🌐 Long-Term Goals</h3>
            <ul style="font-size: 16px; line-height: 1.8;">
                <li><strong>Leadership:</strong> Lead sustainable ICT initiatives driving innovation.</li>
                <li><strong>Global Solutions:</strong> Create digital transformation strategies for developing countries.</li>
                <li><strong>Entrepreneurship:</strong> Establish a tech consultancy focused on cloud and AI solutions.</li>
                <li><strong>Collaboration:</strong> Build partnerships with global tech leaders to elevate ICT practices in Sri Lanka.</li>
            </ul>
            <div style="margin-top: 20px;">
                <p style="text-align: center;">Progress Tracker:</p>
                <div style="background-color: #E0E0E0; border-radius: 15px; height: 20px; width: 100%; position: relative;">
                    <div style="background-color: #1E90FF; height: 100%; width: 40%; border-radius: 15px;"></div>
                </div>
                <p style="font-size: 14px; text-align: center; margin-top: 10px;">40% towards completion</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Final Vision Statement with Call-to-Action
    st.markdown("""
        <div style="background-color: #FFF5EE; padding: 20px; margin-top: 30px; border-radius: 8px; text-align: center; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);">
            <h3 style="color: #FF4500;">My Vision</h3>
            <p style="font-size: 16px; line-height: 1.8;">
                I aspire to leverage the latest advancements in technology to solve real-world problems, foster global collaborations, and
                contribute to the sustainable growth of the ICT sector. My ultimate goal is to create innovative solutions that bridge gaps, enhance lives, and leave a lasting impact on communities worldwide.
            </p>
            <p style="font-size: 16px; line-height: 1.8; margin-top: 20px;">
                If you share a similar vision or are working on exciting projects, let's connect and collaborate! Together, we can shape the future of technology.
            </p>
            <a href="mailto:yasas.gunarathna@example.com" style="display: inline-block; margin-top: 20px; padding: 10px 20px; background-color: #FF4500; color: #FFF; text-decoration: none; border-radius: 5px;">
                Contact Me
            </a>
        </div>
    """, unsafe_allow_html=True)

# Contact Section
elif selected == "Contact":
    st.markdown("<h1 style='color: #FF4500; text-align: center;'>Contact Me</h1>", unsafe_allow_html=True)
    
    # Contact Info with Icons
    st.markdown("""
        <div style='display: flex; flex-direction: column; align-items: center; margin-top: 20px;'>
            <div style='background-color: #F9F9F9; padding: 20px; border-radius: 10px; width: 80%; text-align: center;'>
                <p style='font-size: 18px;'><strong>📞 Phone:</strong> +61 493 620 319</p>
                <p style='font-size: 18px;'><strong>📧 Email:</strong> <a href='mailto:yasas.gunarathna@example.com' style='color: #FF4500;'>yasas.gunarathna@example.com</a></p>
                <p style='font-size: 18px;'><strong>🔗 LinkedIn:</strong> <a href='www.linkedin.com/in/weera-gunarathne-5a9546227' target='_blank' style='color: #FF4500;'>Visit My LinkedIn Profile</a></p>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Contact Form Section
    st.markdown("""
        <div style='margin-top: 40px; background-color: #F1F1F1; padding: 30px; border-radius: 10px;'>
            <h2 style='color: #FF4500; text-align: center;'>Drop Me a Message</h2>
            <form action="mailto:yasas.gunarathna@example.com" method="post" enctype="text/plain" style='margin-top: 20px;'>
                <label for="name" style='font-size: 16px;'>Your Name:</label>
                <input type="text" id="name" name="name" placeholder="Enter your name" style='width: 100%; padding: 10px; margin-top: 10px; border: 1px solid #ccc; border-radius: 5px;'>
                <label for="email" style='font-size: 16px; margin-top: 20px;'>Your Email:</label>
                <input type="email" id="email" name="email" placeholder="Enter your email" style='width: 100%; padding: 10px; margin-top: 10px; border: 1px solid #ccc; border-radius: 5px;'>
                <label for="message" style='font-size: 16px; margin-top: 20px;'>Your Message:</label>
                <textarea id="message" name="message" placeholder="Type your message here" rows="5" style='width: 100%; padding: 10px; margin-top: 10px; border: 1px solid #ccc; border-radius: 5px;'></textarea>
                <button type="submit" style='margin-top: 20px; padding: 10px 20px; background-color: #FF4500; color: #FFF; border: none; border-radius: 5px; cursor: pointer;'>Send Message</button>
            </form>
        </div>
    """, unsafe_allow_html=True)

    # Map Integration
    st.markdown("""
        <div style='margin-top: 40px; text-align: center;'>
            <h3 style='color: #FF4500;'>Find Me Here</h3>
            <iframe 
                src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3539.0082385143156!2d153.02107261506112!3d-27.470125983890197!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6b915a1cf79c4f1d%3A0x502a35af3de4730!2sBrisbane%20QLD%2C%20Australia!5e0!3m2!1sen!2slk!4v1612305588914!5m2!1sen!2slk"
                width="100%" 
                height="300" 
                style="border: 0; border-radius: 10px;" 
                allowfullscreen="" 
                loading="lazy">
            </iframe>

        </div>
    """, unsafe_allow_html=True)

    # Call-to-Action Section
    st.markdown("""
        <div style='margin-top: 40px; text-align: center;'>
            <h2 style='color: #FF4500;'>Let’s Connect</h2>
            <p style='font-size: 16px; line-height: 1.6;'>I’m open to collaboration, exciting projects, or just a friendly conversation. Feel free to reach out through any of the above methods!</p>
            <a href='https://www.linkedin.com/in/yasas-gunarathna-5a9546227/' target='_blank' style='padding: 10px 20px; background-color: #FF4500; color: #FFF; text-decoration: none; border-radius: 5px; display: inline-block;'>Connect on LinkedIn</a>
        </div>
    """, unsafe_allow_html=True)
