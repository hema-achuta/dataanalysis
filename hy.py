import streamlit as st
import subprocess

def main():
    st.set_page_config(page_title="Data Analysis App")

    st.title('Data Plotting & Analysis Software')

    if st.button('Run Data Analysis App'):
        subprocess.Popen(["streamlit", "run", "nstl.py"])

if __name__ == '__main__':
    main()
