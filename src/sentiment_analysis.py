import pandas as pd
from textblob import TextBlob

def analyze_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return 'positivo'
    elif analysis.sentiment.polarity == 0:
        return 'neutro'
    else:
        return 'negativo'

def perform_sentiment_analysis(input_file, output_file):
    df = pd.read_csv(input_file)
    df['sentiment'] = df['text'].apply(analyze_sentiment)
    df.to_csv(output_file, index=False)
    print("Análise de sentimento concluída.")

if __name__ == "__main__":
    perform_sentiment_analysis('data/tweets_processados.csv', 'data/analise_sentimentos.csv')
