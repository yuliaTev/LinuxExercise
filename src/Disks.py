from Disk import Disk
from utils.Utils import Utils

class Disks:

    def __init__(self):

        self.allDisks = Utils.produce_command("lsblk | grep ^[a-z]  | awk '{print $1}'")
        self.disksList = {}
        self.disksObject = {}
        self.get_all_disks()
        self.init_disks_object()

    def get_all_disks(self):
        for disk in self.allDisks.split():
            self.disksList.update({disk: Disk(Utils.produce_command("sudo fdisk -l | grep /dev/sda: |awk '{print $3$4}'"),
                                              Utils.produce_command("cat /sys/block/sd?/device/vendor"))})

    def init_disks_object(self):
        for k, v in self.disksList.items():
            self.disksObject.update({k: v.diskObject})