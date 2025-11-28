import streamlit as st
import pandas as pd

st.set_page_config(page_title="RACI Matrix", layout="wide")

st.title("RACI Matrix for Modern Product Practice")

# ---------------------------
# 1. Define the RACI matrix
# ---------------------------
raci_data = [
    ["Define Holistic Product", "A/R", "C", "C", "C", "I"],
    ["Define Product Vision", "A/R", "C", "C", "C", "I/C"],
    ["Continuous Discovery & Delivery Framework", "A/R", "C", "C", "I", "I"],
    ["Run Discovery Experiments", "A", "R", "R", "I", "I"],
    ["Identify User Value", "A/R", "C", "I", "C", "I"],
    ["Ensure Usability", "C", "A/R", "I", "I", "I"],
    ["Assess Feasibility", "C", "C", "A/R", "I", "I"],
    ["Assess Business Viability", "A/R", "I", "I", "C", "C"],
    ["Create Discovery Prototypes", "C", "R", "R", "I", "I"],
    ["Run 10–20 Experiments / Week", "A", "R", "R", "I", "I"],
    ["Validate Backlog", "A/R", "C", "C", "C", "I"],
    ["Define MVP (Prototype)", "A/R", "C", "C", "I", "I"],
    ["Product Delivery (Production Builds)", "C", "C", "A/R", "I", "I"],
    ["Build Production Software", "I", "I", "A/R", "I", "I"],
    ["Ensure Scalability/Security", "I", "I", "A/R", "I", "I"],
    ["Prepare GTM Narrative", "I", "I", "I", "A/R", "C"],
    ["Achieve Product/Market Fit", "A/R", "C", "C", "C", "I"],
    ["Post-PMF Optimisation", "A/R", "C", "R", "C", "I"]
]

columns = [
    "Activity",
    "Product Manager (PM)",
    "Designer (UX)",
    "Engineering (Eng)",
    "Product Marketing (PMM)",
    "Stakeholders (SL)"
]

df = pd.DataFrame(raci_data, columns=columns)

# ---------------------------
# 2. Define color function for responsibilities
# ---------------------------
def color_responsibility(val):
    val_str = str(val)
    if 'R' in val_str:
        return 'background-color: #ff0000; color: white'  # Bold red for Responsible
    elif 'A' in val_str:
        return 'background-color: #0000ff; color: white'  # Bold blue for Accountable
    elif 'C' in val_str:
        return 'background-color: #00ff00; color: white'  # Bold green for Consulted
    elif 'I' in val_str:
        return 'background-color: #ffff00; color: black'  # Bold yellow for Informed
    else:
        return ''

# ---------------------------
# 3. Filtering controls
# ---------------------------
st.subheader("Filters")

roles = columns[1:]  # all role columns
selected_role = st.selectbox("Highlight Responsibilities For:", ["None"] + roles)

# ---------------------------
# 4. Apply styling
# ---------------------------
def style_row(row):
    styles = []
    for col in df.columns:
        if col == "Activity":
            style = ''
        else:
            style = color_responsibility(row[col])
        if selected_role != "None" and row[selected_role]:
            style += '; font-weight: bold'
        styles.append(style)
    return styles

df_highlight = df.style.apply(style_row, axis=1)

# ---------------------------
# 3. Display the table
# ---------------------------
st.subheader("RACI Matrix")

st.dataframe(df_highlight, use_container_width=True)

# ---------------------------
# 4. Download button
# ---------------------------
csv = df.to_csv(index=False)
st.download_button(
    label="Download RACI as CSV",
    data=csv,
    file_name="raci_matrix.csv",
    mime="text/csv"
)
