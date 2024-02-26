import os
import subprocess

import streamlit as st

from setting import FILES_DIR


def main():
    st.title("Select an excel file and press Open button")

    # Input Excel file using file uploader
    excel_file = st.file_uploader("Upload an Excel file (XLSX)", type=["xlsx"])
    if st.button("Open", type="primary") and excel_file:
        try:
            filename2 = os.path.join(FILES_DIR, excel_file.name)
            with open(filename2, "wb") as temp_excel_file:
                temp_excel_file.write(excel_file.read())
            # Execute the Python script with the Excel file as an argument
            args = ["python", "main.py", excel_file.name]
            result = subprocess.run(args, capture_output=True, text=True)
            st.write("Execution output:")
            st.code(result.stdout, language="python")
        except Exception as e:
            st.error(f"Error executing the script: {e}")
    else:
        st.write("Select an xlsx file")


if __name__ == "__main__":
    main()
