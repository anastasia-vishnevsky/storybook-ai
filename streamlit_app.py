import streamlit as st
import requests
from pathlib import Path
from src.config import settings

# Config
API_URL = settings.API_URL

# Page setup
st.set_page_config(page_title="Storybook AI", page_icon="📚", layout="wide")

# Tabs
tab1, tab2 = st.tabs(["Upload Image", "Saved Content"])

# --- Tab 1: Upload and Generate ---
with tab1:
    st.title("Storybook AI")
    st.write("Upload any picture to get a magical story and a beautiful cover.")

    uploaded_file = st.file_uploader("Upload a picture", type=["jpg", "jpeg", "png"])

    if uploaded_file:
        st.image(uploaded_file, caption="Your picture", width=500)

        if st.button("Generate Story and Cover"):
            with st.spinner("Generating..."):
                files = {'file': uploaded_file.getvalue()}
                try:
                    response = requests.post(f"{API_URL}/generate-storybook", files=files)

                    if response.status_code == 200:
                        result = response.json()

                        st.subheader("Your Story")
                        st.write(result.get("story", "No story received."))

                        st.subheader("Generated Cover")
                        cover_url = result.get("cover_url")
                        if cover_url:
                            cover_response = requests.get(cover_url)
                            st.image(cover_response.content, caption="Cover", width=500)
                        else:
                            st.warning("No cover image returned.")
                    else:
                        st.error(f"Error: {response.status_code} - {response.text}")
                except Exception as e:
                    st.error(f"Request failed: {e}")

# --- Tab 2: View Saved Content ---
with tab2:
    st.header("Saved Content")

    # Covers
    st.subheader("Generated Covers")
    cover_dir = Path("generated/covers")
    cover_files = sorted(cover_dir.glob("*.png"), reverse=True)

    if cover_files:
        cols = st.columns(5)
        for i, cover in enumerate(cover_files[:15]):
            with cols[i % 5]:
                st.image(str(cover), caption=cover.name, use_container_width=True)
    else:
        st.info("No covers found.")

    st.divider()

    # Stories
    st.subheader("Generated Stories")
    story_dir = Path("generated/stories")
    story_files = sorted(story_dir.glob("*.txt"), reverse=True)

    if story_files:
        for story in story_files[:10]:
            st.markdown(f"**{story.name}**")
            with open(story, encoding="utf-8") as f:
                st.markdown(f"> {f.read().strip()}")
            st.markdown("---")
    else:
        st.info("No stories found.")