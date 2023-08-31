import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from AVL import AVLTree, Node 
from BST import BinaryTree
from autoCompletar import searchWordsStarting
from processText import process_text
import string
import time


nltk.download('punkt')
nltk.download('stopwords')

# Carrega o corpus a partir do arquivo
corpus_file = "corpus.txt"
with open(corpus_file, 'r', encoding='utf-8') as file:
    corpus = file.readlines()

preprocessed_corpus = []
my_list = [] 

unique_words = set()

preprocessed_text = process_text(corpus, unique_words)
    
avl_tree = AVLTree()

rootAVL = None

for word in unique_words:
    rootAVL = avl_tree.insert(rootAVL, word)


#imprimir corpus
#for idx, preprocessed_text in enumerate(preprocessed_corpus):
#    print(f"Texto {idx+1}: {preprocessed_text}")

#imprimir arvore
#avl_tree.printTree(rootAVL)

prefixo = input("Digite o prifixo a ser pesquisado: ")

prefixos = searchWordsStarting(rootAVL, prefixo)

print(f"Palavras comecando com '{prefixo}':")
for word in prefixos:
    print(word)



