a = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
b = "BCDEFGHIJKLMNOPQRSTUVWXYZAbcdefghijklmnopqrstuvwxyza"
c = "CDEFGHIJKLMNOPQRSTUVWXYZABcdefghijklmnopqrstuvwxyzab"
d = "DEFGHIJKLMNOPQRSTUVWXYZABCdefghijklmnopqrstuvwxyzabc"
e = "EFGHIJKLMNOPQRSTUVWXYZABCDefghijklmnopqrstuvwxyzabcd"
f = "FGHIJKLMNOPQRSTUVWXYZABCDEfghijklmnopqrstuvwxyzabcde"
g = "GHIJKLMNOPQRSTUVWXYZABCDEFghijklmnopqrstuvwxyzabcdef"
h = "HIJKLMNOPQRSTUVWXYZABCDEFGhijklmnopqrstuvwxyzabcdefg"
i = "IJKLMNOPQRSTUVWXYZABCDEFGHijklmnopqrstuvwxyzabcdefgh"
j = "JKLMNOPQRSTUVWXYZABCDEFGHIjklmnopqrstuvwxyzabcdefghi"
k = "KLMNOPQRSTUVWXYZABCDEFGHIJklmnopqrstuvwxyzabcdefghij"
l = "LMNOPQRSTUVWXYZABCDEFGHIJKlmnopqrstuvwxyzabcdefghijk"
m = "MNOPQRSTUVWXYZABCDEFGHIJKLmnopqrstuvwxyzabcdefghijkl"
n = "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
o = "OPQRSTUVWXYZABCDEFGHIJKLMNopqrstuvwxyzabcdefghijklmn"
p = "PQRSTUVWXYZABCDEFGHIJKLMNOpqrstuvwxyzabcdefghijklmno"
q = "QRSTUVWXYZABCDEFGHIJKLMNOPqrstuvwxyzabcdefghijklmnop"
r = "RSTUVWXYZABCDEFGHIJKLMNOPQrstuvwxyzabcdefghijklmnopq"
s = "STUVWXYZABCDEFGHIJKLMNOPQRstuvwxyzabcdefghijklmnopqr"
t = "TUVWXYZABCDEFGHIJKLMNOPQRStuvwxyzabcdefghijklmnopqrs"
u = "UVWXYZABCDEFGHIJKLMNOPQRSTuvwxyzabcdefghijklmnopqrst"
v = "VWXYZABCDEFGHIJKLMNOPQRSTUvwxyzabcdefghijklmnopqrstu"
w = "WXYZABCDEFGHIJKLMNOPQRSTUVwxyzabcdefghijklmnopqrstuv"
x = "XYZABCDEFGHIJKLMNOPQRSTUVWxyzabcdefghijklmnopqrstuvw"
y = "YZABCDEFGHIJKLMNOPQRSTUVWXyzabcdefghijklmnopqrstuvwx"
z = "ZABCDEFGHIJKLMNOPQRSTUVWXYzabcdefghijklmnopqrstuvwxy"

def chifr(lettre,lettrcle):
    #on localise d'abord lettre dans a pour avoir sa position
    loclett = int(a.find(lettre))
    # on prend cette lettre dans la liste de la letre de chifr
    if "a" == lettrcle :
        bla = a[loclett]
    else:
        if "b" == lettrcle :
            bla = b[loclett]
        else:
            if "c" == lettrcle :
                bla = c[loclett]
            else:
                if "d" == lettrcle :
                    bla = d[loclett]
                else:
                    if "e" == lettrcle :
                        bla = e[loclett]
                    else:
                        if "f" == lettrcle :
                            bla = f[loclett]
                        else:
                            if "g" == lettrcle :
                                bla = g[loclett]
                            else:
                                if "h" == lettrcle :
                                    bla = h[loclett]
                                else:
                                    if "i" == lettrcle :
                                        bla = i[loclett]
                                    else:
                                        if "j" == lettrcle :
                                            bla = j[loclett]
                                        else:
                                            if "k" == lettrcle :
                                                bla = k[loclett]
                                            else:
                                                if "l" == lettrcle :
                                                    bla = l[loclett]
                                                else:
                                                    if "m" == lettrcle :
                                                        bla = m[loclett]
                                                    else:
                                                        if "n" == lettrcle :
                                                            bla = n[loclett]
                                                        else:
                                                            if "o" == lettrcle :
                                                                bla = o[loclett]
                                                            else:
                                                                if "p" == lettrcle :
                                                                    bla = p[loclett]
                                                                else:
                                                                    if "q" == lettrcle :
                                                                        bla = q[loclett]
                                                                    else:
                                                                        if "r" == lettrcle :
                                                                            bla = r[loclett]
                                                                        else:
                                                                            if "s" == lettrcle :
                                                                                bla = s[loclett]
                                                                            else:
                                                                                if "t" == lettrcle :
                                                                                    bla = t[loclett]
                                                                                else:
                                                                                    if "u" == lettrcle :
                                                                                        bla = u[loclett]
                                                                                    else:
                                                                                        if "v" == lettrcle :
                                                                                            bla = v[loclett]
                                                                                        else:
                                                                                            if "w" == lettrcle :
                                                                                                bla = w[loclett]
                                                                                            else:
                                                                                                if "x" == lettrcle :
                                                                                                    bla = x[loclett]
                                                                                                else:
                                                                                                    if "y" ==  lettrcle:
                                                                                                        bla = y[loclett]
                                                                                                    else:
                                                                                                        if "z" ==  lettrcle:
                                                                                                            bla = z[loclett]
    return bla
def chifrgene(clée,mot):
    result = ""
    depla = 0
    while len(clée) <= len(mot):
        clée = clée + clée
    for corect in mot :
        result = result + str(chifr(corect,str(clée[depla])))
        depla = depla +1
    return result
print(chifrgene("lol","rob"))