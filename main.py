import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from AVL import AVLTree, Node 
from autoCompletar import searchWordsStarting
import string

nltk.download('punkt')
nltk.download('stopwords')

# Carregue as palavras de parada em português
stop_words = set(stopwords.words('portuguese'))

def preprocess_text(text):
    # Converte o texto para minúsculas
    text = text.lower()
    
    # Remove pontuação e caracteres especiais
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Tokeniza o texto em palavras
    words = word_tokenize(text)
    
    # Remove palavras de parada
    filtered_words = [word for word in words if word not in stop_words]
    
    return filtered_words

# Carrega o corpus a partir do arquivo
corpus_file = "corpus.txt"
with open(corpus_file, 'r', encoding='utf-8') as file:
    corpus = file.readlines()

preprocessed_corpus = []
unique_words = set()
for text in corpus:
    preprocessed_text = preprocess_text(text)
    preprocessed_corpus.append(preprocessed_text)
    unique_words.update(preprocessed_text)
 
    
avl_tree = AVLTree()

root = None
for word in unique_words:
    root = avl_tree.insert(root, word)

#imprimir corpus
#for idx, preprocessed_text in enumerate(preprocessed_corpus):
#    print(f"Texto {idx+1}: {preprocessed_text}")

#imprimir arvore
#vl_tree.printTree(root)

prefixo = input("Digite o prifixo a ser pesquisado: ")

prefixos = searchWordsStarting(root, prefixo)

print(f"Palavras comecando com '{prefixo}':")
for word in prefixos:
    print(word)



