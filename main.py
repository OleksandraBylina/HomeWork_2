from Vector import Vector
def reader(file):
    vectors = []
    with open(file, 'r') as f:
        for line in f:
            try:
                data = line.split()
                data = list(data)
                vectors.append(Vector(data))
            except AssertionError:
                pass
        return vectors

        
def big_size(vectors):  # векторс - набор всех векторов, список списков
    pust = []
    doppust = [0]
    dopdoppust=[]
    for i in vectors:
        size1 = i.size()
        pust.append(size1)
    t = 1

    for i in pust:  # набор всех сайзов
        try:

            if pust[t] > doppust[0]:
                doppust.clear()
                doppust.append(pust[t])

                dopdoppust.clear()
                dopdoppust.append(t)

            elif pust[t] == pust[t - 1] and (pust[t]>max(pust) or (not doppust)):
                if vectors[t].size() >= vectors[t - 1].size():
                    doppust.append(pust[t - 1])
                    dopdoppust.append(t - 1)
                else:
                    doppust.append(pust[t])
                    dopdoppust.append(t)
            t = t + 1
        except IndexError:
            break
    for i in dopdoppust:
        res=i
    return (vectors[res])


def big_module(vectors):  # векторс - набор всех векторов, список списков
    pust = []
    doppust = [0]
    dopdoppust=[]
    for i in vectors:
        module1 = i.module()
        pust.append(module1)
    t = 1

    for i in pust:  # набор всех сайзов
        try:

            if pust[t] > doppust[0]:
                doppust.clear()
                doppust.append(pust[t])

                dopdoppust.clear()
                dopdoppust.append(t)

            elif pust[t] == pust[t - 1] and (pust[t]>max(pust) or (not doppust)):
                if vectors[t].module() >= vectors[t - 1].module():
                    doppust.append(pust[t - 1])
                    dopdoppust.append(t - 1)
                else:
                    doppust.append(pust[t])
                    dopdoppust.append(t)
            t = t + 1
        except IndexError:
            break
    for i in dopdoppust:
        res=i
    return (vectors[res])

def avarage_vector(vectors):
    ch=0
    chi=0
    for i in vectors:
        ch=ch+i.module()
        chi=chi+1
    return ch/chi
def more_than_avarage(vectors):
    pust=[]
    avarageVector = avarage_vector(vectors)
    for i in vectors:
        if i.module() > avarageVector:
            pust.append(i)
    return len(pust)
def maximal(vectors):
    pust=[]
    puster=[]

    t=0
    for i in vectors:

        maxx=max(i.vector)#ищет максимальное значение каждого вектора
        pust.append(int(maxx))
        puster.append(t)#содержит теперь набор всех индексов, полностью всех
        t=t+1
    for g in pust:
        try:
            if pust[g]>pust[g-1]:
                pust.remove(pust[g])
                puster.remove(puster[g])
            elif pust[g]==pust[g-1]:
                if min(vectors[g])<=min(vectors[g]):
                    pust.remove(pust[g-1])
                    puster.remove(puster[g-1])
                elif min(vectors[g-1])>min(vectors[g]):
                    pust.remove(pust[g])
                    puster.remove(puster[g])
        except IndexError:
            break
    for i in puster:
        a=i
    return vectors[a]
def minimal(vectors):
    pust=[]
    puster=[]

    t=0
    for i in vectors:

        maxx=min(i.vector)#ищет максимальное значение каждого вектора
        pust.append(int(maxx))
        puster.append(t)#содержит теперь набор всех индексов, полностью всех
        t=t+1
    for g in pust:
        try:
            if pust[g]>pust[g-1]:
                pust.remove(pust[g])
                puster.remove(puster[g])
            elif pust[g]==pust[g-1]:
                if max(vectors[g])>=max(vectors[g]):
                    pust.remove(pust[g-1])
                    puster.remove(puster[g-1])
                elif max(vectors[g-1])<max(vectors[g]):
                    pust.remove(pust[g])
                    puster.remove(puster[g])
        except IndexError:
            break
    for i in puster:
        a=i
    return vectors[a]
if __name__ == '__main__':
    for file in ("input01.txt", "input02.txt", "input03.txt", "input04.txt"):

        print(file, ":", "big_size")
        print(big_size((reader(file))))

        print(file, ":", "big_module")
        print(big_module((reader(file))))

        print(file, ":", "avarage_vector")
        print(avarage_vector((reader(file))))

        print(file, ":", "more_than_avarage")
        print(more_than_avarage((reader(file))))

        print(file, ":", "maximal")
        print(maximal((reader(file))))

        print(file, ":", "minimal")
        print(minimal((reader(file))))














