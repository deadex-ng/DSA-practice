#author: Fumbani
#A python program to represent a unidirected weighted graph
#using adjaceny list
class Graph:
    def __init__(self,edge_list,num_of_nodes):
        self.adj_lst = [[] for i in range(num_of_nodes)]

        for (origin,dest,weight) in edge_list:
            self.adj_lst[origin].append([dest,weight])
            self.adj_lst[dest].append([origin,weight])
        print(self.adj_lst)

    def add_node(self, origin, dest,weight):
        self.adj_lst[origin].append([dest,weight])

        return self.adj_lst

if __name__ == "__main__":
    num_of_nodes = 5
    edge_list = [(0,4,20),(0,1,10),(4,3,70),(4,1,50),(1,3,40),(1,2,30),(2,3,60)]

    graph = Graph(edge_list,num_of_nodes)    
    #print(graph)
    print("Added a node from node 4 to node 5 with a weight of 10")
    print(graph.add_node(4,5,10))
