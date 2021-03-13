class Employee:
    company="google"
    def show(self):
        print(f"this is an employee of {self.company} ")

class programmer(Employee):
   language="python"
   company="microsoft"
   def languageused(self):
         print(f"the language used is {self.language}")
   def show(self):
    print(f"this is an employee of {self.company} ")     

e=Employee()
p=programmer()
e.show()
p.show()
p.languageused()

