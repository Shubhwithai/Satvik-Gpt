# 🤖 Satvik-GPT

Generate LinkedIn posts on Generative AI using a fine-tuned GPT-4o model.

## Features

- Compare **Base GPT-4o** vs **Fine-tuned Model** side by side
- Generate professional LinkedIn posts on any AI topic
- Simple and clean UI with Streamlit

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Set API Key

```bash
export OPENAI_API_KEY="your-api-key-here"
```

Or create `.streamlit/secrets.toml`:

```toml
OPENAI_API_KEY = "your-api-key-here"
```

### 3. Run the App

```bash
streamlit run app.py
```

## Usage

1. Enter a topic (e.g., "Transformers Architecture", "RAG", "Prompt Engineering")
2. Click **Generate Posts**
3. Compare the outputs from both models

## Tech Stack

- **Streamlit** - Web UI
- **OpenAI SDK** - Direct API calls (no LangChain)
- **GPT-4o** - Base model
- **Fine-tuned GPT-4o** - Custom trained model

## Screenshot

| Base Model | Fine-tuned Model |
|------------|------------------|
| Generic LinkedIn post | Customized style post |

---

Made with ❤️ using OpenAI SDK
