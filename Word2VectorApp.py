import gensim
from gensim.corpora import WikiCorpus
import os
import random
'''
1- get corpus
1.2- train word2vec models to get vectors
2- select some keywords about same topic as dataset
3- select some anomaly words which have no interest with topic to insert dataset
4- return dataset - word and vektor
'''
keywords = ["bilgisayar","c++","java","sistematik","insan-bilgisayar","komputer","computer","programlama","windows",
            "işlem","hesaplama","incelemek",
            "algoritmalar","program","yazılım","ağı","veritabanı","sistemleri","paralel","dağıtık",
            "etkileşimi", "işletim","sistemi","teorik","bilimi","matematiksel","kodlama","teorisi","veri","yapıları",
            "assembly","analizi","işlediğimiz","cihaz","dizüstü","masaüstü","bayt","ikili","sayılar","bit","rastgele",
            "erişimli","bellek"]
anomaly=["tarih","türk","atsız","kubilay","cengiz"]
def getCorpus():
    # parse an xml file by name
    wiki = WikiCorpus("trwiki-20181201-pages-articles-multistream.xml.bz2", lemmatize=False, dictionary={})
    space = " "
    i = 0
    corpus = [text for text in wiki.get_texts()]
    print("Finished Saved " + str(len(corpus)) + " articles")
    return  corpus
def modeling(doc):
    model = gensim.models.Word2Vec(doc, size=150, window=10, min_count=2, workers=10)
    return model
def dataset(keyws, model):
    dataset = []
    for k in keyws:
        dataset.append(list(model[k.lower()]))
    return dataset
def app(outfile="model.txt"):
    model = {}
    global anomaly
    if not(os.path.isfile(outfile) ):
        print("model is not exist, it will be produced")
        corpus = getCorpus()
        model = modeling(corpus)
        # trim unneeded model memory = use (much) less RAM
        model.init_sims(replace=True)
        model.save(outfile)
    else:
        print("model is exist, it will load from file")
        model = gensim.models.Word2Vec.load(outfile)

    words = list(model.wv.vocab)
    lw =len(words)
    print(lw)
    #print("\n"+str(words[:100]))
    keyws = checkKeywords(words)
    for k in anomaly:
        if (k in words):
            keyws.append(k)
        else:
            print("bu anomaly yok:"+k)
    dset = dataset(keyws,model)
    return dset,keyws

def checkKeywords(words):
    global keywords
    kw= []
    for k in keywords:
        if(k in words):
            kw.append(k)
        else:
            print("bu kelime yok:"+k)
    return kw
if __name__=="__main__":
    print(app())