import streamlit as st
import plotly.express as px
import pandas as pd
from datetime import datetime, timedelta

# Configuración de página
st.set_page_config(page_title="Carta para Isa 💖", layout="centered")

# ----------- PREGUNTAS -----------
questions = [
    {"question": "¿Cómo se llama el bebé de Isa y Santi?", "answer": "Zeus"},
    {"question": "¿Cuál es el correo de Isa chistoso?", "answer": "isalondon03@gmail.com"}
]

if "current_question" not in st.session_state:
    st.session_state.current_question = 0
if "answers_correct" not in st.session_state:
    st.session_state.answers_correct = False
if "show_secret" not in st.session_state:
    st.session_state.show_secret = False

st.title("💌 Validación antes de ver tu carta especial")

# Preguntas
if st.session_state.current_question < len(questions):
    q = questions[st.session_state.current_question]
    user_input = st.text_input(q["question"], key=f"q_{st.session_state.current_question}")

    if st.button("Responder"):
        if user_input.strip().lower() == q["answer"].lower():
            st.success("✅ ¡Correcto!")
            st.session_state.current_question += 1
        else:
            st.error("❌ Intenta de nuevo.")
else:
    st.session_state.answers_correct = True

# ----------- CARTA -----------
if st.session_state.answers_correct:
    st.subheader("🎉 ¡Una carta especial celebrando tu vida!")

    birth_date = datetime(2003, 7, 21)
    today_date = datetime(2025, 7, 21)

    # Edad
    total_days = (today_date - birth_date).days
    years = total_days // 365
    months = (total_days % 365) // 30
    days = (total_days % 365) % 30

    st.markdown(f"""
    Hoy celebramos **22 añitos** de la vida de **Isabellita Salamanca Trujillo** 🎂  
    Es una alegría inmensa poder compartir mi vida a tu lado, mi amor 💖  
    """)

    # ----------- LÍNEA DE TIEMPO MEJORADA -----------
    timeline_labels = [
        "Nacimiento 👶",
        "Primer día de escuela 🎒",
        "Nos conocimos 💘",
        "Graduación del colegio 🎓",
        "Inicio universidad 🎯",
        "Nuestro primer viaje ✈️",
        "Aniversario especial 💝",
        "Hoy 💖"
    ]

    base_date = datetime(2000, 1, 1)
    duration = timedelta(days=30)

    data = []
    for i, etapa in enumerate(timeline_labels):
        start = base_date + timedelta(days=i * 40)
        end = start + duration
        data.append({"Etapa": etapa, "Inicio": start, "Fin": end})

    df = pd.DataFrame(data)

    fig = px.timeline(
    df,
    x_start="Inicio",
    x_end="Fin",
    y="Etapa",
    color="Etapa",
    title="Línea del tiempo de tu vida ✨"
)

    fig.update_yaxes(autorange="reversed")
    fig.update_layout(
        showlegend=False,
        height=400,
        xaxis=dict(
            showticklabels=False,  # 👈 Oculta los años
            showgrid=False,
            title=""
        )
    )

    st.plotly_chart(fig, use_container_width=True)

    # ----------- VIDEO DE YOUTUBE -----------
    st.markdown("### 🎶 Una canción especial para acompañar esta carta:")
    st.video("https://www.youtube.com/watch?v=FE_KnGLsX5c")

    # ----------- MENSAJE SECRETO -----------
    if st.button("💖 Ver mensaje secreto"):
            st.session_state.show_secret = True

    if st.session_state.show_secret:
            st.success("💌 Mi amor...")
            st.markdown("""
            Desde que llegaste a mi vida, todo se volvió aún más lindo.  
            Cada momento contigo es un regalo, y cada día a tu lado lo atesoro como el más hermoso.  
            Esta carta es solo un reflejo de cuánto te amo y cuánto significas para mí.  
            Gracias por ser tú. 💘  
            """)

        # ----------- DESCARGA DE CARTA -----------
    carta = f"""
        Pochita hermosa,

        Hoy celebramos tus 22 años, y me siento afortunado de acompañarte en esta historia hermosa.
        Esta línea del tiempo es solo una forma de recordarte todo lo que has vivido y lo increíble que eres.
        Gracias mi amor, por cada risa, cada abrazo y cada momento compartido.

        Gracias por ser tan amorosa en los consentimientos que me dashh, tan especial en momentos díficiles y en todos los detalles que me haces,
        tan comprensiva y paciente en mis momentos de estrés, tan divertida en nuestras locuras, tan apasionada en tus sueños y metas, y tan única en todo lo que haces. 
        
        Gracias también por elegirme como tu compañero de vida, una vida que en la que hemos vivido momentos espectaculares juntos, y que 
        estoy seguro que aún nos quedan muchos más por vivir.

        Todos esos momentos, que nos han hecho crecer juntos, son los que hacen que cada día a tu lado sea un regalo. Tus cualidades son infinitas,
        y cada una de ellas son las que me enamoran de ti una y otra vez. Son esas cualidades las cuales has sabido implementar 
        en nuestra relación, y que hacen que sea más fuerte cómo tu resiliencia, tu empatía, tu amor por la vida y tu capacidad de hacerme sonreír incluso en los días más difíciles.

        Gracias por ser ese motorcito que me impulsa a ser mejor cada día, por pensar un futuro a tu lado, y estar seguro que todo el esfuerzo y 
        trabajo valdrá la pena aún más si estás a mi lado.

        Mi amorcito, espero que este nuevo año de vida esté lleno de aventuras, risas y mucho amor, como siempre...
        Que éste nuevo año sea otro capítulo lleno de momentos inolvidables, y que sigamos escribiendo juntos nuestra historia.
        Te amo con todo mi corazón, y estoy emocionado por todo lo que nos espera.

        Nunca me alcanzarán las palabras para expresar lo agradecido que estoy por tenerte en mi vida pochita de mi alma, eres el amor
        de mi vida y eso no cambiará jamás. Sigamos consintiendo a nuestro bebé Zeus, sigamos viajando por el mundo, dejémonos sorprender por la vida juntos,
        y sigamos dejando huella en cada cosa que hacemos. Me siento muy orgulloso de todo lo que haces, de como no te rindes en cada una de tus experiencias.
        Eres una mujer increíble, valiente, inteligente y miles de cosas más que me hacen aprender de ti en cada momento.


        Espero que esta carta te haga sonreír y te recuerde lo especial que eres para mí polluelitaaa.

        Con amor,
        Santy 💖
        """
    st.download_button("📄 Descargar esta carta", carta, file_name="carta_para_isabellita.txt")
