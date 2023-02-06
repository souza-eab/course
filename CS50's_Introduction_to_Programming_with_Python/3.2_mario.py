# Utilizar os blocos do mario bros em code

#Ex 1 Criar os blocos ....
#def main():
#  print_square(3)
#
#def print_square(size):
#  
#  #For each row in square (Interação para cada loop, ou seja, para cada linha construida de tijolos, retorno apenas 
#  for i in range (size):
#    
#    #For each brick in row
#    for j in range(size):
#      
#      #Print brick
#      print("#", end="")
#      print() #1 pq esse print?
#main()


# Verificamos que os tijolos ainda é pequeno, mas bora ver quantas linhas fizemos para costruir: da para encurtar??
def main():
  print_square(3)
def print_square(size):
  for i in range (size):
      print("#"* size)
main()
