class Degree:
    pass

    def getDegree(self):
        print("I got a degree")


class UnderGraduate(Degree):
    def underGraduate(self):
        print("Undergraduate")


class PostGraduate(Degree):
    def postgraduate(self):
        print("PostGraduate")


UG = UnderGraduate()
UG.underGraduate()
PG = PostGraduate()
PG.postgraduate()
PG.getDegree()
