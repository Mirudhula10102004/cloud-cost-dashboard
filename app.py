import streamlit as st
import matplotlib.pyplot as plt

# ------------------------
# TITLE
# ------------------------
st.title("📊 Cloud Cost Optimization Dashboard")

# ------------------------
# FAKE DATA
# ------------------------
st.header("💰 Monthly Cloud Cost Summary")

total_cost = 4500  # You can change this value
st.metric("Total Cloud Spend (INR)", f"₹{total_cost}")

# ------------------------
# COST BY SERVICES (FAKE DATA)
# ------------------------
st.header("🧾 Cost by Service")

services = ["Compute", "Storage", "Database", "Networking", "Monitoring"]
costs = [1500, 800, 1000, 700, 500]

fig, ax = plt.subplots()
ax.pie(costs, labels=services, autopct="%1.1f%%", startangle=90)
ax.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

st.pyplot(fig)

# ------------------------
# COST OPTIMIZATION TIPS
# ------------------------
st.header("💡 Cost Optimization Tips")
st.info("1. Use auto-scaling to avoid paying for unused servers.")
st.info("2. Delete unused storage and snapshots.")
st.info("3. Use serverless functions for event-driven workloads.")
st.info("4. Monitor usage weekly to prevent sudden cost spikes.")
