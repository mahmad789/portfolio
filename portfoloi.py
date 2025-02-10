import streamlit as st
import base64
from pathlib import Path

def get_image_base64(image_path):
    # Convert local image to base64
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# CSS for Animation
st.markdown("""
    <style>
    @keyframes fadeInOut {
        0% { opacity: 0; transform: scale(0.8); }
        50% { opacity: 1; transform: scale(1); }
        100% { opacity: 0.8; }
    }

    .profile-header {
        animation: fadeInOut 1.9s ease-in-out;
        text-align: center;
        background: linear-gradient(to right, #4EA1D3, #3E5C76);
        color: white;
        padding: 40px;
        border-radius: 20px;
        box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.2);
    }

    .profile-img {
        width: 120px;
        height: 120px;
        border-radius: 50%;
        border: 4px solid white;
        object-fit: cover;
        margin-bottom: 10px;
    }

    .profile-name {
        font-size: 26px;
        font-weight: bold;
    }

    .profile-heading {
        font-size: 18px;
        font-style: italic;
    }
    </style>
""", unsafe_allow_html=True)

# Profile Details
image_path = "ahmad.jpeg"  # Make sure this file exists in the same directory as your script
name = "Muhammad Ahmad"
heading = "Python Developer | Data Analyst"

# Convert image to base64
try:
    img_base64 = get_image_base64(image_path)
    
    # HTML for Profile Header
    profile_html = f"""
        <div class="profile-header">
            <img src="data:image/jpeg;base64,{img_base64}" class="profile-img">
            <div class="profile-name">{name}</div>
            <div class="profile-heading">{heading}</div>
        </div>
    """
except FileNotFoundError:
    st.error(f"Image file '{image_path}' not found. Make sure it exists in the same directory as your script.")
    profile_html = f"""
        <div class="profile-header">
            <div class="profile-name">{name}</div>
            <div class="profile-heading">{heading}</div>
        </div>
    """

# Render Profile Header
st.markdown(profile_html, unsafe_allow_html=True)

import streamlit as st
import streamlit as st

# # Custom HTML for a more beautiful and vertical skills div
# st.markdown("""
# <div style="background-color:#FF9D23; padding:40px; border-radius:30px; box-shadow:0px 4px 8px rgba(0, 0, 0, 0.1); width: 45%; margin-right:30px;margin-top: 10px;">
#     <h2 style="text-align:center; font-size:30px; color:#FEF9E1;">Skills</h2>
#     <ul style="list-style-type:none; padding:0;">
#         <li style="font-size:22px; padding:15px; color:#FEF9E1; border-bottom:1px solid #ddd; font-weight:bold;">Pandas</li>
#         <li style="font-size:22px; padding:15px; color:#FEF9E1; border-bottom:1px solid #ddd; font-weight:bold;">Numpy</li>
#         <li style="font-size:22px; padding:15px; color:#FEF9E1; border-bottom:1px solid #ddd; font-weight:bold;">Matplotlib</li>
#         <li style="font-size:22px; padding:15px; color:#FEF9E1; border-bottom:1px solid #ddd; font-weight:bold;">Scikit-learn</li>
#     </ul>
# </div>
# """, unsafe_allow_html=True)

# st.markdown("""
# <div style="background-color:#e3f2fd; padding:30px; border-radius:30px; box-shadow:0px 4px 8px rgba(0, 0, 0, 0.1); width: 50%; margin-bottom:400px; margin-left: 100px;">
#     <h2 style="text-align:left; font-size:30px; color:#007F73;">About Me</h2>
#     <p style="font-size:18px; color:#333;">
#         We are a team of passionate data scientists and engineers committed to providing innovative solutions using data science and machine learning. 
#         Our goal is to empower businesses and individuals with powerful data-driven insights and tools.
#     </p>
# </div>
# """, unsafe_allow_html=True)


col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div style="background-color:#FF9D23; padding:40px; border-radius:30px; box-shadow:0px 4px 8px rgba(0, 0, 0, 0.1); width:100%; margin-top:10px;">
        <h2 style="text-align:center; font-size:30px; color:#FEF9E1;">Skills</h2>
        <ul style="list-style-type:none; padding:0;">
            <li style="font-size:22px; padding:15px; color:#FEF9E1; border-bottom:1px solid #ddd; font-weight:bold;">Pandas</li>
            <li style="font-size:22px; padding:15px; color:#FEF9E1; border-bottom:1px solid #ddd; font-weight:bold;">Numpy</li>
            <li style="font-size:22px; padding:15px; color:#FEF9E1; border-bottom:1px solid #ddd; font-weight:bold;">Matplotlib</li>
            <li style="font-size:22px; padding:15px; color:#FEF9E1; border-bottom:1px solid #ddd; font-weight:bold;">Scikit-learn</li>
            <li style="font-size:22px; padding:15px; color:#FEF9E1; border-bottom:1px solid #ddd; font-weight:bold;">Power-BI</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="background-color:#E52020; padding:30px; border-radius:30px; box-shadow:0px 4px 8px rgba(0, 0, 0, 0.1); width:100%;margin-top:10px;">
        <h2 style="text-align:left; font-size:30px; color:#FEF9E1;">About Me</h2>
        <p style="font-size:18px; color:#FEF9E1;">
                Experienced Python Developer and Data Analyst with a passion for creating efficient solutions 
                and deriving meaningful insights from data. Specializing in automation, data analysis, 
                and custom software development.
        </p>
    </div>
    """, unsafe_allow_html=True)




col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div style="background-color:#4B164C; padding:40px; border-radius:30px; box-shadow:0px 4px 8px rgba(0, 0, 0, 0.1); width:150%; margin-top:10px;">
        <h3 style="color:#FEF9E1; margin-top:30px;">Services Offered</h3>
            <ul style="color:#FEF9E1; font-size:18px; line-height:1.6;">
                <li>Custom Python Script Development</li>
                <li>Data Analysis and Visualization</li>
                <li>Process Automation Solutions</li>
                <li>Web Scraping & Data Collection</li>
            </ul>
    </div>
    """, unsafe_allow_html=True)



import streamlit as st
import streamlit as st

import streamlit as st

# CSS for the animated div and button
st.markdown("""
    <style>
        .project-container {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 30px;
            padding: 20px;
            justify-items: center;
            transition: all 0.3s ease-in-out;
        }
        .project-card {
            background: #578FCA;
            border-radius: 15px;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
            padding: 20px;
            text-align: center;
            transition: transform 0.4s ease-in-out, box-shadow 0.4s ease-in-out;
            width: 800px;
            height: 280px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }
        .project-card:hover {
            transform: translateY(10px);
            box-shadow: 0 15px 30px rgba(0, 0, 0, 0.2);
        }
        .project-title {
            font-size: 24px;
            font-weight: bold;
            color: #FEF9E1;
            margin-bottom: 15px;
        }
        .project-description {
            font-size: 16px;
            color: #FEF9E1;
            flex-grow: 1;
            margin-bottom: 20px;
        }
        .project-button {
            padding: 12px 20px;
            background-color: #3674B5;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
            text-align: center;
            text-decoration: none;
            transition: background-color 0.3s ease;
        }
        .project-button:hover {
            background-color: #A1E3F9;
            color:black;
        }
    </style>
""", unsafe_allow_html=True)

# Project data with description and link
projects = [
    {"name": "Exploratory Data Analysis", "description": "This project performs an in-depth exploratory data analysis (EDA) on the Datasets, aiming to uncover underlying patterns, relationships, and insights. Using statistical methods and visualizations, it explores data distributions, correlations, outliers, and missing values to help guide further analysis or modeling. The goal is to prepare the data for more advanced techniques by providing a clear understanding of its structure and key features.. It does amazing things!", "url": "https://data-analysts-ux5uzwldu7nzl9rsvnl8si.streamlit.app/"},
    
]

st.markdown('<div class="project-container">', unsafe_allow_html=True)

for project in projects:
    st.markdown(f"""
        <div class="project-card">
            <div class="project-title">{project["name"]}</div>
            <div class="project-description">{project["description"]}</div>
            <a href="{project["url"]}" target="_blank">
                <button class="project-button">Visit Project</button>
            </a>
        </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)








# import streamlit as st

# # Footer content with animations and stylish design
# footer = """
#     <style>
#         .footer {
#             background-color: #A27B5C;
#             color: white;
#             padding: 20px 0;
#             wwidth:150px;
#             text-align: center;
#             font-size: 16px;
#             box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
#             border-radius: 10px;
#             margin-top: 50px;
#             transition: background-color 0.3s ease-in-out;
#         }
#         .footer:hover {
#             background-color: #005f52;
#         }
#         .footer a {
#             color: #F8C8C6;
#             text-decoration: none;
#             margin: 0 15px;
#             font-weight: bold;
#             font-size: 18px;
#             position: relative;
#             transition: color 0.3s ease;
#         }
#         .footer a::after {
#             content: '';
#             position: absolute;
#             bottom: -5px;
#             left: 0;
#             width: 100%;
#             height: 3px;
#             background-color: #F8C8C6;
#             transform: scaleX(0);
#             transform-origin: bottom right;
#             transition: transform 0.25s ease-out;
#         }
#         .footer a:hover::after {
#             transform: scaleX(1);
#             transform-origin: bottom left;
#         }
#         .footer a:hover {
#             color: #98E4FF;
#         }
#     </style>

#     <div class="footer">
#         <p>Contact me: <a href="mailto:your.email@example.com">your.email@example.com</a></p>
#         <p>
#             Connect with me on:
#             <a href="https://www.linkedin.com/in/yourprofile" target="_blank">LinkedIn</a> |
#             <a href="https://github.com/yourusername" target="_blank">GitHub</a> |
#             <a href="https://www.upwork.com/freelancers/~yourprofile" target="_blank">Upwork</a>
#         </p>
#     </div>
# """

# # Add footer to the Streamlit app
# st.markdown(footer, unsafe_allow_html=True)



import streamlit as st

# Footer content with animations, stylish design, and center alignment
footer = """
    <style>
        .footer {
            background-color: #A27B5C;
            color: white;
            padding: 20px 0;
            text-align: center;
            font-size: 16px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            border-radius: 10px;
            margin-top: 100px;
            transition: background-color 0.3s ease-in-out;
            position: relative;
            bottom: 0;
            left: 55%;
            transform: translateX(-50%);
            width: 100%;
        }
        .footer:hover {
            background-color: #3C3D37;
            color:white;
        }
        .footer a {
            color: #F8C8C6;
            text-decoration: none;
            margin: 0 15px;
            font-weight: bold;
            font-size: 18px;
            position: relative;
            transition: color 0.3s ease;
        }
        .footer a::after {
            content: '';
            position: absolute;
            bottom: -5px;
            left: 0;
            width: 100%;
            height: 3px;
            background-color: #F8C8C6;
            transform: scaleX(0);
            transform-origin: bottom right;
            transition: transform 0.25s ease-out;
        }
        .footer a:hover::after {
            transform: scaleX(1);
            transform-origin: bottom left;
        }
        .footer a:hover {
            color: #98E4FF;
        }
    </style>

    <div class="footer">
        <p>Contact me: <a href="mailto:your.email@example.com">ahmadmubashir9009@gmail.com</a></p>
        <p>
            Connect with me on:
            <a href="https://www.linkedin.com/in/m-ahmad123" target="_blank">LinkedIn</a> |
            <a href="https://github.com/mahmad789" target="_blank">GitHub</a>
        </p>
    </div>
"""

# Add footer to the Streamlit app
st.markdown(footer, unsafe_allow_html=True)
