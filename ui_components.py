
import streamlit as st

def apply_custom_style():
    """
    Injeta um design Hyper-Modern de Terminal de Trading.
    """
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Inter:wght@300;400;600&display=swap');

        /* Reset e Fundo */
        .main {
            background: radial-gradient(circle at top right, #1a1c23, #08090a);
            color: #ffffff;
        }

        /* Esconder cabeçalho padrão do Streamlit */
        header {visibility: hidden;}
        footer {visibility: hidden;}

        /* Sidebar Modernizada */
        [data-testid="stSidebar"] {
            background-color: rgba(15, 17, 21, 0.95);
            border-right: 1px solid #F0B90B33;
            box-shadow: 5px 0 15px rgba(0,0,0,0.5);
        }

        /* Tabs Modernas estilo Apple/Binance */
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px;
            background-color: rgba(255, 255, 255, 0.03);
            padding: 8px;
            border-radius: 15px;
            border: 1px solid rgba(255, 255, 255, 0.05);
        }
        .stTabs [data-baseweb="tab"] {
            border-radius: 10px !important;
            padding: 10px 25px !important;
            border: none !important;
            color: #848e9c !important;
            font-family: 'Inter', sans-serif;
            transition: all 0.3s;
        }
        .stTabs [aria-selected="true"] {
            background: linear-gradient(135deg, #F0B90B 0%, #ca9600 100%) !important;
            color: #000000 !important;
            font-weight: bold !important;
            box-shadow: 0 4px 15px rgba(240, 185, 11, 0.3);
        }

        /* Estilização de Containers (Cards Customizados) */
        .trading-card {
            background: rgba(30, 35, 41, 0.5);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(240, 185, 11, 0.1);
            border-radius: 20px;
            padding: 25px;
            margin-bottom: 20px;
            transition: transform 0.3s, border 0.3s;
        }
        .trading-card:hover {
            border: 1px solid #F0B90B;
            transform: translateY(-5px);
        }

        /* Títulos */
        h1, h2, h3 {
            font-family: 'Orbitron', sans-serif;
            letter-spacing: 2px;
            text-transform: uppercase;
        }
        .main-title {
            background: linear-gradient(to right, #F0B90B, #ffffff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 2.5rem !important;
            font-weight: 800;
        }

        /* Glow para botões */
        .stButton button {
            background: linear-gradient(90deg, #F0B90B, #ca9600) !important;
            color: black !important;
            border: none !important;
            border-radius: 12px !important;
            font-weight: 800 !important;
            height: 50px !important;
            text-transform: uppercase;
            box-shadow: 0 0 15px rgba(240, 185, 11, 0.2);
        }
        .stButton button:hover {
            box-shadow: 0 0 25px rgba(240, 185, 11, 0.5) !important;
            transform: scale(1.02);
        }
    </style>
    """, unsafe_allow_html=True)

def render_custom_metric(label, value, delta=None, color="#F0B90B"):
    """
    Renderiza um card de métrica ultra-moderno em HTML puro.
    """
    delta_html = ""
    if delta:
        d_color = "#0ecb81" if "+" in delta or float(delta.replace('%','')) > 0 else "#f6465d"
        delta_html = f"<div style='color: {d_color}; font-size: 0.9rem; font-weight: bold;'>{delta}</div>"

    st.markdown(f"""
    <div style="
        background: rgba(255, 255, 255, 0.03);
        border-left: 4px solid {color};
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        backdrop-filter: blur(4px);
    ">
        <div style="color: #848e9c; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 1px;">{label}</div>
        <div style="color: #ffffff; font-size: 1.8rem; font-weight: 800; margin: 5px 0;">{value}</div>
        {delta_html}
    </div>
    """, unsafe_allow_html=True)

def render_metric_card(label, value, delta=None, sentiment=None):
    """
    Renderiza um card de métrica personalizado.
    """
    with st.container():
        st.metric(label=label, value=value, delta=delta)

def render_how_it_works():
    """
    Explicación técnica clara y profesional sobre la integración de datos.
    """
    st.markdown("## 🧠 Metodología y Fuentes de Datos")

    st.markdown("""
    Este dashboard integra múltiples fuentes de datos para ofrecer una visión consolidada del mercado. A continuación, detallamos qué significa cada componente:
    """)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 1. Integración de Datos (Back-end)")
        st.markdown("""
        *   **yfinance (Yahoo Finance):** Proporciona datos históricos OHLCV (Apertura, Máximo, Mínimo, Cierre, Volumen). Es la base para analizar **tendencias de largo plazo** y patrones de precios.
        *   **NewsAPI:** Agregador de noticias financieras en tiempo real. Nos permite monitorear el flujo constante de información global que impacta el sentimiento del mercado.
        *   **Alpha Vantage:** Ofrece datos de series temporales diarias de alta calidad, fundamentales para el análisis técnico más granular y la validación de movimientos de precios.
        """)

    with col2:
        st.markdown("### 2. Análisis IA (Procesamiento)")
        st.markdown("""
        *   **VADER (NLP):** Utilizamos un modelo de Procesamiento de Lenguaje Natural para cuantificar el sentimiento de los titulares de las noticias.
        *   **Cuantificación:** VADER asigna una puntuación de polaridad entre **-1 (muy negativo)** y **+1 (muy positivo)**.
        *   **Señal MVP:** Agregamos el promedio ponderado de estos scores para determinar la tendencia de sentimiento actual.
            - *🟢 Positivo:* Optimismo predominante en las noticias.
            - *🔴 Negativo:* Incertidumbre o noticias bajistas.
            - *🟡 Neutral:* Falta de catalizadores claros.
        """)

    st.markdown("---")
    st.info("💡 **Nota para el Trader:** Este dashboard transforma datos no estructurados (noticias) en métricas accionables, permitiendo una toma de decisiones basada en datos cuantitativos y cualitativos.")
