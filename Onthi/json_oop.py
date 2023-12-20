import json
class Student:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id
    def __str__(self):
        return f'{self.name} {self.employee_id}'
f = open('D:/Learning/CodePTIT_Python/Python_Codeptit/Onthi/1.json')
data = json.load(f)
ds=[]
for i in data['data']:
    ds.append(Student(i['name'],i['employee_id']))
for i in ds:
    print(i)
f.close()
