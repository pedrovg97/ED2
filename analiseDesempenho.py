import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from AVL import AVLTree, Node 
from BST import BinaryTree
from processText import process_text
import time


nltk.download('punkt')
nltk.download('stopwords')

# Carrega o corpus a partir do arquivo
corpus_file = "corpus.txt"
with open(corpus_file, 'r', encoding='utf-8') as file:
    corpus = file.readlines()

corpusp_file = "corpus_pequeno.txt"
with open(corpusp_file, 'r', encoding='utf-8') as file:
    corpusp = file.readlines()

preprocessed_corpus = []
my_list = [] 

unique_words = set()
unique_words_aux = set()


preprocessed_text = process_text(corpus, unique_words)
preprocessed_text_aux = process_text(corpusp, unique_words_aux)



avl_tree = AVLTree()
bst_tree = BinaryTree()

rootAVL = None
rootBST = None

#################################Calcula tempo de inserção da AVL########################

start_time_AVL = time.perf_counter()

for word in sorted(unique_words):
    rootAVL = avl_tree.insert(rootAVL, word)

end_time_AVL = time.perf_counter()
insertion_time_AVL = end_time_AVL - start_time_AVL

###############################Calcula tempo de inserção da BST############################
start_time_BST = time.perf_counter()

for word in sorted(unique_words):
    rootBST = bst_tree.insert(rootBST, word)

end_time_BST = time.perf_counter()
insertion_time_BST = end_time_BST - start_time_BST
print("Insercao AVL x BST")
print(f"Tempo de insercao da AVL: '{insertion_time_AVL}'")
print(f"Tempo de insercao da BST: '{insertion_time_BST}'\n")

############################Calcula tempo de busca da AVL########################

start_time_serch_AVL = time.perf_counter()

serchAVL = avl_tree.search(rootAVL, "voyager")

end_time_serch_AVL = time.perf_counter()
search_time_AVL = end_time_serch_AVL - start_time_serch_AVL

#########################Calcula tempo de busca da BST##############################
start_time_serch_BST = time.perf_counter()

serchBST = bst_tree.search(rootBST, "voyager")

end_time_serch_BST = time.perf_counter()
search_time_BST = end_time_serch_BST - start_time_serch_BST

print("Busca AVLxBST")
print(f"Tempo de busca da AVL: '{search_time_AVL}'")
print(f"Tempo de busca da BST: '{search_time_BST}'\n")

###############################Comparando o desempenho da AVL para corpus grande e pequeno##########################
rootAVL = None

start_time_AVL_p = time.perf_counter()

for word in sorted(unique_words_aux):
    rootAVL = avl_tree.insert(rootAVL, word)

end_time_AVL_p = time.perf_counter()
insertion_time_AVL_p = end_time_AVL_p - start_time_AVL_p

print("Insercao corpus grande x corpus pequeno ")
print(f"Tempo de insercao da AVL para corpus pequeno: '{insertion_time_AVL_p}'")
print(f"Tempo de insercao da AVL para corpus grande: '{insertion_time_AVL}'\n")

############################Calcula tempo de busca da AVL para corpus pequeno########################

start_time_serch_AVL_p = time.perf_counter()

serchAVL = avl_tree.search(rootAVL, "trabalho")

end_time_serch_AVL_p = time.perf_counter()
search_time_AVL_p = end_time_serch_AVL_p - start_time_serch_AVL_p

print("Busca corpus grande x corpus pequeno ")
print(f"Tempo de busca da AVL para corpus pequeno: '{search_time_AVL_p}'")
print(f"Tempo de busca da AVL para corpus grande: '{search_time_AVL}'")



#print(sorted(unique_words))

#print(sorted(unique_words_aux))
