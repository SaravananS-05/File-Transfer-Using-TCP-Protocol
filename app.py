import streamlit as st
import subprocess
import os

# Set the title of the app
st.title("File Transfer Application")

# Input fields for server IP and filename
server_ip = st.text_input("Enter Server IP Address:")
filename = st.text_input("Enter File Name to Download:")

# Button to initiate download
if st.button("Download File"):
    if server_ip and filename:
        # Run the client script with server IP and filename as arguments
        result = subprocess.run(
            ['python', 'client.py', server_ip, filename],  # Adjust command as needed
            capture_output=True, text=True
        )
        if result.returncode == 0:
            st.success(f"File '{filename}' downloaded successfully!")
        else:
            st.error("Error: File not found or download failed.")
            st.text(result.stderr)
    else:
        st.warning("Please enter both server IP and filename.")

# Footer
st.write("Powered by Streamlit")
