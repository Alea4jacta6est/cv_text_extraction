"""The main part of Streamlit UI is rendered here"""
import os

import streamlit as st
import seaborn as sns

from handlers.pipeline_runner import run_pipeline


image_root_path = 'data/inputs/'
cm = sns.light_palette("green", as_cmap=True)

def main():
    st.set_page_config(page_title="Information extraction from images", layout='wide', initial_sidebar_state='auto')
    st.title("Information extraction from images")
    user_input = st.sidebar.selectbox("Choose a picture", os.listdir(image_root_path))
    path_to_image = f"{image_root_path}{user_input}"
    df, extracted_text = run_pipeline(path_to_image)
    st.subheader("Source image:")
    st.image(path_to_image)
    st.subheader("Results of parsing:")
    st.dataframe(df)
    st.subheader("Results of text extraction with pytesseract:")
    st.text(extracted_text)

   
if __name__ == "__main__":
    main()