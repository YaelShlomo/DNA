def factoryHndleCommand(command):
    commands = {
        "new": NewSeq,
        "load": Load,
        "dup": Dup,
    }

    return commands[command]()