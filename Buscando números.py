for números in range (1,11):
    print (números)

    # buscando números específicos
    for i in range(0,101,5):
        print(i)

        # dando pouse nos números 
        print('Loop com o break:')
        for número in range(1, 11):
            if número > 5:
                break
            print(número)
            print('Loop com o continue:')
            for número in range (1,11):
                if número == 5:
                    continue
                    print(número)