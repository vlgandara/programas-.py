def soma_hipotenusas(n):
    hip,soma = 1,0
    while hip <= n:
        c_o,c_a = 1,1     
        while c_o < n:
            while c_a < n:
                if hip**2 == c_o**2 + c_a**2:
                    soma,c_o = soma+hip,n; break
                c_a = c_a + 1
            c_o,c_a = c_o+1,c_o
        hip = hip + 1
    return soma
