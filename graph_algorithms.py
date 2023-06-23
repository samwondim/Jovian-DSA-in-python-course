class Graph:
    def __init__(self):
        self.adj_list = []
        
    def add_edge(self, n_list):
        self.adj_list.append(n_list)
        
    def remove_edge(self, edge):
        for l in adj_list:
            for i in l:
                if i == edge:
                    l.remove(i)
                    
    def get_list(self):
        return self.adj_list
