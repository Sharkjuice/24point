def calc24 (cards_4):
    cards_3 = draw_3(cards_4)
    for a in cards_3 :
        half = calc_3(a[0])
        for b in half :
            c = last(a[1],b)
            if c != None :
                return c 
    
    cards_2 = draw_2(cards_4)
    for c in cards_2:
        ordered1 = sort_2(c[0])
        half1 = calc_2(ordered1)
        ordered2 = sort_2(c[1])
        half2 = calc_2(ordered2)

        for e in half1 :
        
             for f in half2 :
                g = last(e,f)
                return g 
 

   

def draw_2 (cards_4) :
    return [[[[cards_4[0]],[cards_4[1]]],[[cards_4[2]],[cards_4[3]]]],
            [[[cards_4[0]],[cards_4[2]]],[[cards_4[1]],[cards_4[3]]]],
            [[[cards_4[0]],[cards_4[3]]],[[cards_4[1]],[cards_4[2]]]]]

def draw_3 (cards_4) :
    return [[[cards_4[0],cards_4[1],cards_4[2]],[cards_4[3]]],
            [[cards_4[0],cards_4[1],cards_4[3]],[cards_4[2]]],
            [[cards_4[0],cards_4[2],cards_4[3]],[cards_4[1]]],
            [[cards_4[1],cards_4[2],cards_4[3]],[cards_4[0]]]]

def sort_2 (cards_2) :
    g = cards_2[0]
    f = cards_2[1]
    if g > f:
        return [g,f]
    return [f,g]

def calc_2 (cards_2) :
    r = []
    g = cards_2[0]
    f = cards_2[1]    
    a = g[0]
    b = f[0]    
    h = a + b
    r.append([h,["+",g,f]])
    i = a - b
    r.append([i,["-",g,f]])
    j = b - a 
    r.append([j,["-",f,g]])
    k = a * b
    r.append([k,["*",g,f]])
    if b != 0 :
        l = a / b
        r.append([l,["/",g,f]]) 
    if a != 0 :
        m = b / a
        r.append([m,["/",f,g]])
    return r

    
def draw_2_3 (cards_3) :
    return [[[[cards_3[0]],[cards_3[1]]],[cards_3[2]]],
            [[[cards_3[0]],[cards_3[2]]],[cards_3[1]]],
            [[[cards_3[1]],[cards_3[2]]],[cards_3[0]]]]
    
def calc_3 (cards_3) :
    r = []
    g = draw_2_3(cards_3)
    for h in g :
        i = calc_2([h[0][0],h[0][1]])
        for j in i :
            k = calc_2([j,h[1]])
            r = r + k
    return r 
        
def last (e,f) :
#    print (e,f)
    a = e[0]
    b = f[0]
    if a+b == 24 :
        return [24,["+",e,f]]

    if a-b == 24 :
        return [24,["-",e,f]]
        
    if b-a == 24 :
        return [24,["-",f,e]]
    if a*b == 24 :
        return [24,["*",e,f]]
        
def real (x) :
    r = ""
    if len(x) == 1 :
        r = r + str(x[0])
    else : 
        op = x[1][0]
        n_1 = x[1][1]
        n_2 = x[1][2]
        
        r = r + "(" + real(n_1) + op + real(n_2) + ")"
    return r
        
#b = calc24([5,5,12,6])
#if b != None :
#    print (b)
#    print (real(b))
#print ("No")

