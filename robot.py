roads = [
    "Alice's House-Bob's House", "Alice's House-Cabin",
    "Alice's House-Post Office", "Bob's House-Town Hall",
    "Daria's House-Ernie's House", "Daria's House-Town Hall",
    "Ernie's House-Grete's House", "Grete's House-Farm",
    "Grete's House-Shop", "Marketplace-Farm",
    "Marketplace-Post Office", "Marketplace-Shop",
    "Marketplace-Town Hall", "Shop-Town Hall"
]


# def create_Graph(relations):
#     graph = {}
#     def addEdge(fr , to):
        
#         if graph[fr] != None:
#             graph[fr].add(to)
#         else:
#             graph[fr] = to
        
#     def func_for_split(arr):
#         arr0 = []
#         for i in arr:
#             j = i.split('-')
#             arr0.append(j)
#         return arr0
    
#     x = map(func_for_split,relations)
#     for el in x:
#         addEdge(el[0],el[1])
#         addEdge(el[1],el[0])
        
#     return graph
# graph = create_Graph(roads)
# print(graph)

def func_for_split(arr):
        arr0 = []
        for i in arr:
            j = i.split("-")
            arr0.append(j)
        return arr0
    
x = map(func_for_split,roads)
print(list(x))