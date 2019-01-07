import tsne
import numpy as np
import matplotlib.pylab as pylab
import Word2VectorApp as w2v
import AnomalyDet as anomaly
def getWordAndVectors():
    # Create	a	dataset	where	each	tuple	will	be	word2vec	vector	of	a	word.
    dataset = []
    dfn = "word2vec.txt"
    a = 0
    words = []
    with open(dfn, "r") as f:
        for l in f:
            a += 1
            wv = l.split(" ")
            wv[-1] = wv[-1].replace("\n", "")

            if (a == 1):
                continue
    return dataset,words
def EuclideanDistance(a,b):
    import math
    distance = math.sqrt(sum([(x-y)**2 for x,y in zip(a,b)]))
    #print("Uzaklık: "+str(distance))
    return distance
def printoutliers(outlier,words):
    print(str(len(outlier))+" kadar outlier vardır:")
    o = [words[i] for i in outlier]
    print(o)

def __main():
    #Create	a	dataset	where	each	tuple	will	be	word2vec	vector	of	a	word.
    dataset, words = w2v.app()
    X =np.array(dataset).astype(np.float)
    print(X)

    #Apply	an	anomoly	detection	technique
    outlier = anomaly.distanceBasedOutlierDetection(X,EuclideanDistance,1,0.2)
    print("1.0 icin outliers:")
    printoutliers(outlier,words)

    outlier = anomaly.distanceBasedOutlierDetection(X, EuclideanDistance, 1.1, 0.3)
    print("1.2 icin outliers:")
    printoutliers(outlier,words)
    outlier = anomaly.distanceBasedOutlierDetection(X, EuclideanDistance, 1.2, 0.3)
    print("1.2 icin outliers:")
    printoutliers(outlier, words)
    outlier = anomaly.distanceBasedOutlierDetection(X, EuclideanDistance, 1.3, 0.3)
    print("1.3 icin outliers:")
    printoutliers(outlier, words)
    outlier = anomaly.distanceBasedOutlierDetection(X, EuclideanDistance, 1.5, 0.4)
    print("1.5 icin outliers:")
    printoutliers(outlier,words)
    #Show	the	string	of	words	on	the	TSNE	visualization
    Y = tsne.tsne(X, 2, 50, 20.0)
    pylab.scatter(Y[:, 0], Y[:, 1])
    for i, word in enumerate(words):
        pylab.annotate(word, xy=(Y[i, 0], Y[i, 1]))
    pylab.show()
if __name__ == "__main__":
    __main()