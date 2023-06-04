import os
import tweepy
import matplotlib.pyplot as plt

from textblob import TextBlob


class AnaliseSentimentos:
    def __init__(self):
        # Obter as chaves de acesso
        __consumer_key = 'aaa'
        __consumer_secret = 'bbb'
        __access_token = 'ccc'
        __access_token_secret = 'ddd'

        # Autenticar-se na API do Twitter
        auth = tweepy.OAuthHandler(__consumer_key, __consumer_secret)
        auth.set_access_token(__access_token, __access_token_secret)
        self.api = tweepy.API(auth)

        self.palavras_boas = [
            'bom', 'ótimo', 'excelente', 'positivo', 'progresso', 'avanço',
            'eficiente', 'honesto', 'transparente', 'responsável', 'inovador',
            'sensato', 'correto', 'eficaz', 'justo', 'dedicado', 'competente',
            'sincero', 'confiável', 'solidário', 'harmonioso', 'diplomático',
            'progressista', 'integro', 'prestativo', 'colaborativo', 'liderança',
            'qualidade', 'tolerante', 'respeito', 'esperança', 'cuidadoso',
            'exemplar', 'resiliente', 'paciente', 'equilibrado', 'realização',
            'proativo', 'criativo', 'altruísta', 'visionário', 'gratidão',
            'sabedoria', 'motivado', 'comprometido', 'empreendedor', 'valente',
            'harmonia', 'solução', 'celebrar', 'gentileza', 'humanidade',
            'entusiasmo', 'cooperar', 'incentivar', 'generosidade', 'solidariedade',
            'confiança', 'amizade', 'felicidade', 'inspiração', 'paz',
            'inclusão', 'justiça', 'verdade', 'esperança', 'liderança',
            'coragem', 'respeito', 'honestidade', 'empatia', 'compaixão',
            'colaboração', 'integridade', 'altruísmo', 'excelência', 'progresso',
            'transformação', 'equidade', 'diálogo', 'sustentabilidade', 'cidadania',
            'inovação', 'criatividade', 'desenvolvimento', 'responsabilidade', 'solidariedade',
            'igualdade', 'liberdade', 'resiliência', 'gratidão', 'harmonia'
        ]

        self.palavras_ruins = [
            'ruim', 'péssimo', 'terrível', 'negativo', 'corrupção', 'escândalo',
            'incompetente', 'desonesto', 'opressor', 'mentiroso', 'ineficiente',
            'conflito', 'irresponsável', 'injusto', 'culpado', 'violência',
            'desigualdade', 'enganoso', 'instabilidade', 'indiferente', 'preconceito',
            'caos', 'impunidade', 'incompetência', 'desigual', 'abuso',
            'exclusão', 'tirano', 'arrogante', 'insensível', 'traição',
            'fraude', 'negligente', 'cruel', 'violento', 'desonestidade',
            'desvalorização', 'despreparado', 'enganador', 'opressão', 'falha',
            'intransigente', 'improdutivo', 'desrespeito', 'insegurança', 'destrutivo',
            'corrupto', 'impaciência', 'retrógrado', 'irracional', 'péssimo', 'safado', 'genocida', 'canalha',
            'burro', 'ladrão', 'misógino', 'homofóbico', 'racista']

    def buscaTweets(self, frase, quantidade):
        # Termo de busca
        self.frase = frase

        # Realizar a busca de tweets no Twitter
        tweets = self.api.search_tweets(self.frase, count=quantidade)
        # Contadores para os sentimentos
        self.positive_count = 0
        self.negative_count = 0

        # Analisar o sentimento de cada tweet
        sentiments = []
        for tweet in tweets:
            analysis = TextBlob(tweet.text)
            sentiment = analysis.sentiment.polarity
            sentiments.append(sentiment)

            for palavra in self.palavras_boas:
                if palavra in tweet.text.lower():
                    self.positive_count += 1
            
            for palavra in self.palavras_ruins:
                if palavra in tweet.text.lower():
                    self.negative_count += 1
            
        self.tweets_neutros = len(tweets) - self.positive_count - self.negative_count
        # Imprimir os resultados
        print(f"Total de tweets analisados: {len(tweets)}")
        print(f"Total de tweets positivos: {self.positive_count}")
        print(f"Total de tweets negativos: {self.negative_count}")
        print(f"Total de tweets neutros: {len(tweets) - self.positive_count - self.negative_count}")

    def plotBarh(self):
        # Plotar o gráfico de barras
        sentiments = ['Positivos', 'Negativos', 'Neutros']
        colors = ['green', 'red', 'blue']
        counts = [self.positive_count, self.negative_count, self.tweets_neutros]

        plt.barh(sentiments, counts, color=colors)
        plt.xlabel('Quantidade')
        plt.title(f'Tweets relacionados à palavra "{self.frase}"')
        plt.show()

