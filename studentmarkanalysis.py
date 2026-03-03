import streamlit as st
import pandas as pd

st.set_page_config(page_title="Student Marks Analysis")

st.title("📊 Student Marks Analysis")

file = st.file_uploader("Upload CSV File", type=["csv"])

if file:
    df = pd.read_csv(file)

    st.subheader("Dataset Preview")
    st.dataframe(df)

    st.subheader("Basic Statistics")
    st.write(df.describe())

    subject = st.selectbox("Select Subject Column", df.columns)

    st.subheader("Average Marks")
    avg = df[subject].mean()
    st.success(f"Average {subject} Marks: {avg:.2f}")

    st.subheader("Bar Chart")
    st.bar_chart(df[subject])

else:
    st.info("Please upload a CSV file")