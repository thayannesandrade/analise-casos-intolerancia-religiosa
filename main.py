from src.collect_data import collect_tweets
from src.preprocess_data import preprocess_tweets
from src.sentiment_analysis import perform_sentiment_analysis
from src.report_generation import generate_report

if __name__ == "__main__":
    collect_tweets("#intoleranciareligiosa OR #racismoreligioso")
    preprocess_tweets('data/raw_tweets.json', 'data/twetts_processados.csv')
    
    perform_sentiment_analysis('data/twetts_processados.csv', 'data/sentiment_analysis.csv')
    
    generate_report('data/analise_sentimentos.csv')
