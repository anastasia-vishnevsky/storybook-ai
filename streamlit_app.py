import streamlit as st
import requests
from pathlib import Path
from src.config import settings

API_URL = settings.API_URL

# Page setup
st.set_page_config(page_title="Storybook AI", page_icon="📚", layout="wide")

# Tabs
tab1, tab2 = st.tabs(["Generate New", "View Archive"])

# --------- Tab 1: Upload and Generate ---------
with tab1:
    st.title("Storybook AI")
    st.write("Upload any picture to generate a magical story and an illustrated cover.")

    uploaded_file = st.file_uploader("Upload a picture", type=["jpg", "jpeg", "png"])

    if uploaded_file:

        if st.button("Generate Story and Cover"):
            with st.spinner("Working some magic..."):
                files = {"file": uploaded_file.getvalue()}
                try:
                    response = requests.post(f"{API_URL}/generate-storybook", files=files)
                    if response.status_code == 200:
                        result = response.json()
                        cover_url = result.get("cover_url")
                        story = result.get("story")

                        # Layout in 3 columns
                        cols = st.columns([2, 2, 4])
                        with cols[0]:
                            st.image(uploaded_file, caption="Uploaded", use_container_width=True)
                        with cols[1]:
                            if cover_url:
                                cover_response = requests.get(cover_url)
                                st.image(cover_response.content, caption="Cover", use_container_width=True)
                        with cols[2]:
                            st.markdown("**Story**")
                            st.write(story if story else "No story returned.")
                    else:
                        st.error(f"Error: {response.status_code} - {response.text}")
                except Exception as e:
                    st.error(f"Request failed: {e}")

# --------- Tab 2: View Archive ---------
with tab2:
    st.header("Saved Storybooks")

    upload_dir = Path("uploads")
    cover_dir = Path("generated/covers")
    story_dir = Path("generated/stories")

    # Collect all filenames based on file_id
    uploaded_images = {f.stem.rsplit("_", 1)[0]: f for f in upload_dir.glob("*_uploaded.*")}
    covers = {f.stem.rsplit("_", 1)[0]: f for f in cover_dir.glob("*_cover.png")}
    stories = {f.stem.rsplit("_", 1)[0]: f for f in story_dir.glob("*_story.txt")}

    # Only display items with matching image + cover + story
    common_ids = sorted(set(uploaded_images) & set(covers) & set(stories), reverse=True)

    if not common_ids:
        st.info("No saved storybooks found.")
    else:
        for file_id in common_ids:
            img_path = uploaded_images[file_id]
            cover_path = covers[file_id]
            story_path = stories[file_id]

            # Show uploaded image, generated cover, and story side by side
            cols = st.columns([2, 2, 4])
            with cols[0]:
                st.image(str(img_path), caption="Uploaded", use_container_width=True)
            with cols[1]:
                st.image(str(cover_path), caption="Cover", use_container_width=True)
            with cols[2]:
                with open(story_path, encoding="utf-8") as f:
                    st.markdown("**Story**")
                    st.write(f.read().strip())

            st.divider()