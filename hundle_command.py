from factory import Factory
class CommandHundler:
    def __init__(self):
        self.__commands = ['new', 'load', 'dup']

    def hundle(self, command):  # Command is all the cmd input
        splited_command = self.splite_command(command)
        if splited_command[0] not in self.__commands:  # check if the command name valid
            print("Command {} is not valid".format(splited_command[0]))
            return
        # splited_command[0] is the command name and splited_command[1:] is the params
        Factory(splited_command[0]).executor(splited_command[1:])

    def splite_command(self, command):
        command_list = command.split(" ")
        return command_list