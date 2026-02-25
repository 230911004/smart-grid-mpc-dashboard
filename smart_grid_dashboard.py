import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="AI Smart Grid Control", layout="wide")

st.title("⚡ AI Smart Grid MPC Dashboard")

st.markdown("### Academic Comparison: Fixed vs MPC Control")

data = {
    "Metric": [
        "Total Curtailment (MW)",
        "Total Reactive Usage (MVAR)",
        "Total Voltage Deviation (p.u.)"
    ],
    "Fixed Control": [0.942569, 3.200000, 0.438261],
    "MPC Control": [0.356719, 4.066985, 0.498796]
}

df = pd.DataFrame(data)

st.dataframe(df)

st.markdown("### Performance Visualization")

fig, ax = plt.subplots()
x = np.arange(len(df["Metric"]))
width = 0.35

ax.bar(x - width/2, df["Fixed Control"], width, label="Fixed")
ax.bar(x + width/2, df["MPC Control"], width, label="MPC")

ax.set_xticks(x)
ax.set_xticklabels(df["Metric"], rotation=45)
ax.legend()

st.pyplot(fig)

st.success("Deployment Successful 🚀")
