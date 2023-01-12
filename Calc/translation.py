    
def transl(num):

    x = num
    if x[-1] == 'j':
        num = 0
        ncom2 = float(x[:-1])

            
    if x[0]=='-':
        z = -1
    else:
        z = 1
    if x[0] == '-' or x[0]=='+':
        x = x[1:]

    if '+' in x:
        ncom1 = x.rpartition('+')[0] 
        ncom1 = ncom1[:-1]
                
        ncom2 = float(ncom1)*z
                
        cc = x.rpartition('+')[1] 
        num = float(x.rpartition('+')[2])
        if cc == '-':
            num = (-1)*num
    elif '-' in x:
        ncom1 = x.rpartition('-')[0] 
        ncom1 = ncom1[:-1]
                
        ncom2 = float(ncom1)*z
                
        cc = x.rpartition('-')[1] 
        num = float(x.rpartition('-')[2])*(-1) 
            
            
    comp_num = complex(num, ncom2)
    #print(comp_num)
    return comp_num
