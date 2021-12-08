import pandas as pd
from gensim.models import Word2Vec

an = pd.read_csv("./anime.csv")
model = Word2Vec.load("./rating_structure.model")

def showSimilar(id):
    print((an[an["MAL_ID"] == int(id)])["Japanese name"].values)

    for a in model.wv.similar_by_word(str(id)):
        print((an[an["MAL_ID"] == int(a[0])])["Japanese name"].values, a)