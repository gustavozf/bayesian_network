import copy

# Cria o grafo
node = {
    "nome": "" ,
    "ligacoes" : []
}
# Conta o numero de Amostras
num_amostras = 0
# Conta o numero de amostras por classe
classes = {
    "unacc":0,
    "acc":0,
    "good":0,
    "vgood":0
}
# Conta a quantidade de tipos de features
features_cout = {
	"buying":   { "vhigh":0, "high":0, "med":0, "low":0 },
    "maint":    { "vhigh":0, "high":0, "med":0, "low":0 },
    "doors":    { "2":0, "3":0, "4":0, "5more":0 },
    "persons":  { "2":0, "4":0, "more":0 },
    "lug_boot": { "small":0, "med":0, "big":0 },
    "safety":   { "low":0, "med":0, "high":0 }
}
# Enumera os nomes das classes
tags = {
    "unacc":0,
    "acc":1,
    "good":2,
    "vgood":3
}
# Lista os nomes dos features
features_names = ["buying", "maint", "doors", "persons", "lug_boot", "safety"]
# Cria um dicionario de probabilidades
# futuramente sera probabilidades[nome_da_classe][feature][tipo_do_feature] = probabilidade de ocorrencia do feature na classe
probabilidades = {}

# ---------------------------------------------------------------------------- Funcoes
# Cria os nos
def cria_nos():
    global node

# Cria um arquivo de estatisticas
def create_stats(file_name, featPerCla):
    # declara variaveis globais
    global num_amostras, classes, features_cout, features_names, tags, probabilidades
    # cria o arquivo de estatistica
    stats = open(file_name+'.stats.txt', 'w')

    # cria as chaves do dicionario 
    probabilidades = copy.deepcopy(featPerCla)
    stats.write("Numero total de amostras: " + str(num_amostras) + "\n")
    
    # escreve a quantidade de amostras
    for classe in classes.keys():
        stats.write("  |   {0} : {1} [{2}%]\n".format(classe, classes[classe], round(classes[classe]/num_amostras,5)))
    
    # escreve a quantidade de features e proporcoes
    stats.write("\nFEATURES COUNT\n")
    for feat in features_names:
        stats.write(feat + "\n")
        for fdf in features_cout[feat].keys():
            stats.write(" | {0} : {1} [{2}]\n".format(fdf, features_cout[feat][fdf], round(features_cout[feat][fdf]/num_amostras,5)))

    # escreve a frequencia de feature por classe
    stats.write("\nFEATURES COUNT PER CLASS\n")
    for classe in featPerCla.keys():
        stats.write(classe + "\n")
        for feat in features_names:
            stats.write(" | " + feat + "\n")
            for fdf in featPerCla[classe][feat].keys():
                # calcula a probabilidade do feature pra classe
                prob = round(featPerCla[classe][feat][fdf]/sum(featPerCla[classe][feat].values()),5)
                # salva
                probabilidades[classe][feat][fdf] = prob
                # escreve no arquivo de saida
                stats.write(" | | {0} : {1} [{2}]\t(P={3})\n".format(
                                fdf, 
                                featPerCla[classe][feat][fdf],
                                prob,
                                round(featPerCla[classe][feat][fdf]/num_amostras,5)
                                )
                            )

    print("Feito arquivo de estatistica!")
    stats.close()

# Le o arquivo do carro
def car_reader(file_name):
    # Abre o arquivo pra leitura
    arq = open(file_name, 'r')
    # Cria o arquivo de saida (mais organizado)
    outp = open(file_name+'.bn', 'w')

    # identifica as variaveis globais
    global num_amostras, classes, features_cout, features_names, tags

    # cria o dicionario de frequencia
    features_cout_per_class = {
        "unacc": copy.deepcopy(features_cout),
        "acc": copy.deepcopy(features_cout),
        "good": copy.deepcopy(features_cout),
        "vgood": copy.deepcopy(features_cout)
    }   

    for line in arq.readlines():
        # Conta o total de amostras
        num_amostras+= 1
		# processa a linha lida
        features = line.split(',')
        features[6] = features[6][:-1]
		
        # Conta a quantidade de amostras daquela classe
        classes[features[6]] += 1
        # cria uma string de saida que sera escrita no arquivo
        out_str = str(tags[features[6]])

        for i in range(len(features)-1):
            # conta os features
            features_cout[features_names[i]][features[i]] += 1
            # conta a frequencia do feature
            features_cout_per_class[features[6]][features_names[i]][features[i]] += 1
            out_str += " " + str(i) + ":" + features[i]

        # escreve na saida
        outp.write(out_str + "\n")

    print("Arquivo de saida criado!")
    outp.close()

    # cria o arquivo de estatistica
    create_stats(file_name, features_cout_per_class)

def conta_ocorrencia(file_name, wanted_features):
    # Abre o arquivo pra leitura
    arq = open(file_name, 'r')

    global features_names

    count = 0
    amostras = arq.readlines()
    arq.close()

    lenFile = len(amostras)

    for amostra in amostras:
        contem = True

        # Le as features de uma amostra do arquivo
        features = amostra.split(',')
        features[6] = features[6][:-1]

        # analisa as features passadas pela funcao
        for feature in wanted_features.keys():
            # se a feature analisada possuir valor diferente,
            # entao nao entra no caso analisado
            if features[features_names.index(feature)] != wanted_features[feature]:
                contem = False
                break

        # se a amostra possui todas features desejadas
        # aumenta o contador
        if contem:
            count+=1

    print("Ocorrencia = {0}/{1} = {2}".format(count, lenFile, count/lenFile))