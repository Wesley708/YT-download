data = [
    84, 12, 57, 43, 25, 68, 91, 7, 36, 50,
    74, 29, 88, 62, 15, 97, 41, 3, 80, 19,
    33, 59, 46, 21, 70, 90, 11, 55, 5, 65,
    38, 17, 83, 48, 24, 77, 8, 93, 30, 61,
    14, 71, 44, 26, 87, 10, 53, 2, 82, 31,
    40, 20, 69, 92, 16, 76, 6, 58, 27, 86,
    13, 52, 1, 81, 32, 42, 22, 66, 95, 18,
    75, 9, 60, 28, 85, 35, 47, 23, 79, 4,
    94, 34, 73, 45, 63, 98, 39, 64, 49, 72,
    0, 89, 37, 56, 78, 96, 67, 99, 54, 85
]

row = sorted(data)
print(row)

dez = 0
vinte = 0
trinta = 0
quarenta = 0
cinquenta = 0
sesenta = 0
setenta = 0
oitenta = 0
noventa = 0
cem = 0

for element in row:
    if element < 10:
       dez += 1
    elif element < 20 and element >= 10:
        vinte += 1    
    elif element < 30 and element >= 20:
        trinta += 1    
    elif element < 40 and element >= 30:    
        quarenta += 1    
    elif element < 50 and element >= 40:    
        cinquenta += 1    
    elif element < 60 and element >= 50:    
        sesenta += 1    
    elif element < 70 and element >= 60:    
        setenta += 1    
    elif element < 80 and element >= 70:    
        oitenta += 1
    elif element < 90 and element >= 80:    
        noventa += 1
    elif element < 100 and element >= 90:    
        cem += 1 
        
print(f'0-9: {dez}')
print(f'10-19: {vinte}')
print(f'20-29: {trinta}')
print(f'30-39: {quarenta}')
print(f'40-49: {cinquenta}')
print(f'50-59: {sesenta}')
print(f'60-69: {setenta}')
print(f'70-79: {oitenta}')
print(f'80-89: {noventa}')
print(f'90-99: {cem}')