# Declaracoes
nodes = {}
database = "asia_db.txt"

# Leitura da base de dados
def db_reader(node_dict, file_name):
    arq = open(file_name, 'r')
    
    for line in arq.readlines():
        # separa o no origem do destino
        # para criar a aresta
        origem, destino = line.split(" ")

        # se a origem nao foi inicializada ainda
        if origem not in node_dict.keys():
            node_dict[origem] = []

        # insere a aresta (retirando o '\n')
        node_dict[origem].append(destino[:-1])

# Main
def main():
    db_reader(nodes, database)
    print(nodes)

if __name__ == "__main__":
    main()
