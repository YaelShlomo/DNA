from hundle_command import CommandHundler

class CLI:
    def __init__(self):
        # self.__command = Hundle_command()
        self.__command = CommandHundler()

    ''' Every time the comad line run'
    the user insert command and the program executes it'''
    def run(self):
        while True:
            command = input("cmd >>>")
            self.__command.hundle(command)

cli = CLI()
cli.run()