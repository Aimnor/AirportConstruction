import matplotlib.pyplot as plt
from math import sqrt

class Vertex:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def getDistanceFrom(self, other):
        return sqrt((other.x - self.x)**2 + (other.y - self.y)**2)

class NaiveStraightLine:
    def __init__(self, vl, vr) -> None:
        self.vl = vl
        self.vr = vr
        self.size = vl.getDistanceFrom(vr)

    def plotOn(self, ax, color = 'tab:red'):
        ax.plot([self.vl.x, self.vr.x], [self.vl.y, self.vr.y], color=color)

class StraightLine:
    def __init__(self, vl, vr) -> None:
        self.vl = vl
        self.vr = vr
        self.a = (vl.y - vr.y) / (vl.x - vr.x)
        self.b = (vl.y - self.a * vl.x)

    def plotOn(self, ax, color = 'tab:red'):
        ax.plot([self.vl.x, self.vr.x], [self.vl.y, self.vr.y], color=color)

def plotPolygon(ax, vertexes):
    xdata = [vertex.x for vertex in vertexes]
    xdata.append(vertexes[0].x)
    ydata = [vertex.y for vertex in vertexes]
    ydata.append(vertexes[0].y)
    ax.plot(xdata, ydata, color='tab:blue')

def getNaiveLongestStraightLine(input):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    verticesNmb = input[0]
    if (len(input) != verticesNmb*2+1):
        raise ValueError(f"must have an input of {verticesNmb*2+1} length but instead got {len(input)}")

    longestStraightLine = None
    vertexes = []

    for i in range(1,len(input),2):
        tempVertex = Vertex(input[i], input[i+1])
        for otherVertex in vertexes:
            tempStraightLine = NaiveStraightLine(tempVertex, otherVertex)
            tempStraightLine.plotOn(ax)

            if longestStraightLine is None:
                longestStraightLine = tempStraightLine
                continue

            if longestStraightLine.size < tempStraightLine.size:
                longestStraightLine = tempStraightLine

        vertexes.append(tempVertex)

    plotPolygon(ax, vertexes)
    longestStraightLine.plotOn(ax, color= 'tab:green')
    ax.text(longestStraightLine.vl.x, longestStraightLine.vl.y, longestStraightLine.size, color = '0')
    plt.show()

    return longestStraightLine.size

