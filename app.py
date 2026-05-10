import pandas as pd
import streamlit as st

# Keywords to filter announcements
KEYWORDS = [
    "board meeting intimation",
    "split",
    "bonus",
    "buyback",
    "general updates",
    "record date for",
    "bagging"
]

st.set_page_config(page_title="Corporate Announcements", layout="wide")

if st.sidebar.button("Exit"):
    st.stop()

st.title("Filtered Corporate Announcements")

# --- File uploader ---
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file is not None:
    # Read uploaded CSV
    df = pd.read_csv(uploaded_file)

    # Apply keyword filter
    mask = df.apply(
        lambda row: row.astype(str).str.lower().str.contains('|'.join(KEYWORDS)).any(),
        axis=1
    )
    filtered_df = df[mask]

    # Get unique subjects
    subjects = filtered_df['SUBJECT'].dropna().unique()

    # Display tables grouped by subject
    for subject in subjects:
        st.subheader(subject)
        sub_df = filtered_df[filtered_df['SUBJECT'] == subject]
        # Wrap text in DETAILS column
        sub_df['DETAILS'] = sub_df['DETAILS'].astype(str).apply(lambda x: x.replace(". ", ".\n"))
        st.table(sub_df)

else:
    st.info("Please upload a CSV file to continue.")
