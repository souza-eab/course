'''
@Parameters

1.0_Functions_Variables.py

'''

#Comments
'''
Aqui seu texto
'''
#Ask user for their name
name = input ("Como gostaria de ser chamado, nome? ")

# Say hello to user
print("Oiêee, ", name)


#Ask2 user for their name
name = input ("Como gostaria de ser chamado, nome? ")

# Say2 hello to user
print("Oiêee, ", end='')
print(name)

# Official Documentation 
#print(*objects, sep=' ', end ='\n',  file = sys.stdout, flush = False)
#* >1 +1 objects


#Ask3 user for their name
name = input ("Como gostaria de ser chamado, nome? ").strip() .title()

# Spli user'ss name into first name and last name

first, last = name.split('')
  #Remove whitespace from str
#name = name.strip() .title()

  # Capitalize user's names (Maiscula)
# name = name.capitalize ()

  # Title user's names (Maiscula)
# name = name.title()


# Say3 hello to user
print(f"Oiêee, ", {name})


# Say4 hello to user
print(f"Oiêee, ", {first})
