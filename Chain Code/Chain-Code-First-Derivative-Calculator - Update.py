#Introduction to the product
print("This program calculates the shapenum of a chain code!")
#ask the user if it's a 4 code or 8 code
fourcode = input("Is this a four code mapping (y/n (default))\t") == 'y'
#advise user on how to enter the chain code
print("Please enter a token of the chain code, and hit enter afterwards.")
print("To end the chain please enter any character > max(mapping numbers(3 or 7)) ")


#ask the user for the chain code
scanning = True
chain = []
while(scanning):
    val = input("Enter next token\t")
    if(val.isnumeric()):
        if int(val) >= 0 and ((int(val) <= 7 and not fourcode) or (int(val) <= 3 and fourcode)):
            chain.append(int(val))
        else:
            scanning = False
    else:
        print("Hey I only take in natural numbers, don't do that >:(")
print('the chain code you input is: ' + str(''.join(str(i) for i in chain)))

#calculate the first derivative (immune to rotation)
fd_chain = []
for i in range(len(chain)):
    if not fourcode:
        if chain[i] >= chain[i - 1]:
            fd_chain.append(chain[i] - chain[i - 1])
        else:
            fd_chain.append(8 - (chain[i - 1] - chain[i]))
    if fourcode:
        if chain[i] >= chain[i - 1]:
            fd_chain.append(chain[i] - chain[i - 1])
        else:
            fd_chain.append(4 - (chain[i - 1] - chain[i]))
print('the first derivative is: ' + str(''.join(str(i) for i in fd_chain)))

#calculate the shape number by normalizing the chain code (immune to different start points)
import sys
min_num = str(sys.maxsize)
for i in range(len(fd_chain)):
    current_num = str(''.join(str(i) for i in fd_chain))
    if(int(current_num) < int(min_num)):
        min_num = current_num
    fd_chain = fd_chain[1:] + fd_chain[:1]
print('the shape number is: ' + min_num)