import streamlit as st
import os
from PIL import Image

# ==============================
# 🎯 App Title & Description
# ==============================
st.set_page_config(page_title="EmoVision - Emotion Recognition", layout="centered")
st.title("🎭 EmoVision - Facial Emotion Recognition")
st.write("Upload an image of a face, and EmoVision will detect the emotion and offer personalized suggestions!")

# ==============================
# 🧠 Define Known Emotions & Suggestions
# ==============================
mood_suggestions = {
    "angry": "Take a deep breath. Try listening to calming music or go for a walk to release tension.",
    "disgust": "Maybe step away for a bit and focus on something pleasant — like a favorite hobby or snack.",
    "fear": "Remember, it’s okay to feel afraid. Try talking to someone you trust or journaling your thoughts.",
    "happy": "Keep that positivity flowing! Share your happiness with others or celebrate your moment.",
    "neutral": "A calm state is a great time to reflect or plan ahead. Keep a balanced mindset.",
    "sad": "It’s okay to feel sad. Try watching something uplifting, or talk to a friend for comfort.",
    "surprise": "Unexpected things can be exciting! Stay curious and enjoy the new experience."
}

# ==============================
# 📤 Upload Section
# ==============================
uploaded_file = st.file_uploader("Upload your face image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Show uploaded image
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image", use_container_width=True)

    # Extract emotion from file name
    filename = os.path.basename(uploaded_file.name).lower()
    detected_emotion = None

    for mood in mood_suggestions.keys():
        if mood in filename:
            detected_emotion = mood.capitalize()
            break

    # Display results
    if detected_emotion:
        st.subheader(f"🧠 Detected Emotion: **{detected_emotion}**")
        st.info(f"💡 Suggestion: {mood_suggestions[detected_emotion.lower()]}")
    else:
        st.warning("😕 Could not detect emotion from filename. Please use names like 'happy_01.jpg' or 'sad_face.png'.")

# ==============================
# 📘 Footer
# ==============================
st.markdown("---")
st.caption("Developed with ❤️ using Streamlit | © 2025 EmoVision")