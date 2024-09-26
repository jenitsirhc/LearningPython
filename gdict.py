class graph:

    def __init__(self,gdict=None):

        if gdict is None:

            gdict = {}

        self.gdict = gdict



    def edges(self):

        return self.findedges()



    def getVertices(self):

        return list(self.gdict.keys())



    def addVertex(self, vrtx):

        if vrtx not in self.gdict:

            self.gdict[vrtx] = []



    def AddEdge(self, edge):

        edge = set(edge)

        (vrtx1, vrtx2) = tuple(edge)

        if vrtx1 in self.gdict:

            self.gdict[vrtx1].append(vrtx2)

        else:

            self.gdict[vrtx1] = [vrtx2]



 



# List the edge names

    def findedges(self):

        edgename = []

        for vrtx in self.gdict:

            for nxtvrtx in self.gdict[vrtx]:

                if {nxtvrtx, vrtx} not in edgename:

                    edgename.append({vrtx, nxtvrtx})

        return edgename



  

        



        

# Create the dictionary with graph elements

graph_elements = {

"a" : ["b","c"],

"b" : ["a", "d"],

"c" : ["a", "d"],

"d" : ["e"],

"e" : ["d"]

}

g = graph(graph_elements)





g.AddEdge({'a','e'})

g.AddEdge({'a','c'})

g.addVertex("f")

g.addVertex("g")

g.AddEdge({'f','g'})

g.AddEdge({'d','g'})

g.AddEdge({'f','e'})

g.AddEdge({'a','f'})

print("Vertices are",g.getVertices())

print("Edges are", g.edges())

print("Removing Vertex")

g.removeVertex('a')

print("Final Graph")

print(g.gdict)