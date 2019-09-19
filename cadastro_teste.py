# Criando e escrevendo em arquivos de texto (modo 'w').
arquivo = open('arq01.txt','w')
arquivo.write("Bóson Treinamentos\n")
arquivo.write("Criando um arquivo de texto com Python\n")
arquivo.write("Arquivo criado por Fábio dos Reis\n")
arquivo.write("É isso ai pessoal!\n")
arquivo.close()

# Lendo o arquivo criado:
arquivo = open('arq01.txt','r')
for linha in arquivo:
    linha = linha.rstrip()
    print (linha)
arquivo.close()