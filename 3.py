def ingredientes(contPoFenix,contEsCelestial,contRaizDragão,contOrvLunar,contFloresSecas,contElixirA,contLaUnicorn):
    print('lista de ingredientes disponíveis:')
    print('Pó de Fênix:',contPoFenix,'g')
    print('Essência Celestial:',contEsCelestial,'ml')
    print('Raiz de Dragão:',contRaizDragão,'g')
    print('Orvalho Lunar:',contOrvLunar,'ml')
    print('Flores secas:',contFloresSecas,'g')
    print('Elixir amargo:',contElixirA,'ml')
    print('Lágrimas de unicórnio:',contLaUnicorn,'ml')
    print('')

def prepararPocao(contPoFenix,contEsCelestial,contRaizDragão,contOrvLunar,contFloresSecas,contElixirA,contLaUnicorn):
    print('lista de poções: ')
    print('1 - Poção de Cura: ingredientes-Pó de Fênix(30g),Essência Celestial(20ml),Flores secas(20g),Lágrimas de unicórnio(10ml)')
    print('2 - Poção Força da Floresta: ingredientes-Orvalho Lunar(20ml), Raiz de Dragão(30g), Flores secas(30g)')
    print('3 - Poção Sabedoria da Riqueza: ingredientes-Essência Celestial(30ml), Pó de Fênix(50g)')
    print('4 - Poção Sorte no Amor: ingredientes-Orvalho Lunar(10ml), Flores secas(50g), Lágrimas de unicórnio(5ml)')
    print('5 - Poção Malvada: ingredientes-Elixir amargo(10ml), Raiz de Dragão(15g)')
    escolha=int(input('digite o número da poção que deseja: '))
    if escolha==1:
        if contPoFenix>=15 and contEsCelestial >=20 and contFloresSecas>=20 and contLaUnicorn >=10:
            print('Poção de cura feita com SUCESSO')
            contPoFenix=contPoFenix-15
            contEsCelestial=contEsCelestial-20
            contFloresSecas=contFloresSecas-20
            contLaUnicorn=contLaUnicorn-10
        else:
            print('a Poção de cura não pode ser preparada pois está faltando: ')
            if not contPoFenix>=15:
                print('Pó de Fênix')
            if not contEsCelestial >=20:
                print('Essência Celestial')
            if not contFloresSecas>=20:
                print('Flores secas')
            if not contLaUnicorn >=10:
                print('Lágrimas de unicórnio')

    if escolha==2:
        if contOrvLunar>=20 and contRaizDragão>=30 and contFloresSecas>=30:
            print('Poção Força da Floresta feita com SUCESSO')
            contOrvLunar=contOrvLunar-20
            contRaizDragão=contRaizDragão-30
            contFloresSecas=contFloresSecas-30
        else: 
            print('a Poção Força da Floresta não pode ser preparada pois está faltando: ')
            if not contOrvLunar>=20:
                print('Orvalho Lunar')
            if not contRaizDragão>=30:
                print('Raiz de Dragão')
            if not contFloresSecas>=30:
                print('Flores secas')
    
    if escolha==3:
        if contEsCelestial>=30 and contPoFenix>=50:
            print('Poção Sabedoria da Riqueza feita com SUCESSO')
            contEsCelestial=contEsCelestial-30
            contPoFenix=contPoFenix-50
        else:
            print('a Poção Sabedoria da Riqueza não pode ser preparada pois está faltando: ')
            if not contEsCelestial>=30:
                print('Essência Celestial')
            if not contPoFenix>=50:
                print('Pó de Fênix')
    
    if escolha==4:
        if contOrvLunar>=10 and contFloresSecas>=50 and contLaUnicorn>=5:
            print('a Poçâo Sorte no Amor feita com SUCESSO')
            contOrvLunar=contOrvLunar-10
            contFloresSecas=contFloresSecas-50
            contLaUnicorn=contLaUnicorn-5
        else:
            print('a Poção Sorte no Amor não pode ser preparada pois está faltando: ')
            if not contOrvLunar>=10:
                print('Orvalho Lunar')
            if not contFloresSecas>=50:
                print('Flores secas')
            if not contLaUnicorn>=5:
                print('Lágrimas de unicórnio')
    
    if escolha==5:
        if contElixirA>=10 and contRaizDragão>=15:
            print('a Poção Malvada feita com SUCESSO')
            contElixirA=contElixirA-10
            contRaizDragão=contRaizDragão-15
        else:
            print('a Poção Malvada não pode ser preparada pois está faltando: ')
            if not contElixirA>=10:
                print('Elixir amargo')
            if not contRaizDragão>=15:
                print('Raiz de Dragão')
    print('')
    return(contPoFenix,contEsCelestial,contRaizDragão,contOrvLunar,contFloresSecas,contElixirA,contLaUnicorn)

#main
contPoFenix=100
contEsCelestial=50
contRaizDragão=45
contOrvLunar=30
contFloresSecas=200
contElixirA=20
contLaUnicorn=15
encerrar=False

while encerrar!=True:
    print('MENU:')
    print('')
    print('1 - preparar poção')
    print('2 - consultar os ingredientes disponíveis')
    print('0 - sair')
    print('')
    tarefa=int(input('digite a ação que deseja realizar: '))
    if tarefa==0:
        print('encerrando programa...')
        encerrar=True

    elif tarefa==2:
        ingredientes(contPoFenix,contEsCelestial,contRaizDragão,contOrvLunar,contFloresSecas,contElixirA,contLaUnicorn)
        encerrar=False

    elif tarefa==1:
        (contPoFenix,contEsCelestial,contRaizDragão,contOrvLunar,contFloresSecas,contElixirA,contLaUnicorn)=prepararPocao(contPoFenix,contEsCelestial,contRaizDragão,contOrvLunar,contFloresSecas,contElixirA,contLaUnicorn)
        encerrar=False
    else:
        print('Erro! use um dos números apresentados no menu')
        encerrar=False