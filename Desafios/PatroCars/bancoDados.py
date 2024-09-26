def whatMontadora(id_montadora):
   for i in range(len(modelosMontadoras)):
      for j in range(len(modelosMontadoras[i])):
         if id_montadora == modelosMontadoras[i][j]["id_montadora"]:
            return i
   
   return -1


def hasMontadora(id_montadora):
   for i in range(len(modelosMontadoras)):
      for j in range(len(modelosMontadoras[i])):
         if id_montadora == modelosMontadoras[i][j]["id_montadora"]:
            return True
   
   return False


def dadosModelos(id_montadora,datas):
   modelo = {}
   modelo["id"] = datas[0]
   modelo["nome"] = datas[1]
   modelo["id_montadora"] = datas[2]
   modelo["valor_referencial"] = datas[3]
   modelo["motarizacao"] = datas[4]
   modelo["turbo"] = datas[5]
   modelo["automatico"] = datas[6]

   if hasMontadora(id_montadora):
      indexMontadora = whatMontadora(id_montadora)
      modelosMontadoras[indexMontadora].append(modelo)
   if not hasMontadora(id_montadora):
      modelosMontadoras.append([modelo])
      

modelosMontadoras = []


def dadosMontadora(datas,montadoras):
   montadora = {}
   montadora["id"] = datas[0]
   montadora["nome"] = datas[1]
   montadora["pais"] = datas[2]
   montadora["anofundacao"] = datas[3]
   montadoras.append(montadora)


montadoras = []