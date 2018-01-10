# -*- coding: utf-8 -*-
import os
from DirFileList import DirFileList

print(os.getcwd())

diretorios = DirFileList()
diretorios.setDirFileList( os.getcwd() )
lista = diretorios.getDirFileList()

print(lista)

for registro in lista:
    print(registro[0])