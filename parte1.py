import pandas as pd
from datetime import datetime
import gtts
from playsound import playsound
from random import randint
import time

planilha_df = pd.read_excel('C:/Users/Bruno/Desktop/Bruno/Rotina/geral.xlsx')
print(planilha_df)

class Rotina():

    def __init__(self):

        self.receber_nulo = str()
        self.local = str()
        self.treinou = str()
        self.provisorio = list()
        self.armazenar = dict()
        self.armazenar_provisorio = dict()
        self.armazenar_habitos = []
        self.contador = 0
        self.nomes_habitos = list()
        self.data_hoje = datetime.today().strftime('%d/%m/%Y')

    def evolucao_habitos(self):

        with open('melhorando.txt', 'r') as arquivo:
            arquivo = arquivo.readlines()
            for arq in arquivo:
                if self.contador == 0:
                    self.receber_nulo = arq
                else:
                    self.provisorio.append(arq)
                self.contador += 1
                if arq == '\n':
                    self.nomes_habitos.append(self.receber_nulo)
                    self.armazenar_provisorio = {self.receber_nulo: self.provisorio}
                    self.contador = 0
                    self.armazenar_habitos.append(self.armazenar_provisorio)
                    self.armazenar_provisorio = {} #olhar, pois é diferente de .clear()
                    self.provisorio = [] #olhar, pois é diferente de .clear()

            return self.armazenar_habitos, self.nomes_habitos

    def tarefa_atual(self, dia_semana, horario_atual):

        return planilha_df.loc[horario_atual - 1, dia_semana]  # bug se for meia noite

class Alarmes():

    def __init__(self):
        pass

    def audio_google_motivacao(self, cont):
        with open('atencao.txt', 'r') as arquivo:
            arquivo = arquivo.readlines()
            audio_sorteado = randint(0, len(arquivo))
            frase = gtts.gTTS(arquivo[audio_sorteado], lang='pt-br')
            frase.save(f'frase{cont}.mp3')
            playsound(f'frase{cont}.mp3')

    def tarefa_alerta(self, tarefa_agora, cont):

        frase = gtts.gTTS(tarefa_agora, lang='pt-br')
        frase.save(f'tarefa{cont}.mp3')
        playsound(f'tarefa{cont}.mp3')

def ler_planilha():
    pass

def gerar_planilha():
    pass

def main():

    lista_habitos = list()
    dia_semana_num = datetime.today().weekday()
    dia_semana_texto = ('SEGUNDA', 'TERÇA', 'QUARTA', 'QUINTA', 'SEXTA', 'SABADO', 'DOMINGO')
    dia_semana = dia_semana_texto[dia_semana_num]
    horario_atual = int(datetime.now().strftime('%H'))

    rotina = Rotina()
    rotina.evolucao_habitos()

    alarmes = Alarmes()
    tarefa_agora = rotina.tarefa_atual(dia_semana, horario_atual)

    habitos = rotina.evolucao_habitos()
    print(habitos[1])
    #alarmes.tarefa_alerta(f'A tarefa de agora é de {tarefa_agora}.')
    cont = 0

    while True:

        comandos = ''

        cont += 1
        time.sleep(30)
        print('Ligado..')
        datetime_minute = int(datetime.now().strftime('%M'))
        print(datetime_minute)

        if datetime_minute == 0:
            alarmes.tarefa_alerta(f'A tarefa de agora é de {tarefa_agora}.', cont )
            time.sleep(60)
        elif datetime_minute == randint(1, 59):
            alarmes.audio_google_motivacao(cont)
        elif datetime_minute == randint(1, 59):
            alarmes.audio_google_motivacao(cont)
        elif datetime_minute == randint(1, 59):
            alarmes.audio_google_motivacao(cont)
        elif datetime_minute == randint(1, 59):
            alarmes.audio_google_motivacao(cont)
        elif datetime_minute == randint(1, 59):
            alarmes.audio_google_motivacao(cont)
        cont += 1

main()