import networkx as nx


# Esta funcion ayuda a importar datos

def get_data(filename):
    with open(filename, 'r', encoding='utf8') as rf:
        lines = rf.read().split("\n")
        data = [line.split("\t") for line in lines]
        header = data[0]
        data = data[1:]
    return header, data


# Esta función elimina un nodo si un tren no puede pasar por su color

def block_path(color_tren):
    if color_tren == 'rojo':
        remove = [K for K, V in dict(G.nodes()).items() if V == {'Color': 'verde'}]
        add1 = [edge[0] for edge in G.edges() if edge[1] in remove]
        add2 = [edge[1] for edge in G.edges() if edge[0] in remove]
        G.remove_nodes_from(remove)
        try:
            for add1[0], add2[0] in add1, add2:
                G.add_edge(add1[0], add2[0])
        except:
            G.add_edge(add1[0], add2[0])
    elif color_tren == 'verde':
        remove = [K for K, V in dict(G.nodes()).items() if V == {'Color': 'rojo'}]
        add1 = [edge[0] for edge in G.edges() if edge[1] in remove]
        add2 = [edge[1] for edge in G.edges() if edge[0] in remove]
        G.remove_nodes_from(remove)
        try:
            for add1[0], add2[0] in add1, add2:
                G.add_edge(add1[0], add2[0])
        except:
            G.add_edge(add1[0], add2[0])
    else:
        pass


node_header, node_data = get_data('src/red_de_metro/Estaciones.tsv')
edge_header, edge_data = get_data('src/red_de_metro/Conexiones.tsv')

# se define una red
G = nx.DiGraph()

# Se añaden nodos y arcos a la red a partir de los archivos
for node in node_data:
    G.add_node(node[0], Color=str(node[1]))

for edge in edge_data:
    G.add_edge(edge[0], edge[1])

# Finalidad principal del programa

print('Bienvenido, esta es tu red de metro:')

print('ingresa estacion de origen')
origen = input()
print('ingresa destino')
destino = input()
print('¿el tren es rojo o verde?')
color_tren = input()

block_path(color_tren)

print('La ruta mas corta es:')
print(nx.shortest_path(G, source=origen, target=destino))
