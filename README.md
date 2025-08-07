# 🌀 MoodSwing: NLP Sentiment Analysis 🤖

**MoodSwing** is a fun and sassy NLP-powered web app that roasts or compliments users based on the sentiment of their input — or lets them override the mood with an emoji-style slider.

Built with [Streamlit](https://streamlit.io), deployed via [Render](https://render.com), and filled with developer-themed wit and warmth.

---

## 🌟 Features

- 🔥 **Roast Me Mode** – Get burned with sentiment-aware tech insults (all in good fun)
- 🌸 **Compliment Me Mode** – Get praised for your inner glow (even when debugging)
- 🎭 **Mood Slider** – Override sentiment with a 😢 → 😊 scale
- 🌶️ **Intensity Control** – Choose how mild or savage the roast/compliment is
- 🎞️ **GIF Reactions** – Dynamic images based on mood
- 📜 **Built-in Roast & Compliment Bank** – Fully custom, developer-themed responses

---

## 🚀 How to Run Locally

1. Clone this repo:

```bash
git clone https://github.com/HarshamIrfan/NLP-Sentiment-Analysis---RoastMe.git
cd NLP-Sentiment-Analysis---RoastMe
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Download NLTK data:

```python
import nltk
nltk.download('punkt')
```

4. Run the app:

```bash
streamlit run app.py
```

---

## 🌐 Live Demo

> 🔗 [Visit the deployed app on Render](https://your-render-url-here.com)  
(Replace this with your actual URL after deployment)

---

## 🧠 Technologies Used

- Python 3.11
- Streamlit
- TextBlob (for sentiment analysis)
- NLTK
- GitHub + Render for deployment

---

## 📁 Project Structure

```
├── app.py                     # Main Streamlit app UI
├── roast_engine.py           # Sentiment-based roast logic
├── compliment_engine.py      # Sentiment-based compliment logic
├── roast_bank.py             # Categorized roast lists
├── compliment_bank.py        # Categorized compliment lists
├── requirements.txt          # All dependencies
└── assets/                   # Optional GIFs/images (if local)
```

---

## 🙌 Acknowledgments

- Made as an assignment during ML Training conducted.
- GIFs sourced from [Tenor](https://tenor.com/) for extra spice

---

## 👨‍💻 Author

**Harsham Irfan**  
GitHub: [@HarshamIrfan](https://github.com/HarshamIrfan)

---

## 🪄 License

MIT License – use it, remix it, deploy it, just give credit. 
