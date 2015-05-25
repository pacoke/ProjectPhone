__author__ = 'javier'
#encoding:utf-8
from BeautifulSoup import BeautifulSoup
import urllib2
import urllib
import sqlite3
from setuptools.package_index import HREF
url = "http://www.phonehouse.es/moviles/moviles-libres.html"

def buscarMoviles():
    soup = BeautifulSoup(urllib2.urlopen(url))
    Moviles = soup.findAll("li",{"class":"resultado"})
    return Moviles
def listamoviles(Moviles):
    moviles=[]
    for movil in Moviles:
        nombre = movil.find("a").attrs[1][1]
        #nombre = movil.find("a").attrs.get("title")
        precio = movil.find("div",{"class":"precio precio-libre"}).find("strong").string
        #Precio = precio1.find("strong").string
        enlace = movil.find("a").attrs[0][1]
        #enlace = movil.find("a").attrs.get("href")
        enlaceconstruido = "http://www.phonehouse.es"+ enlace
        imagen= movil.find("img").attrs[0][1]
        #imagen = movil.find("img").attrs.get("src")
        mitadenlace =  enlaceconstruido.split('#')
        caracteristica =  mitadenlace[0] + "#" + "caracteristicas"
        soup1 = BeautifulSoup(urllib2.urlopen(caracteristica))
        Caracteristicas_Moviles = soup1.findAll("tbody")
        caract = Caracteristicas_Moviles[Caracteristicas_Moviles.__len__()-1]
        listacaracteristicas = []
        for c in caract.findAll("tr"):
            l = c.findAll("td")
            listacaracteristicas.append((l[0].text,l[1].text))
        moviles.append([nombre,precio,enlaceconstruido,imagen,listacaracteristicas])
    return moviles