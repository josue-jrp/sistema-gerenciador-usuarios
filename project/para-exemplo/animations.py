import time
def simple_loading(x=3, y=1, z="#"):
    '''
        x = a quantidade de caracteres que irão aparecer a cada carregamento
        y = a quantidade de segundos que terá o loading
        z = o caractere que será mostrado
    '''

    for c in range(x+1):
        print(f"{z}"*c)
        time.sleep(y)