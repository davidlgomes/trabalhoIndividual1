import pandas as pd

def main():
    lista=[]
    opcao=0
    pontoDeParada=0
    candidatosEncontrados=[]
    auxiliar=[]
    pathArquivo=''
    while pontoDeParada!="SIM" and pontoDeParada!="Sim" and pontoDeParada!="sim" and pontoDeParada!="SiM" and pontoDeParada!="SIm" and pontoDeParada!="sIM" and pontoDeParada!="siM":
        opcao=input("\nDigite a função desejada:\n   1 - Adicionar a lista\n   2 - Pesquisar na lista\n   3 - Adicionar lista através de dados Externos\n")
        if opcao=='1':
            auxiliar=adicionarLista()
            lista.append(f'e{auxiliar[0]}_t{auxiliar[2]}_p{auxiliar[1]}_s{auxiliar[3]}')
        elif opcao=='2':
            candidatosEncontrados=pesquisarCandidato(lista)
            print(candidatosEncontrados)
        elif opcao=='3':
            nomePlanilha=input('Digite o nome da planilha: ')
            leituraPlanilha(nomePlanilha, lista)
        elif opcao!='1' and opcao!='2' and opcao!='3':
            print("\nOpção Inválida\n")
        pontoDeParada=input("Deseja Sair? ")
    return 'Saindo...'

def adicionarLista():
    entrevista=0
    testePratico=0
    testeTeorico=0 
    softSkill=0 
    listaAuxiliar=[]
    entrevista=input("\nDigite a nota da entrevista: \n")
    testePratico=input("\nDigite a nota do Teste Prático: \n")
    testeTeorico=input("\nDigite a nota do Teste Teórico: \n")
    softSkill=input("\nDigite a nota de Soft Skill: \n")
    listaAuxiliar.append(entrevista)
    listaAuxiliar.append(testePratico)
    listaAuxiliar.append(testeTeorico)
    listaAuxiliar.append(softSkill)
    return listaAuxiliar

def pesquisarCandidato(lista):
    candidatosEncontrados=[]
    listaAuxiliar=[]
    entrevista=int(input("\nDigite a nota da entrevista: \n"))
    testePratico=int(input("\nDigite a nota do Teste Prático: \n"))
    testeTeorico=int(input("\nDigite a nota do Teste Teórico: \n"))
    softSkill=int(input("\nDigite a nota de Soft Skill: \n"))
    indice=0
    while indice<len(lista):
        listaAuxiliar = [[item[1:] for item in element.split('_')] for element in lista]
        if int(listaAuxiliar[indice][0])>=entrevista and int(listaAuxiliar[indice][1])>=testePratico and int(listaAuxiliar[indice][2])>=testeTeorico and int(listaAuxiliar[indice][3])>=softSkill:
            candidatosEncontrados.append(f'Candidato {indice+1}')
        indice+=1
    if len(candidatosEncontrados)==0:
        return 'Nenhum candidato encontrado com notas maiores que os parâmetros mínimos'
    return candidatosEncontrados

def leituraPlanilha(nomePlanilha, lista):
    # Carregar a planilha Excel
    dados = pd.read_csv(f'./{nomePlanilha}.csv', header=None, usecols=[1])
    dados = dados.drop(0)
    arrayDados=dados.to_numpy().flatten()
    adicionarListaDeCsv(arrayDados, lista)

def adicionarListaDeCsv(arrayDados, lista):
    for elemento in arrayDados:
        lista.append(elemento)
    print(lista)
    print("Dados salvos com sucesso!")

print(main())