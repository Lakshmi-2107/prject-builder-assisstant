import streamlit as st
import requests
import io
import zipfile

OLLAMA_URL = "http://localhost:11434/api/generate"

# -----------------------------
# SESSION STATE
# -----------------------------
if "code" not in st.session_state:
    st.session_state["code"] = None

if "roadmap" not in st.session_state:
    st.session_state["roadmap"] = None

# -----------------------------
# AI CALL
# -----------------------------
def generate_response(prompt):
    try:
        res = requests.post(OLLAMA_URL, json={
            "model": "mistral",
            "prompt": prompt,
            "stream": False
        })
        return res.json()["response"]
    except:
        return "Error connecting to model"

# -----------------------------
# DOMAIN DETECTION
# -----------------------------
def detect_domain(idea):
    idea = idea.lower()

    if "travel" in idea:
        return "travel"
    elif "movie" in idea:
        return "movie"
    elif "resume" in idea:
        return "resume"
    elif "quiz" in idea:
        return "quiz"
    elif "calculator" in idea:
        return "calculator"
    elif "medical" in idea or "health" in idea:
        return "medical"
    elif "beauty" in idea:
        return "beauty"
    elif "fraud" in idea:
        return "fraud"
    elif "study" in idea or "education" in idea:
        return "study"
    elif "agriculture" in idea or "crop" in idea:
        return "agriculture"
    elif "uber" in idea or "booking" in idea:
        return "uber"
    else:
        return "general"

def chat_response(user_input):
    prompt = f"""
You are a helpful AI assistant.

Rules:
- Do NOT repeat the user's question
- Give clear, useful answers
- Be concise and meaningful

User: {user_input}
Assistant:
"""
    return generate_response(prompt)      
# -----------------------------
# LIVE DEMO ENGINE
# -----------------------------
def render_live_app(domain):
    
    # -------- TRAVEL --------
    if domain == "travel":
        st.title("🌍 Smart Travel Planner")

        place = st.text_input("Destination", key="travel_place")
        days = st.number_input("Days", 1, 10, key="travel_days")

        if st.button("Generate Plan", key="travel_btn"):

            if place:

                with st.spinner("Planning your trip..."):
                    response = generate_response(
                        f"List 6 famous tourist places in {place}"
                    )

                    places = [p.strip() for p in response.split("\n") if p.strip()]

                    if len(places) < 3:
                        places = [
                            "City Center",
                            "Local Market",
                            "Famous Landmark",
                            "Museum",
                            "Park",
                            "Cultural Site"
                        ]

                st.header(f"✈ Trip to {place.title()} for {days} days")

                for i in range(1, days + 1):
                    st.subheader(f"📅 Day {i}")

                    if i == 1:
                        st.write(f"• Arrival at {place}")
                        st.write("• Hotel check-in")
                        st.write(f"• Visit {places[0]}")
                        st.write("• Evening dinner")

                    elif i == days:
                        st.write(f"• Visit {places[-1]}")
                        st.write("• Shopping")
                        st.write("• Departure")

                    else:
                        idx1 = i % len(places)
                        idx2 = (i + 1) % len(places)

                        st.write(f"• Visit {places[idx1]}")
                        st.write(f"• Explore {places[idx2]}")
                        st.write("• Try local cuisine")
                        st.write("• Evening relaxation")

                    st.divider()

                st.subheader("🏨 Hotels")
                st.write(f"• Budget: {place} Budget Inn")
                st.write(f"• Mid-range: {place} Comfort Hotel")
                st.write(f"• Luxury: {place} Grand Palace")

                st.subheader("💡 Travel Tips")
                st.write("• Start early")
                st.write("• Use local transport")
                st.write("• Keep essentials ready")

            else:
                st.warning("Enter destination")

    # -------- MOVIE --------
    elif domain == "movie":
        st.title("🎬 Movie Recommender")

        genre = st.text_input("Genre", key="movie_genre")
        language = st.text_input("Language", key="movie_language")

        if st.button("Recommend", key="movie_btn"):
            res = generate_response(
                f"Suggest 5 {language} {genre} movies"
            )
            st.write(res)

    # -------- RESUME --------
    elif domain == "resume":
        st.title("📄 Resume Analyzer")

        file = st.file_uploader("Upload Resume PDF", key="resume_file")

        if file:
            st.success("Resume uploaded")
            st.write("Skills: Python, AI")
            st.write("Score: 85/100")

    # -------- QUIZ --------
    elif domain == "quiz":
        st.title("❓ Quiz Generator")

        topic = st.text_area("Enter topic", key="quiz_topic")

        if st.button("Generate", key="quiz_btn"):
            st.write("Q1: What is AI?")
            st.write("Q2: Explain ML")

    # -------- CALCULATOR --------
    elif domain == "calculator":
        st.title("🧮 Calculator")

        a = st.number_input("Number 1", key="calc_a")
        b = st.number_input("Number 2", key="calc_b")

        op = st.selectbox("Operation", ["+", "-", "*", "/"], key="calc_op")

        if st.button("Calculate", key="calc_btn"):
            if op == "+": st.success(a + b)
            elif op == "-": st.success(a - b)
            elif op == "*": st.success(a * b)
            elif op == "/": st.success(a / b if b != 0 else "Error")

    # -------- MEDICAL --------
    elif domain == "medical":
        st.title("🏥 Medical Assistant")

        symptoms = st.text_input("Enter symptoms", key="medical_symptoms")

        if st.button("Analyze", key="medical_btn"):
            response = generate_response(
                f"User has symptoms: {symptoms}. Suggest possible conditions and precautions."
            )
            st.write(response)

    # -------- FRAUD --------
    elif domain == "fraud":
        st.title("🛡 Fraud Detection")

        amount = st.number_input("Transaction Amount", key="fraud_amount")
        location = st.text_input("Location", key="fraud_location")

        if st.button("Check", key="fraud_btn"):
            if amount > 100000:
                st.error("⚠ High risk transaction")
            else:
                st.success("✅ Transaction seems safe")

    # -------- AGRICULTURE --------
    elif domain == "agriculture":
        st.title("🌾 Crop Recommendation System")

        soil = st.text_input("Soil Type", key="agri_soil")
        location = st.text_input("Location", key="agri_location")

        if st.button("Suggest Crop", key="agri_btn"):
            response = generate_response(
                f"Suggest best crops for {soil} soil in {location}"
            )
            st.write(response)

    # -------- CHATBOT --------
    else:
        st.title("🤖 AI Assistant")

        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []

        user_input = st.text_input("Ask something", key="chat_input")

        if st.button("Send", key="chat_btn"):
            if user_input:
                response = chat_response(user_input)

                st.session_state.chat_history.append(("You", user_input))
                st.session_state.chat_history.append(("Bot", response))

        for role, msg in st.session_state.chat_history:
            if role == "You":
                st.markdown(f"**🧑 You:** {msg}")
            else:
                st.markdown(f"**🤖 Bot:** {msg}")
# -----------------------------
# UI
# -----------------------------
st.set_page_config(page_title="AI Project Builder", layout="wide")

st.title("🚀 AI Project Builder")

idea = st.text_area("Enter your project idea")

tab1, tab2, tab3, tab4 = st.tabs([
    "📌 Roadmap",
    "💻 Code",
    "⚡ Live Demo",
    "📦 Export"
])

# -----------------------------
# ROADMAP
# -----------------------------
with tab1:
    if st.button("Generate Roadmap"):
        st.session_state["roadmap"] =generate_response(
    f"""
    Create a detailed project roadmap for: {idea}

    Include:
    1. Overview of the project
    2. Step-by-step phases (Phase 1, Phase 2, etc.)
    3. Technologies to use
    4. Tools required
    5. Timeline (weekly breakdown)
    6. Expected output of each phase

    Give a clear, well-structured explanation like a proper plan, not a short answer.
    """
)

    if st.session_state["roadmap"]:
        st.markdown(st.session_state["roadmap"])

# -----------------------------
# CODE
# -----------------------------
with tab2:
    if st.button("Generate Code"):
        st.session_state["code"] = generate_response(
            f"Create Streamlit app for {idea}"
        )

    if st.session_state["code"]:
        st.code(st.session_state["code"])

# -----------------------------
# LIVE DEMO (AUTO)
# -----------------------------
with tab3:
    if idea:
        render_live_app(detect_domain(idea))
    else:
        st.info("Enter idea to see live demo")

# -----------------------------
# EXPORT
# -----------------------------
with tab4:
    st.subheader("📦 Export Project")

    if st.session_state["code"] or st.session_state["roadmap"]:

        zip_buffer = io.BytesIO()

        with zipfile.ZipFile(zip_buffer, "w") as z:
            if st.session_state["code"]:
                z.writestr("app.py", st.session_state["code"])
            if st.session_state["roadmap"]:
                z.writestr("roadmap.txt", st.session_state["roadmap"])

        st.download_button(
            "⬇ Download Project",
            zip_buffer.getvalue(),
            "project.zip"
        )

    else:
        st.warning("Generate code or roadmap first")