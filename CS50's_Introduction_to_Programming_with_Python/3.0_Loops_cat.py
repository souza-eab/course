# While - loop de quantos n quiser

#print("miau")
#print("mia)
#print("miau")

#Ex1

#i =1
#while < 3:
#  print("meow")
#  i = i += 1
#  print()


  
#Ex2 for, list 3 meow

#for i in [0,1,2]:
#  print("meow")

  
  
#Ex3 for, list 
#print("meow\n" *3, end="") # nova linha n \n


#Ex4 for, list

#while True: #por padrão dura para sempre,essa estrutura
#  n = int(input("What's n"))
#  if n <0:
#      break
#for _ in range(n):
#  print("meow")


def main():
  number = get_number()
  meow(3)

def get_number():
  while True:
    n = int(input("What's n?"))
    if n >0:
      break
      return n
def meow(n):
  for _ in range(n):
    print("meow")
    
main()
