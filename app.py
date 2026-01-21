import streamlit as st
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI()

# Title and description
st.title("🤖 Satvik-GPT")
st.markdown("🚀 Generate LinkedIn posts on Generative AI like [Satvik Paramkusham](https://www.linkedin.com/in/satvik-paramkusham/)") 
st.markdown("❤️ Powered by GPT-4o fine-tuned model.")

# Text input for topic
topic = st.text_input("Please enter the topic")

st.code("""
            Try:
            Explain Transformers Architecture
            How does RAG work?
            """, language=None)

# Model names
BASE_MODEL = "gpt-4o-2024-08-06"
FINETUNED_MODEL = "ft:gpt-4o-2024-08-06:personal::AKSobHDd"

def generate_post(prompt, model):
    """Generate a response using OpenAI SDK"""
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def generate_linkedin_posts(topic):
    """Generate posts from both models"""
    prompt = f"Generate a LinkedIn post about {topic}"
    base_response = generate_post(prompt, BASE_MODEL)
    ft_response = generate_post(prompt, FINETUNED_MODEL)
    return base_response, ft_response

if st.button("Generate Posts"):
    if topic:
        with st.spinner("Generating posts..."):
            base_response, ft_response = generate_linkedin_posts(topic)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Base Model (gpt-4o) 🔗")
            st.markdown(f'<div class="output-text">{base_response}</div>', unsafe_allow_html=True)
        
        with col2:
            st.subheader("Satvik-GPT (Fine-tuned Model)")
            st.markdown(f'<div class="output-text">{ft_response}</div>', unsafe_allow_html=True)
    else:
        st.warning("Please enter a topic before generating posts.")
