total_heads = 35
total_legs = 94

# Lets suppose all of the heads are of chickens

chickens = 0
rabbits = total_heads


while total_legs != chickens*2+rabbits*4:
    print('Chickens =', chickens)
    print('Rabbits =', rabbits)
    if total_legs > chickens*2+rabbits*4:
        rabbits = rabbits+1
        chickens = chickens-1
        print('More rabbits required!')
    else:
        rabbits = rabbits-1
        chickens = chickens+1
        print('More chickens required!')

print('\nChickens =', str(chickens))
print('Rabbits =', str(rabbits))
print('Lets check this:')
print('No of chicken legs =', str(chickens*2))
print('No of rabbit legs =', str(rabbits*4))
print('Total legs =',str(chickens*2+rabbits*4))