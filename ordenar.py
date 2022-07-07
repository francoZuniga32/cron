#!/usr/bin/python3
import os 
import datetime 

dia = datetime.datetime.now()
fecha = dia.strftime("%Y")+"-"+dia.strftime("%m")+"-"+dia.strftime("%d")+"/";

print(fecha)

HOME = '/home/franco'

Descargas = HOME+"/Descargas/"
Imagenes = HOME+"/Imágenes/"
Documentos = HOME+"/Documentos/"
Musica = HOME+"/Música/"
Videos = HOME+"/Vídeos/"
Programas = HOME+"/Programas/"

carpetasAOrdenar = [Descargas, Imagenes, Documentos, Musica, Videos, Programas];

def crearCarpeta(carpeta):
    if not os.path.isdir(carpeta):
        try:
            os.mkdir(carpeta)
            os.chwon(carpeta, 1000, 1000)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise

print("Ordenando Descargas...");

for folder in carpetasAOrdenar:
    for filename in os.listdir(folder) :
        name, extencion = os.path.splitext(folder+filename)

        if extencion in [".jpg", ".jpeg", ".png"]: 
            crearCarpeta(Imagenes+fecha)
            os.rename(folder+filename, Imagenes+fecha+filename)
        if extencion in [".pdf", ".xlsx", ".docx", ".odt", ".md" ,".ods", ".odp", ".zip", ".rar", ".tar", ".gz"]:
            crearCarpeta(Documentos+fecha)
            os.rename(folder+filename, Documentos+fecha+filename)
        if extencion in [".mp3", ".wav"]:
            crearCarpeta(Musica+fecha)
            os.rename(folder+filename, Documentos+fecha+filename)
        if extencion in [".mp4", ".mkv"]:
            crearCarpeta(Videos+fecha)
            os.rename(folder+filename, Videos+fecha+filename)
        if extencion in [".deb", ".sh", ".js", ".jar", ".exe", ".st"]:
            crearCarpeta(Programas+fecha)
            os.rename(folder+filename, Programas+fecha+filename)
