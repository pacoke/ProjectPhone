import json
import phohouse
from datetime import datetime
lista=phohouse.listamoviles(phohouse.buscarMoviles())
i = 0
j = 0
caracteristicapk=[]
archivo = open("initial_data.json","w")
caracteristicastodas={}
fechaactual=datetime.now().year.__str__()+"-"+datetime.now().month.__str__()+"-"+datetime.now().day.__str__()
archivo.writelines("[")
for l in lista:
    archivo.writelines(json.dumps({"pk":j,"model":"principal.price","fields":{"coins":"euros","cuantity":l[1],"link":l[2]}},indent=2,separators=(',',':'))+",")
    for caracteristica in l[4]:
        caracteristicanueva = {caracteristica[0]+" "+caracteristica[1]:i}
        if not caracteristicastodas.has_key(caracteristica[0]+" "+caracteristica[1]):
            archivo.writelines(json.dumps({"pk":i,"model":"principal.caracteristic","fields":{"type":caracteristica[0],"information":caracteristica[1]}},indent=2,separators=(',',':'))+",")
            caracteristicapk.append(i)
            caracteristicastodas.update(caracteristicanueva)
            i = i + 1
        else:
            archivo.writelines(json.dumps({"pk":caracteristicastodas.get(caracteristica[0]+" "+caracteristica[1]),"model":"principal.caracteristic","fields":{"type":caracteristica[0],"information":caracteristica[1]}},indent=2,separators=(',',':'))+",")
            caracteristicapk.append(caracteristicastodas.get(caracteristica[0]+" "+caracteristica[1]))
    archivo.writelines(json.dumps({"pk" : j,"model" :"principal.phone","fields":{"name":l[0],"image":"","price_that_has":j,"caracteristics_that_own":caracteristicapk,"tiempo_registro":fechaactual}},indent=2,separators=(',',':'))+",")
    #print caracteristicastodas.items().__str__()
    j = j + 1
    caracteristicapk=[]
    print "Telefono:"+l[0]
archivo.writelines("]")
archivo.close()
