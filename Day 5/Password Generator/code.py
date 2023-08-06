import random 
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


n_letter = int(input('How many letters you want?\n'))
n_number = int(input('How many number you want?\n'))
n_symbol = int(input('How many symbol you want?\n'))


pass_lst = []

for i in range(n_letter):
    pass_lst.append(random.choice(letters))

for i in range(n_number):
    pass_lst.append(random.choice(numbers))

for i in range(n_symbol):
    pass_lst.append(random.choice(symbols))

random.shuffle(pass_lst)

password = ''

for i in range(len(pass_lst)):
    password+=pass_lst[i]

print(f'Password is : {password}')