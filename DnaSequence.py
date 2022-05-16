class DnaSequence:
    def __init__(self, ACTG):
        self.__ACTG = ACTG

    def insert(self, val, index):
        self.__ACTG = self.__ACTG[:index] + val + self.__ACTG[index:]

    def getACTG(self):
        return self.__ACTG

    def assignment(self, val):
        isValid=True
        if type(val)!=str:
            val= val.getACTG()
        for letter in val:
            if letter not in ['A','C','T','G']:
                isValid=False
        if isValid:
            self.__ACTG = val

    def __str__(self):
        print("ACTG: "+self.__ACTG)

    def __eq__(self, other):
        return self.__ACTG == other.getACTG()

    def __ne__(self, other):
        return self.__ACTG != other.getACTG()

    def __getitem__(self, key):
        return self.__ACTG[key]

    def __len__(self):
        return len(self.__ACTG)





