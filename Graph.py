class BipartiteGraph:
    def __init__(self):

        self.N = list() 
        self.V = list() 
        self.adj_list = {} 

    def add_vertex(self, vertex, set_type):

        if set_type == 'N':
            self.N.append(vertex)
        elif set_type == 'V':
            self.V.append(vertex)
        else:
            raise ValueError("set_type must be either 'N' or 'V'")      
        
    def IHashmap(self):
        TempList = []
        for noun in range(len(self.N)):
            for verb in range(len(self.V)):
                self.adj_list.update({self.N[noun]+self.V[verb]: False})

    def add_edge(self, n, v):
        self.adj_list.update({n+v: True})

    def display(self):
        print("Set N:", self.N)
        print("Set V:", self.V)
        print("Adjacency List:")
        for vertex in self.adj_list.items():
            print(vertex)


    def makeGraph(self):
        
        self.add_vertex('19', 'N')
        self.add_vertex('17', 'N')
        self.add_vertex('01', 'V')
        self.add_vertex('02', 'V')
        self.add_vertex('03', 'V')
        self.add_vertex('04', 'V')
        self.add_vertex('05', 'V')
        self.add_vertex('06', 'V')
        self.add_vertex('84', 'V')
        self.add_vertex('76', 'V')

        self.IHashmap()

        self.add_edge('19', '01')
        self.add_edge('19', '02')
        self.add_edge('19', '03')
        self.add_edge('19', '04')
        self.add_edge('19', '05')
        self.add_edge('19', '06')
        self.add_edge('19', '84')
        self.add_edge('17', '76')

        

    def getCodeExists(self, command):
        if command in self.adj_list:
            return self.adj_list[command]
        else:
            return False