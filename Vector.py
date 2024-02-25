class Vector:
    class Vector:
        origin = [0, 0]

        def __init__(self, vector=list):
            if isinstance(vector, Vector):
                self.vector = vector.vector
            else:
                assert len(vector) > 0
                self.vector = vector
    def size(self):
        return len(self.vector)
    def module(self):

        newlist=[]
        for i in self.vector:
            q=int(i)**2
            newlist.append(q)
        v=0
        for t in newlist:
            v=v+t
        return v**0.5
    def avarage(self):
        r=0
        t=0
        for i in self.vector:
            r=r+i
            t=t+1
        return r/t
    def maximum(self):
        return max(self.vector)
    def minimumm(self):
        return min(self.vector)

    def __str__(self):
        coordinates = list(map(float, self.vector))
        return f"Vector {coordinates}"





