import random
import string
from graph import Graph, Vertex


def get_words_from_text(text_path):
    with open(text_path, 'r') as f:
        text = f.read()

        text = ' '.join(text.split())  # Isto diz para transformar os espaços em branco em apenas espaços
        text = text.lower()  # Faz todas as palavras serem minúsculas
        # Agora é preciso ser mais complexo e lidar com as pontuações
        # Precisa adicionar um período como (Mr. Brightside), mas não realmente
        # pontuação, então simplismente remove todas as pontuações
        text = text.translate(str.maketrans('', '', string.punctuation))

    words = text.split()  # Separar por espaços de novo
    return words


def make_graph(words):
    g = Graph()

    previous_word = None

    # Para cada palavra
    for word in words:
        # Checar se a palavra está no gráfico, se não estiver adiciona
        words_vertex = g.get_vertex(word)

        # Se estiver a palavra prevista, então adiciona a borda se ainda não existe
        # no gráfico, então incrementa o peso em 1.
        if previous_word:
            previous_word.increment_edge(words_vertex)

        # E definir a palavra para a palavra anterior e iterar
        previous_word = words_vertex
    # O que quero é gerar a probabilidade mapeando antes de compor
    # Este é um bom lugar para fazer isto ante de retornar para o gráfico de objeto
    g.generate_probability_mappings()

    return g


def compose(g, words, length=50):
    composition = []
    word = g.get_vertex(random.choice(words))  # Pega uma palavra aleatória para iniciar
    for _ in range(length):
        composition.append(word.value)
        word = g.get_next_word(word)

    return composition


def main():
    # Passo 1: pegar as letras do texto
    words = get_words_from_text('texts/hp_sorcerer_stone.txt')

    # Passo 2: fazer o gráfico usando estas palavras
    g = make_graph(words)

    # Passo 3: Pegar a próxima palavra para os "Xs" números de palavras (Definido pelo usuário)

    # Passo 4: Mostrar o resultado para o usuário
    composition = compose(g, words, 100)
    print(' '.join(composition))  # Retorna a string onde todas as palavras são separadas por espaços


if __name__ == '__main__':
    main()
