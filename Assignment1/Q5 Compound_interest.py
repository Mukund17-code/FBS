p = int(input('principle amount ='))
r = int(input('rate of intrest='))
t = int(input('time in year='))

compound_intrest = p*(1+(r/100))**t
print(f'compound intrest =',compound_intrest)