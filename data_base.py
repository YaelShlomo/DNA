class DataBase:

    __dna_sequences = []
    __dna_dict_by_id = dict()
    __dna_dict_by_name = dict()
    __counter = 0
    __valid_latters = ['A', 'C', 'G', 'T']
    # __instance=None
    #
    # def __new__(cls, *args, **kwargs):
    #     if not DataBase.__instance:
    #         DataBase.__instance=object.__init__(cls)
    #     return DataBase.__instance

    def add_dna(self, seq, id, name):
        validate_seq = self.validate_seq(seq)
        if validate_seq:
            #if seq not in self.__dna_sequences:
            self.__dna_sequences.append(seq)
            seq_index = len(self.__dna_sequences)-1
            self.__dna_dict_by_id[id] = seq_index
            self.__dna_dict_by_name[name] = seq_index
            self.__counter+=1
            return True
        else:
            print("{} is not valid sequence".format(seq))
            return False

    def get_all_dna_lst(self):
        return self.__dna_sequences

    def get_dna_by_id(self,id):
        id = int(id)
        try:
            index = self.__dna_dict_by_id[id]
        except:
            print ("ID {} does'nt exist".format(id))
            return False
        return self.__dna_sequences[index]

    def get_dna_by_name(self,name):
        try:
            index = self.__dna_dict_by_name[name]
        except:
            raise ("Name does'nt exist")
        return self.__dna_sequences[index]

    def get_dna_id(self, dna_seq):
        for s in self.__dna_sequences:
            if s == dna_seq:
                index = self.__dna_sequences.index(s)
                break
        key_list = list(self.__dna_dict_by_id.keys())
        val_list = list(self.__dna_dict_by_id.values())
        id = val_list.index(index)
        return key_list[id]


    '''Return list with all the names of the seq '''
    def get_dna_name(self, dna_seq):
        index=None
        names=[]
        indexs=[]
        res =[]
        for s in self.__dna_sequences:
            if s == dna_seq:
                index = self.__dna_sequences.index(s)
                indexs.append(index)
        key_list = list(self.__dna_dict_by_name.keys())
        val_list = list(self.__dna_dict_by_name.values())
        if len(indexs)==0:
            return False
        for i in indexs:
            name = val_list.index(index)
            names.append(name)
        for name in names:
            res.append(key_list[name])
        return res

    def get_counter(self):
        return self.__counter

    def validate_seq(self, seq):
        for latter in seq:
            if latter not in self.__valid_latters:
                return False
        return True





