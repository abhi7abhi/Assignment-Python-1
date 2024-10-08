#write a program to determine the female population at the end of each year in the last decade. 
# initial population is 1,00,000.  The population increases by 5% per year in the last decade.

population=100000
for year in range(1,11):   #stops at 10
    population+=(population*0.05)
    print(f"Year {year}: {int(population)} women employees")
