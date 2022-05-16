from data_base import DataBase
from DnaSequence import DnaSequence
from new import New

class Load:
    __DB=DataBase()

    def execute(self,command):
        path = command[0]
        f = open(path, "r")
        seq = f.readline()
        if len(command)>1: #If name inserted
            seq_name=command[1]
            New().execute([seq, seq_name])
        else:
            New().execute([seq])