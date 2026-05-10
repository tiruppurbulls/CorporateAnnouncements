import pandas as pd
import streamlit as st

FILE_PATH = "C:/Users/tirup/Downloads/CF-AN-equities-07-05-2026-to-10-05-2026.csv"
KEYWORDS = [
    "board meeting intimation",
    "split",
    "bonus",
    "buyback",
    "general updates",
    "record date for",
    "bagging"
]

df = pd.read_csv(FILE_PATH)

mask = df.apply(
    lambda row: row.astype(str).str.lower().str.contains('|'.join(KEYWORDS)).any(),
    axis=1
)
filtered_df = df[mask]

subjects = filtered_df['SUBJECT'].dropna().unique()

st.set_page_config(page_title="Corporate Announcements", layout="wide")

if st.sidebar.button("Exit"):
    st.stop()

st.title("Filtered Corporate Announcements")

# --- Wrap text in DETAILS column ---
# Use st.table instead of st.dataframe for wrapping
for subject in subjects:
    st.subheader(subject)
    sub_df = filtered_df[filtered_df['SUBJECT'] == subject]
    # Convert DETAILS column to wrapped text
    sub_df['DETAILS'] = sub_df['DETAILS'].astype(str).apply(lambda x: x.replace(". ", ".\n"))
    st.table(sub_df)
