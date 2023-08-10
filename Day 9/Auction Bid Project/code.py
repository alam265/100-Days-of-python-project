dic = {}

print("Welcome to the Secret Auction programm ")

while True:
    name = input('What is your name? : ')
    bid = float(input("What's your bid?: "))
    ip = input("Are there any other bidders? type 'yes' or 'no': ").lower()
    if ip == 'yes':
        dic[name] = bid
    elif ip == 'no':
        break
    else:
        print('Please Enter valid word')
        ip = input("Are there any other bidders? type 'yes' or 'no': ").lower()
        if ip == 'yes':
            dic[name] = bid
        elif ip == 'no':
            break


max_bid = 0
for k,v in dic.items():
    if v > max_bid:
        max_bid = v 

print(f"Auction is winned by {k} with a bid of {v}")


        