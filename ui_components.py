
import streamlit as st

def apply_custom_style():
    """
    Aplica estilos CSS de alta gama para un dashboard de trading profesional.
    """
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
        }

        .main {
            background-color: #0B0E11;
            color: #EAECEF;
        }

        /* Metrics Cards */
        [data-testid="stMetric"] {
            background-color: #1E2329;
            border: 1px solid #2B3139;
            padding: 20px !important;
            border-radius: 12px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transition: transform 0.2s;
        }
        [data-testid="stMetric"]:hover {
            transform: translateY(-2px);
            border-color: #F0B90B;
        }

        /* Tabs Styling */
        .stTabs [data-baseweb="tab-list"] {
            background-color: #1E2329;
            padding: 10px 20px;
            border-radius: 12px 12px 0 0;
            gap: 15px;
        }
        .stTabs [data-baseweb="tab"] {
            color: #848E9C;
            font-weight: 600;
            padding: 12px 24px;
            border-radius: 8px;
            border: none !important;
        }
        .stTabs [aria-selected="true"] {
            background-color: #2B3139 !important;
            color: #F0B90B !important;
        }

        /* Sidebar Styling */
        [data-testid="stSidebar"] {
            background-color: #181A20;
            border-right: 1px solid #2B3139;
        }

        /* Success/Error messages */
        .stAlert {
            border-radius: 12px;
            border: none;
        }

        /* Buttons */
        .stButton button {
            background-color: #F0B90B;
            color: #000000;
            border-radius: 8px;
            font-weight: 700;
            border: none;
            width: 100%;
        }
        .stButton button:hover {
            background-color: #F8D33A;
            color: #000000;
        }

        /* News Cards */
        .news-container {
            background-color: #1E2329;
            border: 1px solid #2B3139;
            padding: 20px;
            border-radius: 12px;
            margin-bottom: 15px;
        }
    </style>
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
