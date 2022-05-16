from data_base import DataBase
from new import New
from load import Load
from dup import Dup

''' This class implement Factory and singelton design pattern'''
class Factory:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not Factory.__instance:
            Factory.__instance = object.__new__(cls)
        return Factory.__instance

    def __init__(self, command_name):
        super().__init__()
        self._creator_types = {
            "new": New,
            "load": Load,
            "dup": Dup
        }
        self._command_name = command_name

    def executor(self, commandsLst):
        '''command list is all the cmd input extract the coomand name. Every word in another index'''
        if len(commandsLst)==0:
            raise Exception ("Missing arguments")
        self._creator_types[self._command_name]().execute(commandsLst)


