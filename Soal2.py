def revereList(l):
    l_new = []
    for i in range(1,len(l)+1):
        l_new.append(l[-i])
    return(l_new)

list1 = [19,22,3,28,26,17,18,4,28,0]
print(revereList(list1))