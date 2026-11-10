
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from backend_data import get_stock_data, get_news_sentiment, get_daily_stock_data_alpha_vantage
from auth import login, logout
from ui_components import apply_custom_style, render_how_it_works

# Configuración de la página
st.set_page_config(
    layout="wide",
    page_title="Dashboard Profesional de Análisis de Acciones MVP",
    page_icon="📈"
)

# Aplicar estilo personalizado
apply_custom_style()

# Verificar autenticación
if not login():
    st.stop()

# --- Sidebar --- #
with st.sidebar:
    st.title("⚙️ Configuración")

    ticker_symbol = st.text_input(
        "Símbolo de la Acción (ej: AAPL, TSLA, BMA):",
        "AAPL"
    ).upper()

    period = st.selectbox(
        "Período Histórico:",
        ("1d", "5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "ytd", "max"),
        index=5
    )

    st.markdown("---")
    if st.button("Cerrar Sesión"):
        logout()

# --- Dashboard Principal --- #
st.title("📈 Dashboard Profesional de Análisis de Acciones")
st.caption("Herramienta MVP impulsada por IA para análisis de mercado y sentimiento de noticias.")

# Tabs principales
tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Panel Principal",
    "📉 Análisis Técnico",
    "📰 Noticias y Sentimiento",
    "❓ ¿Cómo Funciona?"
])

# --- Cargar datos una vez --- #
stock_data_yf = get_stock_data(ticker_symbol, period=period)
news_sentiment_data = get_news_sentiment(ticker_symbol)

# --- TAB 1: Panel Principal --- #
with tab1:
    st.subheader(f"Resumen General: {ticker_symbol}")

    if not stock_data_yf.empty:
        last_price = stock_data_yf['Close'].iloc[-1]
        prev_price = stock_data_yf['Close'].iloc[-2] if len(stock_data_yf) > 1 else last_price
        change = last_price - prev_price
        change_percent = (change / prev_price) * 100

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric("Último Precio", f"${last_price:.2f}", f"{change_percent:.2f}%")

        with col2:
            st.metric("Precio Máximo (Período)", f"${stock_data_yf['High'].max():.2f}")

        with col3:
            st.metric("Precio Mínimo (Período)", f"${stock_data_yf['Low'].min():.2f}")

        with col4:
            if news_sentiment_data:
                avg_score = sum([n['compound_score'] for n in news_sentiment_data]) / len(news_sentiment_data)
                sentiment_label = "Positivo" if avg_score >= 0.05 else ("Negativo" if avg_score <= -0.05 else "Neutral")
                st.metric("Sentimiento IA", sentiment_label, f"Score: {avg_score:.2f}")
            else:
                st.metric("Sentimiento IA", "N/D")

        st.markdown("### Gráfico Principal")
        fig = go.Figure(data=[go.Candlestick(
            x=stock_data_yf.index,
            open=stock_data_yf['Open'],
            high=stock_data_yf['High'],
            low=stock_data_yf['Low'],
            close=stock_data_yf['Close'],
            name=ticker_symbol
        )])
        fig.update_layout(
            template="plotly_dark",
            xaxis_rangeslider_visible=False,
            height=500
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.error(f"No se pudieron cargar los datos para {ticker_symbol}. Verifique el símbolo.")

# --- TAB 2: Análisis Técnico --- #
with tab2:
    st.subheader("Indicadores Técnicos y Datos Históricos")

    if not stock_data_yf.empty:
        st.dataframe(stock_data_yf.tail(15), use_container_width=True)

        st.markdown("### Datos Diarios Complementarios (Alpha Vantage)")
        stock_data_av = get_daily_stock_data_alpha_vantage(ticker_symbol)
        if not stock_data_av.empty:
            st.dataframe(stock_data_av.tail(10), use_container_width=True)
        else:
            st.warning("No se pudieron cargar datos de Alpha Vantage (límite alcanzado o clave no configurada).")

# --- TAB 3: Noticias y Sentimiento --- #
with tab3:
    st.subheader("Análisis de Sentimiento de Noticias")

    if news_sentiment_data:
        avg_score = sum([n['compound_score'] for n in news_sentiment_data]) / len(news_sentiment_data)

        if avg_score >= 0.05:
            st.success("🟢 **Señal IA: POSITIVA** - El mercado muestra optimismo en las noticias recientes.")
        elif avg_score <= -0.05:
            st.error("🔴 **Señal IA: NEGATIVA** - Prevalece la precaución o malas noticias.")
        else:
            st.info("🟡 **Señal IA: NEUTRAL** - Las noticias no reflejan una tendencia clara.")

        st.markdown("### Últimas Noticias Analizadas")
        for news in news_sentiment_data:
            with st.container():
                st.markdown(f"#### [{news['title']}]({news['url']})")
                st.caption(f"Fuente: {news['source']} | Sentimiento: **{news['sentiment']}** (Score: {news['compound_score']:.2f})")
                st.markdown("---")
    else:
        st.warning("No se encontraron noticias recientes o no se pudo conectar con la API de noticias.")

# --- TAB 4: Cómo Funciona --- #
with tab4:
    render_how_it_works()
