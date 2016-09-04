from Nic import Nic
from utils.Utils import Utils


class Nics:

    def __init__(self):

        self.allDevices = Utils.produce_command("ifconfig -a | sed 's/[ \t].*//;/^\(lo\|\)$/d'")
        self.nicsList = {}
        self.nicsObject = {}
        self.get_all_nics_list()
        self.init_nics_object()

    def get_all_nics_list(self):
        for device in self.allDevices.split():
              self.nicsList.update({device: Nic(Utils.produce_command("ethtool " + device + " | grep 'Port'"),
                                                Utils.produce_command("ethtool " + device + " | grep 'Speed'"),
                                                Utils.produce_command(
                                                  "ifconfig " + device + " | grep HWaddr | awk '{print $5}'"))})

    def init_nics_object(self):
        for k, v in self.nicsList.items():
            self.nicsObject.update({k: v.nicObject})