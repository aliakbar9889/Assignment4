import streamlit as st

# 🎯 Page Title and Tagline
st.set_page_config(page_title="BMI Calculator", page_icon="🧮")
st.title("🧮 Body Mass Index (BMI) Calculator")
st.subheader("💪 Stay healthy, stay fit!")
st.markdown("Use this simple calculator to check your **BMI** and understand your body status.")

# 📥 User Input Section
st.header("📌 Enter Your Details:")
height = st.number_input("📏 Height (in cm):", min_value=50, max_value=300)
weight = st.number_input("⚖️ Weight (in kg):", min_value=10, max_value=300)

# 🧠 Calculate BMI
if st.button("🚀 Calculate BMI"):
    if height > 0 and weight > 0:
        height_m = height / 100  # Convert height to meters
        bmi = weight / (height_m ** 2)

        st.success(f"📊 Your BMI is: **{bmi:.2f}**")

        # 😎 Feedback with Emojis
        if bmi < 18.5:
            st.warning("😟 You are **Underweight**. Consider a healthy diet.")
        elif 18.5 <= bmi < 24.9:
            st.info("✅ You have **Normal weight**. Great job!")
        elif 25 <= bmi < 29.9:
            st.warning("😐 You are **Overweight**. Consider exercising.")
        else:
            st.error("🚨 You are **Obese**. Take care and consult a doctor.")

        # 📊 BMI Category Chart
        st.header("📚 BMI Categories:")
        st.markdown("""
        | BMI Range       | Category       |
        |------------------|----------------|
        | Less than 18.5   | Underweight 😟 |
        | 18.5 – 24.9      | Normal 😊      |
        | 25 – 29.9        | Overweight 😐  |
        | 30 and above     | Obese 🚨       |
        """)
    else:
        st.error("❗ Please enter valid height and weight.")

# ✨ Footer
st.markdown("---")
st.caption("📅 Developed by Ali Akbar | Made with ❤️ using Streamlit")
