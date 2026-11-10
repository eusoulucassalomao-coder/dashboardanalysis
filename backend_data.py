
import yfinance as yf
import pandas as pd
import requests
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Baixa o léxico do VADER se ainda não estiver disponível
try:
    nltk.data.find('sentiment/vader_lexicon')
except LookupError:
    nltk.download('vader_lexicon')

# API Keys (pegar do .env)
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
ALPHA_VANTAGE_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")

def get_stock_data(ticker, period="1y"):
    """
    Coleta dados históricos de uma ação usando yfinance.
    Retorna um DataFrame do Pandas.
    """
    try:
        stock = yf.Ticker(ticker)
        hist = stock.history(period=period)
        return hist
    except Exception as e:
        print(f"Erro ao obter dados de {ticker} com yfinance: {e}")
        return pd.DataFrame()

def get_news_sentiment(query):
    """
    Coleta notícias usando NewsAPI e realiza análise de sentimento com VADER.
    Retorna uma lista de dicionários com notícia e sentimento.
    """
    if not NEWS_API_KEY:
        print("NEWS_API_KEY não configurada no .env. Pulando busca de notícias.")
        return []

    url = f"https://newsapi.org/v2/everything?q={query}&language=en&sortBy=relevancy&apiKey={NEWS_API_KEY}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Levanta erro para status HTTP ruins
        articles = response.json().get('articles', [])

        sid = SentimentIntensityAnalyzer()
        news_with_sentiment = []
        for article in articles[:5]: # Limita a 5 notícias para MVP
            title = article.get('title')
            source = article.get('source', {}).get('name')
            url = article.get('url')

            if title:
                ss = sid.polarity_scores(title)
                compound_score = ss['compound']

                sentiment = "Neutro"
                if compound_score >= 0.05:
                    sentiment = "Positivo"
                elif compound_score <= -0.05:
                    sentiment = "Negativo"

                news_with_sentiment.append({
                    "title": title,
                    "source": source,
                    "url": url,
                    "sentiment": sentiment,
                    "compound_score": compound_score
                })
        return news_with_sentiment
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição à NewsAPI: {e}")
        return []
    except Exception as e:
        print(f"Erro ao processar notícias: {e}")
        return []

def get_daily_stock_data_alpha_vantage(ticker):
    """
    Coleta dados diários de uma ação usando Alpha Vantage.
    Retorna um DataFrame do Pandas.
    Limitação: 25 requisições/dia no plano gratuito.
    """
    if not ALPHA_VANTAGE_API_KEY:
        print("ALPHA_VANTAGE_API_KEY não configurada no .env. Pulando Alpha Vantage.")
        return pd.DataFrame()

    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&apikey={ALPHA_VANTAGE_API_KEY}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if "Time Series (Daily)" not in data:
            print(f"Erro ou limite de API atingido para Alpha Vantage em {ticker}: {data.get('Note', 'Dados não encontrados.')}")
            return pd.DataFrame()

        df = pd.DataFrame.from_dict(data["Time Series (Daily)"], orient="index")
        df = df.astype(float)
        df.index = pd.to_datetime(df.index)
        df.columns = ['Open', 'High', 'Low', 'Close', 'Volume'] # Renomear para consistência
        df = df.sort_index()
        return df
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição à Alpha Vantage: {e}")
        return pd.DataFrame()
    except Exception as e:
        print(f"Erro ao processar dados da Alpha Vantage: {e}")
        return pd.DataFrame()

# Exemplo de uso (apenas para testar o módulo)
if __name__ == "__main__":
    # Para testar, crie um arquivo .env na mesma pasta com:
    # NEWS_API_KEY="SUA_CHAVE_NEWSAPI"
    # ALPHA_VANTAGE_API_KEY="SUA_CHAVE_ALPHAVANTAGE"

    print("--- Testando yfinance ---")
    stock_yf = get_stock_data("AAPL")
    if not stock_yf.empty:
        print(stock_yf.head())

    print("")

    print("--- Testando NewsAPI ---")
    news = get_news_sentiment("Apple Inc.")
    if news:
        for n in news:
            print(f"Título: {n['title']}\nSentimento: {n['sentiment']} ({n['compound_score']})\nFonte: {n['source']}\n")

    print("")

    print("--- Testando Alpha Vantage ---")
    stock_av = get_daily_stock_data_alpha_vantage("IBM")
    if not stock_av.empty:
        print(stock_av.head())
