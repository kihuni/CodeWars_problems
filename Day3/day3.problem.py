def nb_year(p0,percent,aug,p):
    targeted_populations = p
    n = 0
    
    while p0 < targeted_populations:
        p0+=p0*percent/100+aug
        n+=1
        
    return n
years_needed = nb_year(1000,2,50,1200)

print(years_needed)

# output 3