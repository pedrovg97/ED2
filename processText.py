import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
from unidecode import unidecode


# Carregue as palavras de parada em português
stop_words = set(stopwords.words('portuguese'))
preprocessed_corpus = []

def preprocess_text(text):
    # Converte o texto para minúsculas
    text = text.lower()
    
    # Remove pontuação e caracteres especiais
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Remove acentos
    text = unidecode(text) 

    # Tokeniza o texto em palavras
    words = word_tokenize(text)
    
    # Remove palavras de parada
    filtered_words = [word for word in words if word not in stop_words]

    return filtered_words

def process_text(corpus, unique_words):
    for text in corpus:
        processed_text = preprocess_text(text)
        preprocessed_corpus.append(processed_text)
        unique_words.update(processed_text)

        return processed_text