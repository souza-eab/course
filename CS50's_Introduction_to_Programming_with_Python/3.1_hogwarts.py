# Utilizar list

# Ex1
#studentes = ["Hermione","Harry","Ron"]
#print(students[0])
#print(students[1])
#print(students[2])


# Algo melhor do que saber o nome, já que a cada tem mais novos alunos
# Ex2
#students = ["Hermione","Harry","Ron"]
#for students in students:
#  print(students)
  
# Ex3 utilizar a função le
#students = ["Hermione","Harry","Ron"]
#for i in range (len(students)): # retorna os tres nomes
#  print(students[i])

# Ex4 utilizar a função para atribuir um número a cada um deles, lembrando que no python começa em 0
#students = ["Hermione","Harry","Ron"]
#for i in range (len(students)): # retorna os tres nomes
#  print(i+1, students[i])
  


# Ex5 utilizar a função ficaria grande/
#students = ["Hermione","Harry","Ron","Draco"]
#houses = ["Gryffindor","Gryffindor","Gryffindor","Slytherin"]
 
#Ux6
#Utiliza single dic {}
#students = {
#  "Hermione":"Gryffindor",
#  "Harry":"Gryffindor".,
#  "Ron":"Gryffindor",
#  "Draco": "Slytherin"
#}
#for student in students:
#  print(student, students[student], sep =",")
  

#Ux7x
#Utiliza dic complexo {}
students = [
  {"name": "Hermione", "house": "Gryffindor", "patronus": "Otther"},
  {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
  {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell Terrier"},
  {"name": "Draco", "house": "Slytherin", "patronus": None}
]

for student in students:
  print(student["name"], student ["house"], student["patronus"], sep= ", ")
