class myStruct():
    def __init__(self, name, salary, doB, title):
        self.name = name
        self.salary = salary
        self.doB = doB
        self.title = title

    def output_all(self):
        print('{} \n{} \n{} \n{}'.format(self.name, self.salary, self.doB,
                                         self.title))


user = myStruct(
    name=input('type your name: '),
    salary=input('type your salary : '),
    doB=input('type your doB: '),
    title=input('type you title : ')
)

myStruct.output_all(user)