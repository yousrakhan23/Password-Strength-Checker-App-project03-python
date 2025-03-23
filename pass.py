
import streamlit as st
import re

# Set page config
st.set_page_config(page_title="Password Strength Checker", page_icon="🔒")

# Custom CSS for better UI
st.markdown("""
    <style>
    .stProgress > div > div > div > div {
        background-color: #4CAF50;
    }
    .st-b7 {
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# Title and description
st.title("🔐 Password Strength Checker")
st.markdown("""
    ## WELCOME TO THE ULTIMATE PASSWORD STRENGTH CHECKER 💛
    Use this simple tool to check the strength of your password and get suggestions on how to make it stronger.
    We will give you helpful tips to create a **strong password**.
    """)

# Password input with a placeholder and show password option
password = st.text_input("Enter your password here", type="password", placeholder="Type your password...")
show_password = st.checkbox("Show Password")

if show_password:
    st.text_input("", value=password, disabled=True)

# Function to calculate password strength
def calculate_password_strength(password):
    feedback = []
    score = 0

    # Check password length
    if len(password) >= 8:
        score += 1
        feedback.append("✅ Password is at least 8 characters long.")
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # Check for lowercase and uppercase letters
    if re.search(r"[A-Z]", password) and re.search(r'[a-z]', password):
        score += 1
        feedback.append("✅ Password contains both lowercase and uppercase letters.")
    else:
        feedback.append("❌ Password should contain both lowercase and uppercase letters.")

    # Check for digits
    if re.search(r"\d", password):
        score += 1
        feedback.append("✅ Password contains at least one digit.")
    else:
        feedback.append("❌ Password should contain at least one digit.")

    # Check for special characters
    if re.search(r"[!@#$%^&*()]", password):
        score += 1
        feedback.append("✅ Password contains special characters.")
    else:
        feedback.append("❌ Password should contain special characters (!@#$%^&*()).")

    # Determine overall strength
    if score == 4:
        strength = "Strong"
        color = "green"
    elif score == 3:
        strength = "Medium"
        color = "orange"
    elif score == 2:
        strength = "Weak"
        color = "red"
    else:
        strength = "Very Weak"
        color = "darkred"

    return score, strength, color, feedback

# Check password strength when input is provided
if password:
    score, strength, color, feedback = calculate_password_strength(password)

    # Display password strength progress bar
    st.markdown(f"### Password Strength: **<span style='color:{color};'>{strength}</span>**", unsafe_allow_html=True)
    st.progress(score / 4)

    # Display feedback
    st.markdown("### Improvement Suggestions for Your Password")
    for tip in feedback:
        if "✅" in tip:
            st.success(tip)
        elif "❌" in tip:
            st.error(tip)
        else:
            st.info(tip)

else:
    st.info("Please enter your password to get started 💛")