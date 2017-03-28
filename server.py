class Server():
    def __init__(self, ip, port):
        self.__ip = ip
        self.__port = port

    ''' Getters '''
    @property
    def ip(self):
        return self.__ip

    @property
    def port(self):
        return self.__port

    ''' Setters '''
    @ip.setter
    def ip(self, ip):
        self.__ip = ip

    @port.setter
    def port(self, port):
        self.__port = port
