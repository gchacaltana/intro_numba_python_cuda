# -*- coding: utf-8 -*-
import platform

class MachineInfo(object):

    def __init__(self):
        pass

    def showMachineInfo(self):
        print("\nInformacion de computador")
        print("---------------------------------")
        print("\nPlataforma: {} {}".format(platform.machine(),platform.version()))
        print("\nProcesador: {}".format(platform.processor()))
        print("\nSistema Operativo : {}".format(platform.platform()))