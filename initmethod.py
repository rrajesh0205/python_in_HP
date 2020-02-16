class Computer:
    def __init__(self, CPU, RAM):
        self.CPU = CPU
        self.RAM = RAM
    def config(self):
        print("The Config is...", self.CPU, self.RAM)
com1 = Computer("i5", 16)
com2 = Computer("Ryzen 3", 8)

com1.config()
com2.config()
