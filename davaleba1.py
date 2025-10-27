


def procesis_data(data, gare_gasaxebi = None, shida_gasaxebi = None, condition = None):

    if gare_gasaxebi is None or gare_gasaxebi not in data:
        print("gare gasaxebi ar chans")
        return None

    if shida_gasaxebi is None:
        girebulebebi = data[gare_gasaxebi]
    else:
        if shida_gasaxebi not in data[gare_gasaxebi]:
            print("shida gasaxebi ar aris")
            return None
        girebulebebi =  data[gare_gasaxebi][shida_gasaxebi]

    if condition is not None:
        girebulebebi = [x for x in girebulebebi if condition(x)]
    
    if len(girebulebebi) == 0:
        return 0
    return sum(girebulebebi) / len(girebulebebi)


magaliti_1 = {
    'nums' : [12,23,25,30,33]
}

result1 = procesis_data(
    data = magaliti_1,
    gare_gasaxebi= 'nums',
    condition= lambda x: str(x).endswith('3')
)

print('magaliti 1 shedegi: ', result1)


magaliti_2 = {
    'group1' : {
        'a':[10,20,30],
        'b':[40,50,60]
    }
}

result2 = procesis_data(
    data = magaliti_2,
    gare_gasaxebi= 'group1',
    shida_gasaxebi= 'b',
    condition= lambda x: x != 0
)

print("magaliti 2 shedegi: ", result2)