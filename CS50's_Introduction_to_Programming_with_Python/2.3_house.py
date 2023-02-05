# Match

#Ex1

#name = input("What's your name?")

#if name =="Harry":
#  print("Gryffindor")
#elif name =="Hermione":
#  print("Gryffindor")
#elif name =="Ron":
#  print("Gryffindor")
#elif name =="Draco":
#  print("Slytherin")
#else:
#  print("Who?")


#Ex2 (Imagina se tivessemos para todas as casas
#name = input("What's your name?")
#if name =="Harry" or name =="Hermione" or name == "Ron":
#print("Gryffindor")
#elif name =="Draco":
#  print("Slytherin")
#else:
#  print("Who?")


#Ex3 (Match
#name = input("What's your name?")
#match name:
#  case "Harry":
#    print("Gryffindor")
#  case "Hermione":
#   print("Gryffindor")
#  case "Ron":
#   print("Gryffindor")
#  case "Draco":
#   print("Slytherin")
#  case _:
#   print("Who?")
  
  


#Ex4 (Match -Reduzindo as linhas - utilizamos | para adicionar mais nomes pertece a aquele caso esm especifico
name = input("What's your name?")
match name:
  case "Harry" | "Hermione"| "Ron" :
    print("Gryffindor")
  case "Draco":
   print("Slytherin")
  case _:
   print("Who?")
  
  
  
    
