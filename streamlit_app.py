import streamlit as st
import requests
import os

API_URL = os.getenv("API_URL", "http://localhost:8000")

# If in Docker, replace localhost with the container name
if os.getenv("IN_DOCKER") == "1":
    API_URL = API_URL.replace("localhost", "storybook-api")

# Set page title and icon
st.set_page_config(page_title="Storybook AI", page_icon="📚")

# Title and description
st.title("📖 Storybook AI")
st.write("Upload any picture to get a magical story and a beautiful cover!")

# File upload widget
uploaded_file = st.file_uploader("Upload a picture", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # Display uploaded image
    st.image(uploaded_file, caption="Your picture", use_container_width=True)

    # Button to generate story and cover
    if st.button("✨ Generate Story and Cover"):
        with st.spinner("Generating story and cover..."):
            files = {'file': uploaded_file.getvalue()}
            try:
                # Send POST request to FastAPI endpoint
                response = requests.post(f"{API_URL}/generate-storybook", files=files)

                if response.status_code == 200:
                    result = response.json()

                    # Display the generated story
                    st.subheader("📖 Your Story")
                    st.write(result.get("story", "No story received."))

                    # Display the generated cover image
                    st.subheader("🎨 Generated Cover")
                    cover_url = result.get("cover_url")
                    if cover_url:
                        cover_response = requests.get(cover_url)
                        st.image(cover_response.content, caption="Cover", use_container_width=True)
                    else:
                        st.warning("No cover image returned.")
                else:
                    st.error(f"Error: {response.status_code} - {response.text}")
            except Exception as e:
                st.error(f"Request failed: {e}")