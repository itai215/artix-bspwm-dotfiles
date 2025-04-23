import os


class Daemons:
    @staticmethod
    def enable_all_daemons():
        Daemons.__enable_network_daemon()
        Daemons.__enable_bluetooth_daemon()

    @staticmethod
    def __enable_network_daemon():
        os.system("sudo dinitctl enable NetworkManager")
    
    @staticmethod
    def __enable_bluetooth_daemon():
        os.system("sudo dinitctl enable bluetooth.service")
        os.system("sudo dinitctl start bluetooth.service")
