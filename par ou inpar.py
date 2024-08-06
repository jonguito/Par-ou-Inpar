numero = int(input('Me diga um número qualquer: '))
par_inpar =  numero % 2
if par_inpar == 0 :
    print(f'O número {numero} é PAR.')
elif par_inpar != 0:
    print(f'O número {numero} é ÍNPAR.')
