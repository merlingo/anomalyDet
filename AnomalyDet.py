
def EuclideanDistance(a,b):
    import math
    distance = math.sqrt(sum([(x-y)**2 for x,y in zip(a,b)]))
    print("Uzaklık: "+distance)
    return distance

def distanceBasedOutlierDetection(dataset, distfunc, dist_threshold, frac_threshold):
    '''
    detect anomaly based on distance
    :param dataset:
    :param dist_threshold:
    :param frac_threshold:
    :return:
    '''
    n=len(dataset)
    outlier = []

    for i in range(n):
        db = False
        count=0
        for j in range(n):
            dist = distfunc(dataset[j],dataset[i])
            if(j !=i and dist<dist_threshold):#eger i j degilse ve ideki jye yakin olan tum datasetin frac yuzdesinden cok eleman var mı
                count+=1
                if(count>=frac_threshold*n):
                    db=True
                    break #dataset[i] is not outlier
                    #endif
                #endif
            #endfor
        if(db):
            continue
        outlier.append(i)
    return outlier

def gridBasedOutlierDetection(dataset, distfunc, dist_threshold, frac_threshold):
    '''

    :param dataset:
    :param distfunc:
    :param dist_threshold:
    :param frac_threshold:
    :return:
    '''

if __name__ =="__main__":
    distanceBasedOutlierDetection([3,5,7,8,3435,234],EuclideanDistance,50,2)
