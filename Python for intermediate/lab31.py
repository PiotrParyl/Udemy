"""
Na przekręcie z wpłatomatem z poprzedniego zadania postanawiasz wraz ze swoim szefem otworzyć linie lotnicze "Flying Python". Linie będą krajowe. Oto wykaz portów lotniczych:

ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']
1. Zbuduj listę tupletów symbolizujących port początkowy i końcowy. Wykonaj połączenie każdy-z-każdym

2. Wyeliminuj z powyższej listy połączenie z portu do tego samego portu

3. Ponieważ połączenie z A do B dubluje się z połączeniem z B do A - wygeneruj możliwe połączenia krajowe pomijając takie zdublowane trasy.

4. Policz ilość generowanych połączeń w krokach 1,2,3

"""



ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
            'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

def port_to_port(posrts):

    
    lista_1 = [[a,b] for a in ports for b in ports]

    return lista_1



print(port_to_port(ports))



def clear_list(lista):
    test_list = []
    dowyjebanie = []
    for i in lista:
        if i[0] == i[1]:
            del lista
        
    return lista

clear_list(port_to_port(ports))

