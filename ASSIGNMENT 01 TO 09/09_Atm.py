import streamlit as st

# Set page config
st.set_page_config(page_title="ATM Machine", page_icon="🏧")

# Initial balance stored in session (so it doesn't reset on every interaction)
if 'balance' not in st.session_state:
    st.session_state.balance = 1000  # Default balance

# 🎯 Title and tagline
st.title("🏧 ATM Machine Simulator")
st.subheader("💰 Manage your money easily and safely!")

# 🧾 Show current balance
st.info(f"💼 Current Balance: **Rs. {st.session_state.balance}**")

# 👇 Select operation
operation = st.selectbox("What would you like to do?", ["Check Balance", "Deposit Money", "Withdraw Money"])

# 🔁 Perform operations
if operation == "Check Balance":
    st.success(f"📊 Your current balance is: Rs. {st.session_state.balance}")

elif operation == "Deposit Money":
    deposit = st.number_input("Enter amount to deposit 💵", min_value=1)
    if st.button("✅ Deposit"):
        st.session_state.balance += deposit
        st.success(f"🎉 Rs. {deposit} deposited successfully!")
        st.info(f"💼 New Balance: Rs. {st.session_state.balance}")

elif operation == "Withdraw Money":
    withdraw = st.number_input("Enter amount to withdraw 💸", min_value=1)
    if st.button("🏧 Withdraw"):
        if withdraw <= st.session_state.balance:
            st.session_state.balance -= withdraw
            st.success(f"💸 Rs. {withdraw} withdrawn successfully!")
            st.info(f"💼 Remaining Balance: Rs. {st.session_state.balance}")
        else:
            st.error("❌ Insufficient balance!")

# 📌 Footer
st.markdown("---")
st.caption("🔒 This is a simulation. No real transactions are made. | Created by Ali Akbar 💻")
