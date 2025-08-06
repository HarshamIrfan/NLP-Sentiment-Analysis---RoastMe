import streamlit as st
from roast_engine import smart_sentiment_roast
from compliment_engine import sweet_sentiment_compliment
import time

# --- Page Setup ---
st.set_page_config(page_title="MoodSwing 🤖", page_icon="🌀", layout="centered")

# --- Session State for History ---
if "history" not in st.session_state:
    st.session_state.history = []

# --- Theme Toggle ---
theme = st.sidebar.selectbox("🌓 Theme", ["🌚 Dark", "🌞 Light"])

if theme == "🌞 Light":
    bg_color = "linear-gradient(135deg, #fef6e4, #fce1e4, #f7cdef, #eebbee, #dcb4eb)"
    container_color = "rgba(255, 255, 255, 0.95)"
    text_color = "#1e1e1e"
    button_color = "#f7cdef"
else:
    bg_color = "linear-gradient(135deg, #1e1e2f, #2c2b3c)"
    container_color = "rgba(34, 34, 34, 0.95)"
    text_color = "#E6E6E6"
    button_color = "#3a3a5c"

# --- Custom Styling ---
st.markdown(
    f"""
    <style>
    .stApp {{
        background: {bg_color};
        background-attachment: fixed;
        background-size: cover;
        color: {text_color};
    }}
    .block-container {{
        background-color: {container_color};
        padding: 3rem 2rem 3rem 2rem;
        border-radius: 12px;
        box-shadow: 0px 4px 20px rgba(0,0,0,0.2);
        margin-top: 3rem;
    }}
    .title-text {{
        font-size: 2.7rem;
        font-weight: 800;
        text-align: center;
        color: #CDB4DB;
        font-family: 'Segoe UI', sans-serif;
        padding-bottom: 1rem;
    }}
    h3, h4, h5 {{
        color: {text_color};
    }}
    .stButton > button {{
        background-color: {button_color};
        color: {text_color};
        font-weight: bold;
        border-radius: 8px;
        padding: 0.6rem 1.2rem;
        border: none;
        box-shadow: 2px 2px 6px rgba(0,0,0,0.1);
    }}
    .stButton > button:hover {{
        opacity: 0.9;
        transform: scale(1.02);
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# --- Sidebar ---
with st.sidebar:
    st.header("🧭 How It Works")
    st.markdown("""
    1. Choose your **vibe**: roast or compliment 🔥🌸
    2. Adjust your **mood slider** 😢 → 😐 → 😊
    3. Type your thoughts below ✏️
    4. Click **Generate Response** 🎭

    ---
    🌀 **MoodSwing** is an NLP-powered sass & sweetness bot for your emotional rollercoaster.

    💡 Tip: Try negative mood in compliment mode... or vice versa 😈

    🧠 Powered by TextBlob, Streamlit, and late-night debugging.
    """)
    st.markdown("👨‍💻 Created by [HarshamIrfan](https://github.com/HarshamIrfan)")

# --- Main Title ---
st.markdown("<div class='title-text'>🌀 MoodSwing: Your Sass or Sweetness Bot</div>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Roasted or complimented... choose your fate. 😈✨</p>", unsafe_allow_html=True)

# --- Mode Selection ---
mode = st.radio("\nChoose your mode:", ["🔥 Roast Me", "🌸 Compliment Me"], horizontal=True)

# --- Mood Slider ---
mood = st.slider("Mood Override", -1.0, 1.0, 0.0, step=0.1, help="Override the sentiment detection with your own mood")

# --- User Input ---
user_input = st.text_input("\n💬 Enter a message, thought, or confession:")

# --- Response Generation ---
def typewriter_effect(text, delay=0.03):
    """Simulate typewriter animation"""
    message = ""
    placeholder = st.empty()
    for char in text:
        message += char
        placeholder.markdown(f"```\n{message}\n```")
        time.sleep(delay)

if st.button("Generate Response 🎭"):
    if mode == "🔥 Roast Me":
        response = smart_sentiment_roast(user_input, override_sentiment=mood)
        st.markdown(f"### 🔥 Your Roast:")
        typewriter_effect(response)

        # Add to history
        st.session_state.history.append(("Roast", mood, user_input, response))

        # Roast GIFs
        if mood > 0.3:
            st.image("https://media1.tenor.com/m/PzY75riTLG0AAAAd/cat-yoongi.gif")
        elif mood < -0.1:
            st.image("https://media1.tenor.com/m/AhfDbzzEIA8AAAAd/qc-got.gif")
        else:
            st.image("https://media1.tenor.com/m/gaEpIfzxzPEAAAAd/pedro-monkey-puppet.gif")

    else:
        response = sweet_sentiment_compliment(user_input, override_sentiment=mood)
        st.markdown(f"### 🌸 Your Compliment:")
        typewriter_effect(response)

        # Add to history
        st.session_state.history.append(("Compliment", mood, user_input, response))

        # Compliment GIFs
        if mood > 0.3:
            st.image("https://media1.tenor.com/m/m98IlNDRa90AAAAd/snoop-dogg-happy.gif")
        elif mood < -0.1:
            st.image("https://media1.tenor.com/m/fQcCh4zbzDEAAAAd/thanxy.gif")
        else:
            st.image("https://media1.tenor.com/m/8zD-n1GzyUcAAAAd/sigma-detected-respect.gif")

# --- Footer ---
st.markdown("---")

# --- History Log ---
if st.session_state.history:
    st.markdown("### 📜 Interaction History")
    for i, (mtype, mood, user_text, result) in enumerate(reversed(st.session_state.history)):
        st.markdown(f"**{mtype}** | Mood: `{mood:+.2f}` | Input: _{user_text}_")
        st.markdown(f"\> {result}")
        st.markdown("---")

st.caption("🧠 Powered by TextBlob | ✨ Designed with Streamlit | ☕ Fuelled by caffeine")
