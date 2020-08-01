# -*- coding: utf-8 -*-
# Gonzalo Chacaltana Buleje
import platform
import socket
import socket
import re
import uuid
import psutil


class MachineInfo(object):

    def __init__(self):
        self.info = {}
        self.buildDictMachineInfo()

    def buildDictMachineInfo(self):
        self.info['platform'] = platform.system()
        self.info['platform-release'] = platform.release()
        self.info['platform-version'] = platform.version()
        self.info['architecture'] = platform.machine()
        self.info['hostname'] = socket.gethostname()
        self.info['ip-address'] = socket.gethostbyname(socket.gethostname())
        self.info['mac-address'] = ':'.join(re.findall('..',
                                                       '%012x' % uuid.getnode()))
        self.info['processor'] = platform.processor()
        self.info['ram'] = str(
            round(psutil.virtual_memory().total / (1024.0 ** 3)))+" GB"

    def showMachineInfo(self):
        print("\nServer Information")
        print("---------------------------------")
        print("\nPlataforma: {}".format(self.info['platform']))
        print("\nPlataforma Release: {}".format(self.info['platform-release']))
        print("\nPlataforma version: {}".format(self.info['platform-version']))
        print("\nArquitectura: {}".format(self.info['architecture']))
        print("\nHostname: {}".format(self.info['hostname']))
        print("\nIP: {}".format(self.info['ip-address']))
        print("\nMAC: {}".format(self.info['mac-address']))
        print("\nProcesador: {}".format(self.info['processor']))
        print("\nMemoria RAM: {}".format(self.info['ram']))
