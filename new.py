from data_base import DataBase
from DnaSequence import DnaSequence
class New:
    __DB=DataBase()

    def execute(self,command):#Command is list of the seq and the name of the the seq
        seq = command[0]
        if (len(command)>1):#If inserted seq_name
            seq_name = command[1]
            if seq_name[0]!= '@':#If the name does not start with @ it is not legal name
                print("DNA name should start with @")
                return
        else:
            seq_name = "seq_"+str(self.__DB.get_counter()+1)
        res = self.__DB.add_dna(seq,self.__DB.get_counter()+1, seq_name)
        if res:
            if len(seq)>40:
                 new_seq = seq[:32]+"..."+seq[-3:]
            else:
                new_seq = seq
            print("[{}] {} {}".format(self.__DB.get_counter(), new_seq, seq_name))
        return