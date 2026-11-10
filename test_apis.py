
import backend_data as bd
import os
import sys
from dotenv import load_dotenv

load_dotenv()

def test_yfinance():
    print("--- Testando yfinance ---")
    data = bd.get_stock_data("AAPL", period="5d")
    if not data.empty:
        print("[OK] yfinance: Sucesso. Dados de AAPL obtidos.")
        print(data.head())
    else:
        print("[ERRO] yfinance: Falhou. Nenhum dado retornado.")
    print()

def test_newsapi():
    print("--- Testando NewsAPI ---")
    if not os.getenv("NEWS_API_KEY"):
        print("[ERRO] NewsAPI: Chave não configurada no .env.")
        return
    news = bd.get_news_sentiment("Apple Inc.")
    if news:
        print(f"[OK] NewsAPI: Sucesso. {len(news)} notícias obtidas.")
        for n in news[:2]:
            print(f"  - {n['title'][:60]}... ({n['sentiment']})")
    else:
        print("[ERRO] NewsAPI: Falhou. Nenhuma notícia retornada.")
    print()

def test_alpha_vantage():
    print("--- Testando Alpha Vantage ---")
    if not os.getenv("ALPHA_VANTAGE_API_KEY"):
        print("[ERRO] Alpha Vantage: Chave não configurada no .env.")
        return
    data = bd.get_daily_stock_data_alpha_vantage("IBM")
    if not data.empty:
        print("[OK] Alpha Vantage: Sucesso. Dados de IBM obtidos.")
        print(data.head())
    else:
        print("[ERRO] Alpha Vantage: Falhou. Nenhum dado retornado. Verifique limite de API.")
    print()

if __name__ == "__main__":
    print("Iniciando teste das APIs...\n")
    test_yfinance()
    test_newsapi()
    test_alpha_vantage()
    print("Testes concluídos.")
