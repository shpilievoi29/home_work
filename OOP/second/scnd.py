#from datetime import date, timedelta

#now = date.today()
#month_start = date(now.year, now.month, 1)

#weekend = [5, 6]

#diff = (now - month_start).days + 1


#day_count = 0

#for day in range(diff):
    #if (month_start + timedelta(day)).weekday() not in weekend:
        #day_count += 1




class Employee:    
     
    def __init__(self, name, salary_day, email,position):
        self.name = name
        self.email = email
        self.salary_day = salary_day
        self.position = position
    def ework(self):
        return "I come to the office"

    def check_salary(self, day):
        salary = self.salary_day * day
        return salary

    
    
    
    def comparison(self, other):
      if self.salary_day> other.salary_day:
          return f'{self.name} earns more'
      elif self.salary_day < other.salary_day:
          return f'{other.name} earns more'
      return 'they earn the same '
    
    

igor = Employee('Igor', 1000, 'igor@gmail.com','programmer')
vera = Employee('Vera', 150, 'vera@such.com','recruiter')
sasha = Employee('Sasha', 130, 'sasha@gmai.com', 'programmer')
vasia = Employee('Vasia', 200, 'vasia@bestcoder.ch', 'programmer' )
lenin = Employee('Ilich', 500, 'grib@yatakdumayu.ru','recruiter')
curt = Employee('Cobein', 180, 'ineedagun@bang.us', 'recruiter')
adic = Employee('Adidas', 350 , 'antarctida@alemania.zik', 'programmer')
print(vera.check_salary(4))
print(Employee.comparison(igor,vera))



class Recruiter(Employee):
    def __init__(self, name: str, salary_day: int, email: str, position: str):
        super().__init__(name, salary_day, email, position)

    
    def work(self):
        e_work = super().ework()
        return e_work + ' and start to hiring.'
    
    def __str__(self):
        return f"Должность:  {self.position} {self.name}"
lenin = Recruiter('Ilich', 500, 'grib@yatakdumayu.ru','recruiter')
curt = Recruiter('Cobein', 180, 'ineedagun@bang.us', 'recruiter')
vera = Employee('Vera', 150, 'vera@such.com','recruiter')
     
class Programmer(Employee):

    def __init__(self, name: str, salary_day: int, email: str, position: str, tech_stack: list):
        super().__init__(name, salary_day, email, position)
        self.tech_stack: list = tech_stack
  
    def work(self):
        work1= super().ework()
        return work1 + ' and start to coding.'



    def __str__(self):
        return f"Должность:  {self.position} {self.name}"

        
    def comparison_stack(self,other):
        self.count_skills = 0
        other.count_skills = 0
        for i in self.tech_stack:
            self.count_skills += 1
        for z in other.tech_stack:
            other.count_skills += 1
        if self.count_skills > other.count_skills:
            return f'{self.name} is probably better than {other.name}'
        elif self.count_skills < other.count_skills:
            return f'{other.name} is probably better than {self.name}'
        return ' probably they are equal '

    
    def __add__ (self, other):
        name = 'Alex'
        salary_day = 1200
        email = 'best@best,be'
        position ="programmer"
        tech_stack = {self.tech_stack + other.tech_stack}
        return Programmer(name, salary_day, email, position,tech_stack)

igor = Programmer('Igor', 1000, 'igor@gmail.com','programmer',['JS', 'Pyton', 'Delphi'])
sasha = Programmer('Sasha', 130, 'sasha@gmai.com', 'programmer' , ['Python'])
vasia = Programmer('Vasia', 200, 'vasia@bestcoder.ch', 'programmer', [ 'PHP', 'C#'] )
adic = Programmer('Adidas', 350 , 'antarctida@alemania.zik', 'programmer',['Java'])

print(Programmer.comparison_stack(igor,adic)) 
print(Recruiter.work(self=lenin))
print(Programmer.work(self=igor))