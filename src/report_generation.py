import pandas as pd
import matplotlib.pyplot as plt

def generate_report(input_file):
    df = pd.read_csv(input_file)
    sentiment_counts = df['sentiment'].value_counts()

    plt.figure(figsize=(8,6))
    plt.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', startangle=90)
    plt.title('Distribuição de Sentimentos sobre Intolerância Religiosa no Twitter')
    plt.show()

if __name__ == "__main__":
    generate_report('data/analise_sentimentos.csv')
