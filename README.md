# automacao-excel

Automação de mensagens para números inclusos em uma tabela.

O algoritmo procura o arquivo excel mencionado utilizando a biblioteca OpenPyXL, e vasculha cada linha, pegando o nome e o número das pessoas, e para cada linha envia uma mensagem que é buscada no arquivo de texto que contém a mensagem desejada.
Para o controle de fluxo, ele retorna o nome e o número da pessoa no terminal durante a execução, e também o
próprio PyWhatKit cria um arquivo de texto na pasta contendo o relatório com a data, hora, número e a mensagem que foi enviada.

Ainda não está pronto, estou aprendendo a utilizar essas bibliotecas e conforme o tempo estarei desenvolvendo melhorias.
