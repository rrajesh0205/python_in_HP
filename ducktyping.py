class Pycharm:
    def execute(self):
        print("Compiling")
        print("Running")
class Laptop:
    def code(self, IDE):
        IDE.execute()
IDE = Pycharm()
lap1 = Laptop()
lap1.code(IDE)
