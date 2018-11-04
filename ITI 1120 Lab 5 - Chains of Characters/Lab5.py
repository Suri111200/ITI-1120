def Chains1():
    s1 = "Good"
    s2 = "Bad"
    s3 = "Crazy"

    if 'azy' in s3:
        print ("There is \'azy\' in \'crazy\'")
    else:
        print ("There is not \'azy\' in \'crazy\'")

    if ' ' in s1:
        print ("There is a space in \'Good\'")
    else:
        print ("There is is not a space in \'Good\'")

    print ("The concatenation of all strings is", s1+s2+s3)

    if ' ' in s1+s2+s3:
        print ("There is a space in the concatenation of all strings")
    else:
        print ("There is not a space in the concatenation of all strings")
    
    print("Crazy repeated 10 times: ", s3*10)

    print ("The number of chars in all chains: ",len(s1) + len(s2) + len(s3))

def Chains2():

    aha = 'abcdefgh'

    if 'abcd' in aha:
        print ("\'abcd\' is in variable")
    else:
        print ("\'abcd\' is not in variable")
    if 'def' in aha:
        print ("\'def\' is in variable")
    else:
        print ("\'def\' is not in variable")
    if 'h' in aha:
        print ("\'h\' is in variable")
    else:
        print ("\'h\' is not in variable")
    if 'fg' in aha:
        print ("\'fg\' is in variable")
    else:
        print ("\'fg\' is not in variable")
    if 'defgh' in aha:
        print ("\'defgh\' is in variable")
    else:
        print ("\'defgh\' is not in variable")
    if 'adg' in aha:
        print ("\'adg\' is in variable")
    else:
        print ("\'adg\' is not in variable")
    if 'bd' in aha:
        print ("\'bd\' is in variable")
    else:
        print ("\'bd\' is not in variable")

def Chains3():
    s = ''' En 1815, M. Charles-François-Bienvenu Myriel était évêque de
    Digne. C’était un vieillard d’environ soixante-quinze ans ; il occupait le
    siège de Digne depuis 1806. … '''
    nS = s.replace('.',' ').replace(',',' ').replace(';',' ')
    print(nS)
    nS = nS.strip()
    print (nS)
    nS = nS.lower()
    print (nS)
    print (nS.count ('de'))
    nS = nS.replace ('était','est')
    print (nS)

def Count(s,c):
    return s.count(c)

def ForCount (s,c):
    num = 0
    for i in range (len(s)):
        if s[i] == c:
            num = num+1
    return num

def Spaces(s):
    return " ".join(s)

def code(s):
    nS = ''
    for i in range (0, len(s),2):
        #Error control, if odd number of letters retain last letter as is
        if i+1 == len(s):
            nS+= s[i]
        else:
            nS+= s[i+1]+s[i]
    return nS
