# Storybook AI API

This is a FastAPI service that creates funny children's stories and illustrated covers based on uploaded photos, using:
- **BLIP (Bootstrapped Language Image Pretraining)** — a vision-language model from hosted on [Hugging Face](https://huggingface.co/Salesforce/blip-image-captioning-base). It automatically generates a natural-language caption from an image, which is then used as the creative seed for the story and illustration.
- **GPT-4o-mini** via OpenAI for generating the story
- **DALL·E 3** via OpenAI for generating a cartoon-style storybook cover

Built with **FastAPI** and **Streamlit**.

---

##  Features

- Upload any picture
- Get an AI-generated children's story
- Receive a matching storybook-style cover image
- Simple web UI powered by Streamlit
- Saves:
  - uploaded images (`uploads/`)
  - generated stories (`generated/stories/`)
  - generated covers (`generated/covers/`)

---

##  Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/) — API backend  
- [Streamlit](https://streamlit.io/) — frontend  
- [OpenAI API](https://platform.openai.com/) — for text and image generation
- [Hugging Face Transformers](https://huggingface.co/docs/transformers/index) — for image captioning
---

##  Project Structure

- `uploads/` — uploaded user images  
- `generated/` — AI-generated output  
  - `covers/` — saved DALL·E cover images  
  - `stories/` — saved GPT-generated stories  
- `logs/` — stores application logs  
  - `app.log` — main log file
- `src/` — main source code  
  - `app.py` — FastAPI app  
  - `config.py` — environment config loader  
  - `prompts.py` — centralized prompt templates  
  - `schemas.py` — response models  
  - `services/` — generation logic  
    - `story_generator.py` — GPT-based story generation  
    - `cover_generator.py` — DALL·E image generation  
  - `utils/` — helper functions  
    - `file_utils.py` — save uploads  
    - `image_captioner.py` — caption image using BLIP  
    - `logger.py` — logger config  
- `.env` — environment variables  
- `.env.example` — example environment file for setup  
- `requirements.txt` — Python dependencies  
- `run.py` — entrypoint to run app locally  
- `Dockerfile` — builds a container image for the app  
- `docker-compose.yml` — defines and runs the container app  
- `.gitignore` — excluded files  
- `streamlit_app.py` — simple Streamlit-based web UI
- `README.md` — you’re reading it!

---

##  Installation

1. Clone the repository:

```bash
git clone https://github.com/anastasia-vishnevsky/storybook-ai.git
cd storybook-ai
```
2. Create and activate a virtual environment:

- On **macOS/Linux**:

```bash  
python3 -m venv .venv
source .venv/bin/activate
``` 

- On **Windows**:

```bash 
python -m venv .venv
.venv\Scripts\activate
```

3. Install dependencies:

```bash 
pip install -r requirements.txt
```

4. Set up environment variables:

Copy .env.example to .env and add your OpenAI key and model names:

- OPENAI_API_KEY=your-openai-key
- API_URL=http://localhost:8000
- HOST=0.0.0.0
- PORT=8000
- BLIP_MODEL=Salesforce/blip-image-captioning-base
- GPT_MODEL=gpt-4o-mini
- DALLE_MODEL=dall-e-3

---

##  How It Works: Two Independent Processes

This project consists of **two separate processes**, each running independently:

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Backend** | FastAPI | Generates stories and cover images based on uploaded images |
| **Frontend** | Streamlit | Provides a simple browser-based interface to interact with the backend |

They communicate via HTTP. The frontend sends image uploads to the backend and receives generated content in response.

> Make sure the FastAPI server is running **before** launching the Streamlit UI.

---


## Running the App

### Locally

Run the app using:

```bash 
python run.py
``` 
Open in browser:
- Swagger UI: http://127.0.0.1:8000/docs

### Docker

To run the app in Docker, use:

```bash
docker compose up --build
``` 
Open in browser:    
- Swagger UI: http://localhost:8000/docs

---

## Generating a Storybook

In http://127.0.0.1:8000/docs, find:
- POST /generate-storybook
- Click “Try it out”
- Upload an image
- Hit Execute

You’ll get back:
- A caption of the image (BLIP)
- A funny story (GPT-4o-mini)
- A cartoon cover image URL (DALL·E 3)

---

## Streamlit Frontend 

You can also run a simple web UI using Streamlit.
It allows you to upload a picture and instantly get a story and a cover right in your browser.

### Run Streamlit

- Make sure FastAPI is already running on http://localhost:8000.
- Then, in a new terminal:
```bash
streamlit run streamlit_app.py
```
- Open your browser at http://localhost:8501 to use the web interface

**What You’ll See:**

- Two tabs:
  - Generate new – for uploading a picture and generating story + cover
  - View Archive – to browse previously generated stories and covers


## Saved Outputs

- Uploaded files are stored in uploads/
- Generated cover images are saved in generated/covers/
- Generated stories are saved as .txt files in generated/stories/

> Streamlit UI also includes a section to view previously generated covers and stories.