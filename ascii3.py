val='ABcTuuo'
for x in val:
    ord_val=ord(x)
    if ord_val in range(65,91):
        print(chr(ord_val+32),end='')
    elif ord_val in range(97,123):
        print(chr(ord_val-32),end='')
    else:
        print(x,end='')