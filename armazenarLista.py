def main():
    lista=[]
    opcao=0
    pontoDeParada=0
    candidatosEncontrados=[]
    auxiliar=[]
    while pontoDeParada!="SIM" and pontoDeParada!="Sim" and pontoDeParada!="sim" and pontoDeParada!="SiM" and pontoDeParada!="SIm" and pontoDeParada!="sIM" and pontoDeParada!="siM":
        opcao=input("\nDigite a função desejada:\n   1 - Adicionar a lista\n   2 - Pesquisar na lista\n   3 - Adicionar lista através de dados Externos\n")
        if opcao=='1':
            auxiliar=adicionarLista()
            lista.append(f'e{auxiliar[0]}_t{auxiliar[2]}_p{auxiliar[1]}_s{auxiliar[3]}')
        elif opcao=='2':
            candidatosEncontrados=pesquisarCandidato(lista)
            print(candidatosEncontrados)
        elif opcao=='3':
            continue
        elif opcao!='1' and opcao!='2' and opcao!='3':
            print("\nOpção Inválida\n")
        pontoDeParada=input("Deseja Sair? ")
    return lista 

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
    entrevista=input("\nDigite a nota da entrevista: \n")
    testePratico=input("\nDigite a nota do Teste Prático: \n")
    testeTeorico=input("\nDigite a nota do Teste Teórico: \n")
    softSkill=input("\nDigite a nota de Soft Skill: \n")
    indice=0
    while indice<len(lista):
        listaAuxiliar = [[item[1:] for item in element.split('_')] for element in lista]
        print(listaAuxiliar)
        if listaAuxiliar[indice][1]==entrevista and listaAuxiliar[indice][1]==testePratico and listaAuxiliar[indice][2]==testeTeorico and listaAuxiliar[indice][3]==softSkill:
            candidatosEncontrados.append(indice)
        indice+=1
    if len(candidatosEncontrados)==0:
        return 'Nenhum candidato encontrado com essas notas'
    return candidatosEncontrados

print(main())