# Float = numeros decimaais 



# Ex1 (Daria para fazer em uma linha
#x = float(input("What's x? "))
#y = float(input("What's y? "))
#print (x+y) # Aí funciona pq declaramos como inteiro




# Ex2 (Arredondar números mais próximo
# Documentation :: round(number[, ndigits])
#x = float(input("What's x? "))
#y = float(input("What's y? "))

#z = round(x+y) #Fica bem documentado e aproxima para o mais próximo
#print (z) # Aí funciona pq declaramos como inteiro




# Ex3 (Numeros muito grande e utilizar separador decimal)
# Documentation :: round(number[, ndigits])
#x = float(input("What's x? "))
#y = float(input("What's y? "))

#z = round(x+y) #Fica bem documentado e aproxima para o mais próximo
#print (f"{z:,}") # Aí funciona pq declaramos como inteiro



# Ex4 ( Numa divisão arrendondar duas casas)
# Documentation :: round(number[, ndigits])
#x = float(input("What's x? "))
#y = float(input("What's y? "))

#z = round(x/y, 2) #Fica bem documentado e aproxima para o mais próximo
#print (z) # Aí funciona pq declaramos como inteiro




# Ex4 ( Numa divisão arrendondar duas casas mas formatando de outra forma no print)
# Documentation :: round(number[, ndigits])
x = float(input("What's x? "))
y = float(input("What's y? "))

z = x/y #Fica bem documentado e aproxima para o mais próximo
print (f"{z:.2f}") # Aí funciona pq declaramos como inteiro
