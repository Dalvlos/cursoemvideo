frase = "Curso em Video Python"
print(frase.find("Video"))

#outros exemplos e anotacoes: ao inserir dados str em uma variavel esses dados sao alocados 
# caractere por caracteres em espacos na memoria, cada espaco na memoria reserveado a alocacao 
#dos caracteres recebe um indice que comeca em 0 ate o "infinito"


#fatiar uma str no python  frase=[9] ira exibir o decimo carctere
#frase[9:13] inicia a cadeia de caracteres do nono ao decimo segundo - essa funcao e chamada de range
#outro exemplo frase[9:21:2] da cadeia nove ate 20 pulando de dois em dois caracteres
#exemplo[:5] apos os dois pontos ":" a omissao da indicacao do cactere do inicio se iniciara do indice 0
#exemplo[15:] antes dos dois pontos ":" a omissao da indicado indice do caractere derradeiro seguira ao ultimo
#ex frase.count("o", 0, 13) da posicao 0 ate a posicao 13 ira indicar quantas vezes a letra o minusca aparece
#ex frase.find("deo") ira indicar a posicao de inicio de carctere indicado entre aspas.
# curso in frase - o "in" verificar se existe o primeiro parametro indicado dentro da variavel mencionada. retorna true ou false
# metodo replace ex: frase.replace("Python", "Android") muda a exibicao. 
#frase.upper() torna maiusculo letras minusculas
#frase.lower() modifica carcteres maiusculoes para minusculos
#frase.capitalize() transforma tudod em minusculos e apenas a primeira leitra de cada palavra em maiusculo.
#frase.title() altera a primeira letra de cada palavra observando os espacos
#frase.strip() remove espacos no inicio e no final da cadeia de caracteres
#frase.rstripe() remove os espacos no final da cadeia de caracteres
#frase.lstrip() remove espacos no inicio da cadeia de caracteres
#frase.split() divisao da str observando os espacos numa cadeia de caracteres (palavras e frases)
#ainda sobre o .split ira criar uma nova lista onde cada conjunto de caracteres sera uma str independente dentro de uma lista
#"-".join(frase) gera uma unica string separado por tracos, caso utilize espaco entre aspas a unica string gerada tera a divisao de palavras por espaco ao inves de tracos



