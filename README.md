
# Projeto de Identificação de Intolerância Religiosa no Twitter

Este projeto visa identificar casos de intolerância religiosa no Brasil utilizando dados de postagens coletadas da rede social Twitter. Ele faz uso de técnicas de análise de sentimentos e processamento de linguagem natural para processar e analisar os tweets, gerando relatórios de possíveis casos de intolerância religiosa.

## Estrutura do Projeto

```
/analise-casos-intolerancia-religiosa/
│
├── src/
│   ├── collect_data.py               # Coleta de dados do Twitter
│   ├── preprocess_data.py            # Pré-processamento dos tweets coletados
│   ├── sentiment_analysis.py         # Análise de sentimentos nos tweets
│   ├── report_generation.py          # Geração de relatórios com os resultados
│
├── config/
│   └── config.py                     # Arquivo de configuração para credenciais da API
│
├── data/
│   ├── raw_tweets.json               # Arquivo gerado após a coleta
│   ├── processed_tweets.csv          # Arquivo gerado após o processamento
│   └── sentiment_analysis.csv        # Arquivo gerado após a análise de sentimentos
│
├── main.py                           # Arquivo principal para execução do projeto
├── requirements.txt                  # Lista de dependências
└── README.md                         # Instruções do projeto
```

## Dependências

Antes de iniciar o projeto, certifique-se de instalar as dependências necessárias. Você pode fazer isso usando o `pip` com o comando:

```bash
pip install -r requirements.txt
```

### Dependências principais:

- `tweepy` - Para coletar dados da API do Twitter
- `pandas` - Para manipulação e análise de dados
- `nltk` - Para processamento de linguagem natural
- `textblob` - Para análise de sentimento
- `matplotlib` - Para geração de gráficos
- `requests` - Para fazer requisições à API
- `dotenv` - Para gerenciar variáveis de ambiente (opcional)

## Configuração da API do Twitter

1. **Obter as Credenciais da API do Twitter**:
   - Vá até o [Twitter Developer](https://developer.twitter.com/) e crie um App.
   - Obtenha as seguintes credenciais:
     - `API Key`
     - `API Key Secret`
     - `Access Token`
     - `Access Token Secret`

2. **Configuração das Credenciais**:
   - Insira as credenciais no arquivo `config/config.py`:

```python
# config/config.py

API_KEY = 'sua-api-key'
API_SECRET_KEY = 'sua-api-secret-key'
ACCESS_TOKEN = 'seu-access-token'
ACCESS_TOKEN_SECRET = 'seu-access-token-secret'
```

## Execução do Projeto

1. **Coletar Tweets**:
   No arquivo `main.py`, o método `collect_data()` coleta tweets relacionados à intolerância religiosa no Brasil, utilizando a API do Twitter.

   Para iniciar a coleta de dados, execute:

   ```bash
   python main.py
   ```

2. **Pré-processar os Dados**:
   Após a coleta, o arquivo `preprocess_data.py` remove ruídos dos tweets (como emojis, URLs, etc.) e normaliza os dados.

3. **Análise de Sentimento**:
   O arquivo `sentiment_analysis.py` faz a análise de sentimentos dos tweets coletados, utilizando a biblioteca `TextBlob`.

4. **Geração de Relatório**:
   O arquivo `report_generation.py` cria relatórios e gráficos para visualização dos resultados.

## Resultados Esperados

- **Gráficos**: A análise de sentimentos pode gerar gráficos como nuvens de palavras ou gráficos de barras, destacando o número de tweets positivos, negativos e neutros.
- **Relatórios**: O relatório final fornecerá informações sobre a frequência de posts relacionados à intolerância religiosa e seus sentimentos associados.

## Licença

Este projeto é de código aberto e está disponível sob a licença MIT.
