import streamlit as st
from roast_engine import smart_sentiment_roast
from compliment_engine import sweet_sentiment_compliment

# --- Page setup ---
st.set_page_config(page_title="MoodSwing 🤖", page_icon="🌀", layout="centered")
st.title("🌀 MoodSwing: Your Sass or Sweetness Bot")
st.markdown("Roasted or complimented... choose your fate. 😈✨")

# --- Mode Selection ---
mode = st.radio("Choose your mood style:", ["🔥 Roast Me", "🌸 Compliment Me"])

# --- Mood Slider ---
mood = st.slider("Mood Override (😢 → 😐 → 😊)", -1.0, 1.0, 0.0, step=0.1)

# --- Input ---
user_input = st.text_input("Enter your message or thought here:")

# --- Generate Button ---
if st.button("Generate Response 🎭"):
    if mode == "🔥 Roast Me":
        roast = smart_sentiment_roast(user_input, override_sentiment=mood)
        st.markdown(f"### 🔥 Your Roast:\n> {roast}")
        
        # Show roast GIF based on mood
        if mood > 0.3:
            st.image("https://tenor.com/fADCQb97sx7.gif")
        elif mood < -0.1:
            st.image("https://tenor.com/5k9g.gif")
        else:
            st.image("https://tenor.com/bcegt.gif")

    else:
        compliment = sweet_sentiment_compliment(user_input, override_sentiment=mood)
        st.markdown(f"### 🌸 Your Compliment:\n> {compliment}")
        
        # Show compliment GIF based on mood
        if mood > 0.3:
            st.image("https://tenor.com/nxRuCOnIcDp.gif")
        elif mood < -0.1:
            st.image("https://tenor.com/kTGgFKTbMw9.gif")
        else:
            st.image("https://tenor.com/u2FhZENPIzj.gif")

# --- Footer ---
st.markdown("---")
st.caption("Made with 💻, ☕, and a little emotional whiplash.")
