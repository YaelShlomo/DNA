from data_base import DataBase
from DnaSequence import DnaSequence
from new import New

class Dup:
    __DB = DataBase()
    __names_dict = dict()
    def execute(self, command):#command is list of id and name
        id = command[0][1:]
        seq = self.__DB.get_dna_by_id(id)
        if seq==False:
            return
        if len(command) > 1:  # If name inserted
            seq_name = command[1]
            New().execute([seq, seq_name])
        else:
            seq_name=self.__DB.get_dna_name(seq)
            seq_name=seq_name[0]
            if seq_name==False:
                print("#{} is not exsist".format(id))
                return
            if seq_name in self.__names_dict:
                self.__names_dict[seq_name]+=1
            else:
                self.__names_dict[seq_name]=1
            seq_name=str(seq_name)+"_"+str(self.__names_dict[seq_name])
            New().execute([seq,seq_name])