# Dashboard Profesional de Análisis de Acciones

Dashboard MVP de análisis de mercado accionario utilizando Python, Streamlit, y APIs financieras (yfinance, NewsAPI, Alpha Vantage).

## 🚀 Despliegue en la Nube (Streamlit Cloud)

Como el dashboard requiere un servidor Python para funcionar, el alojamiento recomendado es **Streamlit Community Cloud** (gratuito y nativo):

1. **GitHub:** Sube tu proyecto a un repositorio público en GitHub.
2. **Conexión:** Entra en [share.streamlit.io](https://share.streamlit.io/).
3. **Deploy:** Conecta tu repositorio de GitHub, selecciona el archivo `app.py` y despliega.
4. **Secrets:** En la configuración del despliegue en Streamlit Cloud, añade tus claves API:
   - `NEWS_API_KEY`
   - `ALPHA_VANTAGE_API_KEY`

## 🌐 ¿Quieres usar Netlify? (Redirección)
Si necesitas que el dashboard tenga una URL en Netlify, puedes crear un sitio estático con un archivo `index.html` que redirija automáticamente a tu URL de Streamlit Cloud.

Crea un archivo `index.html` en tu carpeta:
```html
<!DOCTYPE html>
<html>
  <head>
    <meta http-equiv="refresh" content="0; url='TU_URL_DE_STREAMLIT_AQUI'" />
  </head>
  <body></body>
</html>
```

## 🛠️ Requisitos
- Python 3.12+
- `pip install -r requirements.txt`

## 🔑 Configuración
Crea un archivo `.env` en la raíz basado en `.env.example` con tus claves API válidas.
