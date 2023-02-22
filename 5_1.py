def dec2bin(deci: int)-> str:
    binar = ''
    while deci > 1:
        binar =f'{deci % 2}' + binar
        deci //= 2
    binar = f'{deci}' + binar
    return binar

