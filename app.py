import streamlit as st

# ---------------------- CONFIGURACIÓN ---------------------
st.set_page_config(page_title="Portafolio Paula Chirinos", layout="wide")

# Estilo de separadores lilas
st.markdown("""
    <style>
        .section-divider {
            border: none;
            height: 4px;
            background: linear-gradient(to right, #a26dd8, #e6d6ff);
            margin: 2rem 0;
        }
    </style>
""", unsafe_allow_html=True)

# ---------------------- DATOS PERSONALES ---------------------
info = {
    "Pronoun": "ella",
    "Name": "Paula",
    "Full_Name": "PAULA JIMENA CHIRINOS MOLINA",
    "Intro": "Publicista en formación. Apasionada por el cine y la fotografía",
    "About": """¡Hola! Soy Paula, estudiante de quinto ciclo de la carrera de Publicidad en la PUCP. 
Me encantan las artes y poder orientar aspectos empresariales del Marketing hacia lo creativo, 
participando en voluntariados orientados al cine o trabajos de atención al cliente donde aplicar estrategias 
para la transmisión de mensajes inspiradores.

Vinculado a la transmisión, conoce un poco de mis experiencias fotográficas en Instagram: 
[paula_jchirinos](https://www.instagram.com/paula_jchirinos?igsh=MXZvbXRiMzMwcDZ1MA&utm_source=qr)""",
    "City": "Lima, Perú",
    "Photo": "https://i.imgur.com/27mdmhl.jpeg",
    "Email": "a20230941@pucp.edu.pe",
    "Phone": "999003581"
}

endorsements = {
    "img1": "https://i.imgur.com/yds3ZeZ.jpeg",
    "img2": "https://i.imgur.com/J70h2sZ.jpeg",
    "img3": "https://i.imgur.com/F1gVb1E.jpeg",
    "img4": "https://i.imgur.com/ObAo2g7.jpeg",
    "img5": "https://i.imgur.com/99Ux7Le.jpeg",
    "img6": "https://i.imgur.com/QR7sVIw.jpeg"
}

# ---------------------- CONTENIDO ---------------------

# Header
st.markdown(f"""
    <div style="
        background-image: url('{info['Photo']}');
        background-size: cover;
        background-position: center;
        min-height: 100vh;
        display: flex;
        align-items: center;
        justify-content: center;
        position: relative;
        border-radius: 0 0 15px 15px;
    ">
        <div style="
            background-color: rgba(0, 0, 0, 0.55);
            padding: 40px;
            border-radius: 15px;
            max-width: 800px;
            text-align: center;
            color: white;
        ">
            <h1 style="margin-bottom: 10px;">{info["Full_Name"]}</h1>
            <h4 style="margin-top: 0;">{info["Intro"]}</h4>
            <p style="font-size:16px; line-height:1.6;">
                📍 {info["City"]}<br>
                ✉️ {info["Email"]}<br>
                📞 {info["Phone"]}
            </p>
        </div>
    </div>
""", unsafe_allow_html=True)


st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

# Sobre mí
st.markdown("## Sobre mí")
st.write(info["About"])
st.markdown("""
<div style="background-color:#e6d6ff; padding:20px; border-radius:10px; color:#2e175d; font-size:16px;">
    <h3 style='color:#5f2c9c;'/h3>
      "Estudio publicidad, porque me encanta capturar el mundo a través de mi lente, y busco combinar aquella sensibilidad visual con habilidades estratégicas de la comunicación.
     Cuento con experiencia en el apoyo a la organización de festivales de cine, atención al cliente y ponencias institucionales representando a mi universidad frente a colegios y familias de todo el Perú.
    Curiosa, comprometida y creativa, son algunos de los adjetivos que se me adjudican en mi intento de generar conexiones significativas entre las personas y las marcas a través de ideas que inspiran."
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)


# Experiencia Laboral y Objetivo Profesional en columnas
col1, col2 = st.columns(2)

with col1:
    st.markdown("## 🧳 Experiencia Laboral")
    st.write("- **Atención al cliente en fast food** (2024-2025)")
    st.write("- **Apoyo administrativo - Oficina de Admisión PUCP** (2025–actualidad)")

with col2:
    st.markdown("""
    <div style="background-color:#e6d6ff; padding:20px; border-radius:10px">
        <h3 style='color:#5f2c9c;'>🎯 Objetivo Profesional</h3>
        <p>Desarrollarse como estratega creativa en la industria publicitaria, integrando su pensamiento analítico, sensibilidad cultural y gusto por la narrativa visual para crear campañas relevantes y auténticas.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

# Habilidades y Certificaciones
## Certificaciones y Habilidades en columnas (intercambiadas)
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div style="background-color:#e6d6ff; padding:20px; border-radius:10px; color:#2e175d;">
        <h3 style='color:#5f2c9c;'>📜 Certificaciones</h3>
        <ul>
            <li>Cambridge B1 Preliminary</li>
            <li>Certificado del IB en Artes Visuales (2022)</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("## 🛠️ Habilidades")
    st.write("- **Canva**")
    st.write("- **Excel**")
    st.write("- **Inglés B1**")
    st.write("- **Artes visuales**")


st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

# Galería y Exploración en columnas
col1, col2 = st.columns([2, 1])  # Puedes ajustar proporciones

# Columna 1: Galería
with col1:
    st.markdown("## 📸 Galería de experiencias")
    
    imagenes = [
        {"url": endorsements["img1"], "caption": "AFICHE PROPIO DEL CORTO LA SILLA ANTE EL BANCO"},
        {"url": endorsements["img2"], "caption": "TRABAJO EN REDES Y ORIENTACIÓN COMO GUÍA PUCP"},
        {"url": endorsements["img3"], "caption": "VER Y DESCUBRIR: EVAPORACIÓN ARBÓREA EN MATUCANA"},
        {"url": endorsements["img4"], "caption": "FOTOGRAFIANDO PASIONES: EL McLAREN DE AYRTON SENNA"},
        {"url": endorsements["img5"], "caption": "RIELES ESTRECHOS: CRUCE DEL TREN EN MATUCANA"},
        {"url": endorsements["img6"], "caption": "VIAJAR Y RECORDAR: LA LUNA DESDE BUENOS AIRES"}
    ]

    if "img_index" not in st.session_state:
        st.session_state.img_index = 0

    # Estilo para botones de flecha personalizados usando Streamlit
st.markdown("""
    <style>
    div.stButton > button {
        background-color: #a26dd8;
        color: white;
        border: none;
        font-size: 20px;
        padding: 10px 16px;
        border-radius: 50%;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
        transition: background-color 0.3s ease;
    }
    div.stButton > button:hover {
        background-color: #7a45b2;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# Botones y galería en columnas
col_img1, col_img2, col_img3 = st.columns([1, 6, 1])

with col_img1:
    if st.button("⬅️", key="prev_img"):
        st.session_state.img_index = (st.session_state.img_index - 1) % len(imagenes)

with col_img3:
    if st.button("➡️", key="next_img"):
        st.session_state.img_index = (st.session_state.img_index + 1) % len(imagenes)

# Imagen en el centro
img_actual = imagenes[st.session_state.img_index]
with col_img2:
    st.markdown(f"""
        <div style='text-align: center;'>
            <img src="{img_actual['url']}" style="max-height:400px; width:auto; border-radius:10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);" />
            <p style='color:#5f2c9c; margin-top:10px;'>{img_actual['caption']}</p>
            <p style='color:gray; font-size:14px;'>Imagen {st.session_state.img_index + 1} de {len(imagenes)}</p>
        </div>
    """, unsafe_allow_html=True)

        <p style='color:#5f2c9c; margin-top:10px;'>{img_actual['caption']}</p>
        <p style='color:gray; font-size:14px;'>Imagen {st.session_state.img_index + 1} de {len(imagenes)}</p>
    </div>
""", unsafe_allow_html=True)

# Columna 2: Explora más sobre Paula
with col2:
    st.markdown("## 🔍 Explora más sobre Paula")

    seccion = st.selectbox(
        "Selecciona una sección para ver más información:",
        [
            "---",
            "Fortalezas y ventajas",
            "Desafíos",
            "Intereses y pasatiempos",
            "Portafolio",
            "Disponibilidad",
            "Referencias"
        ]
    )

    if seccion == "Fortalezas y ventajas":
        st.markdown("### Fortalezas y Ventajas")
        st.write("Empática, observadora y versátil, Paula se adapta con facilidad a contextos dinámicos. Su curiosidad constante y dedicación le permiten aportar una mirada fresca y comprometida a los proyectos.")

    elif seccion == "Desafíos":
        st.markdown("### Desafíos")
        st.write("Su nivel de detalle puede ralentizar algunos procesos, pero garantiza resultados cuidados y coherentes con los objetivos del proyecto.")

    elif seccion == "Intereses y pasatiempos":
        st.markdown("### Intereses y Pasatiempos")
        st.write("Apasionada por la fotografía, Paula disfruta documentar escenas cotidianas, explorar rincones urbanos, ver cine independiente y compartir conversaciones largas con café de por medio. También le interesa contar historias visuales en redes sociales.")

    elif seccion == "Portafolio":
        st.markdown("### Portafolio")
        st.write("Actualmente se encuentra desarrollando un portafolio digital que reúna sus trabajos en fotografía, producción de eventos y conceptos creativos. Su objetivo es mostrar su enfoque multidisciplinario y su estilo personal.")

    elif seccion == "Disponibilidad":
        st.markdown("### Disponibilidad")
        st.write("Abierta a prácticas, proyectos freelance o roles de asistencia en publicidad, eventos y creación de contenido.")

    elif seccion == "Referencias":
        st.markdown("### Referencias")
        st.write("Disponibles a solicitud.")



# Footer
st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
st.markdown("Creado por Paula Jimena Chirinos Molina usando Streamlit.")


