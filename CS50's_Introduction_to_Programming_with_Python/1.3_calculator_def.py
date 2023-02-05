'''
Integrando tudo
'''
#Ex1
#def hello():
#  print('hello')
  
#Ask3 user for their name
#name = input ("Como gostaria de ser chamado, nome? ").strip() .title()

# Say3 hello to user
#print(f"Oiêee, ", {name})


#Ex2
#def hello(to):
#  print('hello,', to) 
#name = input ("Como gostaria de ser chamado, nome? ").strip().title()
#hello(name)


#Ex3
#def hello(to = 'World'):
#  print('hello,', to) 
  
#hello()
#name = input ("Como gostaria de ser chamado, nome? ").strip().title() ## e se comentar as linhas acima?
#hello(name)



#Ex4 Nada acontece
#def main():
#  name= input("Como gostaria de ser chamado, nome? ")
#  hello(name)
  
#def hello(to = 'World'):
#  print('hello,', to) 


#Ex4 Nada acontece
#def main():
#  name= input("Como gostaria de ser chamado, nome? ")
#  hello(name)
  
#def hello(to = 'World'):
#  print('hello,', to) 

#main()



#Ex5 Clear
def main():
  x= int(input('Whats x?'))
  print( 'x squared is', square(x))

def square(n):
  #return n ** 2 #** elevado ao quadrado
  return pow (n,2) # elevado ao quadrado
main()
  
