
# Função para abrir o arquivo
def openFile (file):
    with open(file) as f:
        list = f.read().splitlines() 
    return list

# Função para armazenar o arquivo em um dicionário  
def store(input):
    dict = {'alfabeto':input[0]
            ,'num_estados':int(input[1])
            ,'num_transicoes':int(input[2])
            ,'transicoes':input[3:3+int(input[2])]
            ,'num_entradas':int(input[3+int(input[2])])
            ,'entradas':input[4+int(input[2]):]}
    return dict

# Imprimir cada passo
def output(cabecote, string):
    aux = [' ']*len(string)
    aux[cabecote] = '^'
    print(''.join(string))
    print(''.join(aux))

# Máquina de Turing
def turingMachine(dict, test):
    # Estado inicial
    state = 1
    
    # Armazenar string a ser testada, em uma lista
    string = list(dict['entradas'][test])
    
    # Estado final 
    final = int(dict['transicoes'][-1][-1])

    # Preencher o resto da string de tamanho 100 com espaços em branco '-'
    for i in range(101-len(string)):
        string.append('-')

    # Posição inicial do cabeçote
    cabecote = 0

    # Máquina
    while True:
        output(cabecote, string)
        # Armazena todas transições do estado atual 
        transitions = [x for x in dict['transicoes'] if int(x[0])==state]

        if (not transitions and state == final and string[cabecote] == '-'):
            return 'OK'
        elif(not transitions and string[cabecote] != '-'):
            return 'not OK'
        # Armazena a transição que contém o elemento 
        transition = ''.join(x for x in transitions if x[2] == string[cabecote]).split(' ')

        if (transition[0] == '' and state != final):
            return 'not OK'
        if(transition[0] == '' and string[cabecote] == '-' and state == final):
            return 'OK'
        # Escrita na fita
        string[cabecote] = transition[2]
        output(cabecote, string)
        # Mover o cabeçote
        if(transition[3] == 'D'):
            cabecote+=1
        elif(transition[3] == 'E'):
            cabecote-=1
        state = int(transition[4])

# Main
input = openFile('input3.txt')
dict = store(input)

if(len(dict['alfabeto'])<=30 and dict['num_estados']<=50):
    for i in range(dict["num_entradas"]):
        if(len(dict['entradas'][i])<=100):
            print(i+1,': ',dict["entradas"][i],' ',turingMachine(dict,i),'\n\n')
        else:
            print('A fita de entrada precisa ter no máximo 100 elementos!')
            break
else:
    print('O alfabeto precisa ter no máximo 30 elementos, e o número de estados no máximo 50!')


