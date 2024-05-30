# string 

name:str = 'Muhammad waqas'
age:int = 24

concat = name + str(age)
print(concat)

# f-string 

name2:str = 'Waqas'
fname:str = 'Raees ahmed'
age2:int = 24
student_card = f'''
 PIAIC student info.
 Student Name : {name2}
 Father Name : {fname}
 Age : {age2}
 '''
print(student_card)