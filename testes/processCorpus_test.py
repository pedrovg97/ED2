import sys
import os

# Add the project directory to the Python path
project_path = r'C:\Users\pedro\OneDrive\Documentos\Projetos\Auto_Completa'
sys.path.append(project_path)

# Now you can import the module directly

from autoCompletar import searchWordsStarting
from AVL import AVLTree, Node 
from processText import process_text

unique_words = set()

corpus= ["O café é uma bebida deliciosa e açaí é uma fruta típica do Brasil, mas às vezes a vida nos traz desafios difíceis de enfrentar!"]

def test_processCorpus_empty_corpus():
    corpus = []
    result = process_text(corpus, unique_words)
    assert result == None

def test_processCorpus_not_process_corpus():
    result = process_text(corpus, unique_words)
    assert result != ["O café é uma bebida deliciosa e açaí é uma fruta típica do Brasil, mas às vezes a vida nos traz desafios difíceis de enfrentar!"]
    
def test_processCorpus_invalid_corpus():
    result = process_text(corpus, unique_words)
    assert result != ["café", "bebida", "deliciosa", "açaí", "fruta", "típica", "Brasil", "vezes", "vida","traz", "desafios", "difíceis", "enfrentar"]

def test_processCorpus_valid_corpus():
    result = process_text(corpus, unique_words)
    assert result == ["cafe", "bebida", "deliciosa", "acai", "fruta", "tipica", "brasil", "vezes", "vida","traz", "desafios", "dificeis", "enfrentar"]