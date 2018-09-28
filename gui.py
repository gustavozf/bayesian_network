from tkinter import *
from rb import *
# ------------------------------------- Pega a base
database = "./databases/car.features"
read_data(database)
# ------------------------------------ variaveis
nomes = {
	'Muito Alto':'vhigh',
	'Alto':'high',
	'Medio':'med',
	'Baixo':'low',
	'5 ou Mais':'5more',
	'Mais':'more',
	'Pequeno' : 'small',
	'Grande':'big',
	'2':'2',
	'3':'3',
	'4':'4'
}

tags = {'vgood':"Muito Bom", 'good':"Bom", "acc":"Aceitavel","unacc":"Inaceitavel"}

# --------------------------------------- Funcao
def pop_up():
	global tags, asw
	global v1, v2, v3, v4, v5, v6
	global predict

	ans = {
		'buying': nomes[v1.get()], 
		'maint': nomes[v2.get()],
		'doors': nomes[v3.get()],
		'persons': nomes[v4.get()],
		'lug_boot': nomes[v5.get()],
		'safety': nomes[v6.get()]
	}

	print(ans)
	x, _ = predict_bay_net(ans)
	print("Predicao: {}\n".format(x))
	answ['text'] = "Avaliacao: {}".format(tags[x])

# --------------------------------------------------
root = Tk()

maxWid = 500
maxHei = 500

root.geometry('{}x{}'.format(maxWid, maxHei))
root.title("Avaliador de Carros")

# ----------------------------------------------------- Variaveis
buying   =  [ 'Muito Alto','Alto','Medio','Baixo']
maint    =  [ 'Muito Alto','Alto','Medio','Baixo']
doors    =  [ "2", "3", "4", "5 ou Mais"]
persons  =  [ "2", "4", "Mais"]
lug_boot =  [ "Pequeno", "Medio", "Grande"]
safety   =  [ "Baixo", "Medio", "Alto"]
# ------------------------------------------------------------------------ Titulo
titulo = Label(root, text="Avaliador de Carros",width=20,font=("bold", 20))
titulo.place(x=90,y=50)
# ------------------------------------------------------------------------- Botao do valor
label_1 = Label(root, text="Valor do Altomovel",width=20,font=("bold", 10))
label_1.place(x=70,y=100)

v1=StringVar()
droplist=OptionMenu(root,v1, *buying)
droplist.config(width=15)
v1.set('Baixo') 
droplist.place(x=240,y=100)

# ------------------------------------------------------------------------- Botao do valor da manutencao
label_2 = Label(root, text="Valor da Manutencao",width=20,font=("bold", 10))
label_2.place(x=70,y=150)

v2=StringVar()
droplist=OptionMenu(root,v2, *maint)
droplist.config(width=15)
v2.set('Baixo') 
droplist.place(x=240,y=150)

# ------------------------------------------------------------------------- Botao do num de portas
label_3 = Label(root, text="Numero de Portas",width=20,font=("bold", 10))
label_3.place(x=70,y=200)

v3=StringVar()
droplist=OptionMenu(root,v3, *doors)
droplist.config(width=15)
v3.set('2') 
droplist.place(x=240,y=200)

# ------------------------------------------------------------------------- Botao do num de lugares
label_4 = Label(root, text="Numero de Lugares",width=20,font=("bold", 10))
label_4.place(x=70,y=250)

v4=StringVar()
droplist=OptionMenu(root,v4, *persons)
droplist.config(width=15)
v4.set('2') 
droplist.place(x=240,y=250)

# ------------------------------------------------------------------------- Botao do tam do porta mala
label_5 = Label(root, text="Tamanho do Porta-Malas",width=20,font=("bold", 10))
label_5.place(x=70,y=300)

v5=StringVar()
droplist=OptionMenu(root,v5, *lug_boot)
droplist.config(width=15)
v5.set('Pequeno') 
droplist.place(x=240,y=300)

# ------------------------------------------------------------------------- Botao do nivel de seguranca
label_6 = Label(root, text="Nivel de Seguranca",width=20,font=("bold", 10))
label_6.place(x=70,y=350)

v6=StringVar()
droplist=OptionMenu(root,v6, *safety)
droplist.config(width=15)
v6.set('Baixo') 
droplist.place(x=240,y=350)

# ------------------------------------------------------------------------- Botao de calculo
Button(root, text='Avaliar',width=20,bg='blue',fg='white', command=pop_up).place(x=150,y=400)
# ------------------------------------------------------------------------- Texto da predicao
answ = Label(root, text="",width=20,font=("bold", 10))
answ.place(x=150,y=450)

root.mainloop()
