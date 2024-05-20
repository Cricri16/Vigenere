a = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!:/.;?,[]"
def letrechang(let):
    let = a.find(let)
    chang = a[let:] + a[:let]
    return chang
def lettr(lettrcle,loclett):
    bla =""
    var = letrechang(lettrcle)
    bla = var[loclett]
    return bla
def chifr(lettre,lettrcle):
    loclett = int(a.find(lettre))
    bla = lettr(lettrcle,loclett)
    return bla
def chifrgene(clxe,mot):
    result = ""
    depla = 0
    while len(clxe) <= len(mot):
        clxe = clxe + clxe
    for corect in mot :
        if a.find(corect) == -1:
            result = result + corect
        else:
            result = result + str(chifr(corect,str(clxe[depla])))
            depla = depla +1
    return result
def lettra(lettrcle,loclett):
    bla =""
    var = letrechang(lettrcle)
    bla = a[var.find(loclett)]
    return bla
def unchifrgene(clxe,mot):
    result = ""
    depla = 0
    while len(clxe) <= len(mot):
        clxe = clxe + clxe
    for corect in mot :
        if a.find(corect) == -1:
            result = result + corect
        else:
            result = result + str(lettra(str(clxe[depla]),corect))
            depla = depla +1
    return result
