from utils.Utils import Utils


class Cpu:

    def __init__(self):

        self.sockets = self.init_socket()
        self.cores =  self.init_cores()
        self.speed = self.init_speed()
        self.arch = self.init_arch()

        self.cpuObject = {'Sockets' : self.sockets,
                          'Cores' : self.cores,
                          'Speed' : self.speed,
                          'Arch' : self.arch}

    def init_socket(self):
        return Utils.produce_command("lscpu | grep 'Socket(s)' | awk '{print $2}'")

    def init_cores(self):
        return Utils.produce_command("cat /proc/cpuinfo | grep '^processor' | wc -l")

    def init_speed(self):
        return Utils.produce_command("lscpu | grep 'CPU MHz' | awk '{print $3}'")

    def init_arch(self):
        return Utils.produce_command("lscpu | grep 'Arch' | awk '{print $2}'")
