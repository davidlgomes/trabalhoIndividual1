def armazenarLista():
    lista=[]
    pontoDeParada
    do:
        menu()
        switch(pontoDeParada):
            case 1:
                lista.append(adicionarLista())
                break 
            case 2:
                break
            case 3:
                break
        end
    pontoDeParada=fgets()
    while pontoDeParada!="SIM" or pontoDeParada!="Sim" or pontoDeParada!="sim" or pontoDeParada!="SiM" or pontoDeParada!="SIm" or pontoDeParada!="sIM" or pontoDeParada!="siM"
end

def menu()
    print "Digite a função desejada: "
    print "  1 - Adicionar a lista"
    print "  2 - Pesquisar na lista"
    print "  3 - Adicionar lista através de dados Externos"
end

def adicionarLista()
    entrevista, testePratico, testeTeorico, softSkill, listaAuxiliar
    print "Digite a nota da entrevista"
    entrevista=fgets()
    print "Digite a nota do Teste Prático"
    testePratico=fgets()
    print "Digite a nota do Teste Teórico"
    testeTeorico=fgets()
    print "Digite a nota de Soft Skill"
    softSkill=fgets()
    listaAuxiliar.append(entrevista)
    listaAuxiliar.append(testePratico)
    listaAuxiliar.append(testeTeorico)
    listaAuxiliar.append(softSkill)
    listaAuxiliar
end


