# Importando as bibliotecas necessárias
import requests
from tkinter import *

# Função para pegar as cotações das moedas
def pegar_cotacoes():
    try:
        # Fazendo a requisição para a API de cotações
        requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL,ARS-BRL")
        requisicao.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        print ("Erro HTTP:", errh)
    except requests.exceptions.ConnectionError as errc:
        print ("Erro de Conexão:", errc)
    except requests.exceptions.Timeout as errt:
        print ("Timeout:", errt)
    except requests.exceptions.RequestException as err:
        print ("Erro:", err)
    else:
        # Retorna o JSON da resposta da requisição
        return requisicao.json()

# Função para formatar as cotações e atualizar o texto na interface gráfica
def formatar_cotacoes(cotacoes):
    # Pegando as cotações do JSON e convertendo para float
    cotacao_dolar = float(cotacoes['USDBRL']['bid'])
    cotacao_euro = float(cotacoes['EURBRL']['bid'])
    cotacao_peso = float(cotacoes['ARSBRL']['bid'])
    cotacao_btc = float(cotacoes['BTCBRL']['bid'])

    # Formatando o texto com as cotações
    texto = f'''
    Dólar:          R$ {cotacao_dolar:.2f}
    Euro:           R$ {cotacao_euro:.2f}
    Peso Arg:       R$ {cotacao_peso:.2f}
    BTC:            R$ {cotacao_btc:.2f}'''

    # Atualizando o texto do widget de cotações
    texto_cotacoes["text"] = texto

# Criando a janela da aplicação
janela = Tk()
janela.title("Cotação Atual das Moedas")

# Definindo as cores
cor_letras = "#ffffff"
cor_fundo = "#233642"

# Configurando a cor de fundo da janela
janela.config(bg=cor_fundo)

# Criando e posicionando os widgets na janela
texto_orientacao = Label(janela, text="Clique no botão para ver as cotações das moedas", bg=cor_fundo, fg=cor_letras)
texto_orientacao.grid(column=0, row=0, padx=10, pady=10)

texto_cotacoes = Label(janela, text="", bg=cor_fundo, fg=cor_letras)
texto_cotacoes.grid(column=0, row=1, padx=10, pady=10)

texto_desenvolvedor = Label(janela, text="Web Developer: Douglas Pinto Do Nascimento", bg=cor_fundo, fg=cor_letras)
texto_desenvolvedor.grid(column=0, row=3)

# Função principal que será executada quando o botão for pressionado
def main():
    cotacoes = pegar_cotacoes()
    if cotacoes:
        formatar_cotacoes(cotacoes)

# Criando o botão e associando a função main ao evento de clique
botao = Button(janela, text="Buscar cotações Dólar/Euro/Peso Argentino/BTC", command=main, bg=cor_fundo, fg=cor_letras)
botao.grid(column=0, row=2, padx=10, pady=10)

# Iniciando a aplicação
if __name__ == "__main__":
    main()

# Iniciando o loop da interface gráfica
janela.mainloop()
