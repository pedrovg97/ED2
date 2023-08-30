import sys
import os

# Add the project directory to the Python path
project_path = r'C:\Users\pedro\OneDrive\Documentos\Projetos\Auto_Completa'
sys.path.append(project_path)

# Now you can import the module directly

from autoCompletar import searchWordsStarting
from AVL import AVLTree, Node 
from processText import process_text

corpus = [
"Na vastidão do cosmos, estrelas brilham, dançando uma órbita celeste, enquanto planetas continuam traçando suas histórias cósmicas pelo infinito universo."
]
unique_words = set()

process_text(corpus, unique_words)
    
avl_tree = AVLTree()

root = None
for word in unique_words:
    root = avl_tree.insert(root, word)

def test_autoCopleta_empty_tree():
    root = None
    prefixos = searchWordsStarting(root, "test")
    result = prefixos
    assert result == []

def test_autoCopleta_prefix_not_found():
    prefixos = searchWordsStarting(root, "z")
    result = prefixos
    assert result == []

def test_autoCopleta_prefix_c():
    prefixos = searchWordsStarting(root, "c")
    result = prefixos
    assert set(result) == set(['cosmos', 'celeste', 'continuam', 'cosmicas']) 

def test_autoCopleta_prefix_p():
    prefixos = searchWordsStarting(root, "p")
    result = prefixos
    assert result == ["planetas"]
