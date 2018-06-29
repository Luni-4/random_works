# Esercizi 1 2 e 3

import calendar
from datetime import date 

def years(d):
    return d.year if calendar.isleap(d.year) else years(d.year+1)
    
def order(di):
	temp = sorted([elem for elem in di if isinstance(elem,int)])
	return [di[di.index(temp[elem//2])-1] if (elem % 2 == 0) else temp[elem//2] for elem in range(len(di))] 

def order_dict(a,b):
	m = a.copy()
	m.update(b)	
	#return list((elem,m[elem]) for elem in sorted(m.keys()))
	return sorted(m.items(), key = lambda x: x[0])	
	
def identity(n):
	return [y*[0] + [1] + ((n-1)-y)*[0] for y in range(n)]
	
def square(n):
	return [[(n)*y + (x+1) for x in range(n)] for y in range(n)]
	
	
def transpose(m):	
	return [[m[x][y] for x in range(len(m))] for y in range(len(m[0]))]
	
def multiply(a,b):
	return [[sum([m * n for m, n in zip(x, z)]) for z in b.transpose()] for x in a]
	
if __name__ == "__main__":
    d = date.today()
    # Esercizio 3
    print(years(d))    
    # Esercizio 4
    print(calendar.leapdays(2000,2050))
    # Esercizio 5
    print(calendar.day_name[calendar.weekday(2016, 7, 29)])
    
    '''Esercizio 6 versione 1
    alkaline_earth_metals = ["barium", 56, "beryllium", 4, "calcium", 20, "magnesium", 12, "radium", 88, "strontium", 38]
    print(max([elem for elem in alkaline_earth_metals if isinstance(elem,int)]))'''
    
    #Esercizio 6 versione 2
    
    alkaline_earth_metals1 = [('barium', 56), ('beryllium', 4), ('calcium', 20),('magnesium', 12), ('radium', 88), ('strontium', 38)]    
    print(sorted(alkaline_earth_metals1, key = lambda x: x[1], reverse=True)[0][1])   
    
    
    '''Esercizio 7 versione 1
    print(order(alkaline_earth_metals))'''
    
    #Esercizio 7 versione 2
    print(sorted(alkaline_earth_metals1, key = lambda x: x[1])) 
    
    '''Esercizio 8 versione 1
    alkaline = {alkaline_earth_metals[elem]: alkaline_earth_metals[elem+1] for elem in range(len(alkaline_earth_metals)) if (elem % 2 == 0)} 
    print(alkaline)'''
    
    #Esercizio 8 versione 2 
    alkaline_earth_metals1 = dict(alkaline_earth_metals1)
    print(alkaline_earth_metals1)
    
    noble_gases = {"helium": 2, "neon": 10, "argon": 18, "krypton": 36, "xenon": 54, "radon": 86}
    
    #Esercizio 9 versione 1    
    print(order_dict(alkaline_earth_metals1, noble_gases))
    
    # Esercizio 10
    print(identity(3))
    
    # Esercizio 11
    print(square(3))
    
    # Esercizio 12
    print(transpose(square(3)))
    
    mat = [[1, 2], [4, 5], [7, 8]]
    #Esercizio 13
    print(multiply(square(3), mat))
    
    
    
    
    
    
    
