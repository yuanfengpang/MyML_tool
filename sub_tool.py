__author__ = 'yuanfeng pang'

def isnumber(aString):
    try:
        float(aString)
        return True
    except:
        return False

def regulation(adr):
    adr = str(adr).replace('ー','－')
    adr = str(adr).replace(' ','')
    return adr

def check_repeat(seq1, seq2):
    res = []
    for x in str(seq1):
        if x in str(seq2):
            res.append(x)
    #print(res)  
    return len(res)