def division(code,pol):
    i=len(poly)
    temp=code[0:len(poly)]
    for j in range(0,len(code)-len(poly)):
        if(temp[0] != '0'):
            res=xor(temp,poly,len(poly))
            temp=res[1:]+code[i]
        else:
            temp=temp[1:]+code[i]
        i = i + 1
        print(temp)
    if(temp[0] != '0'):
            res=xor(temp,poly,len(poly))
            print(res[1:])
    else:
        print(temp[1:])
def xor(a, b, n):
    ans = ""
    for i in range(n):
        if (a[i] == b[i]):
            ans += "0"
        else:
            ans += "1"
    return ans
code = input("ENTER CODEWROD \n")
poly = "1010"
zeroes = "000"
modified_code = code+zeroes
division(modified_code,poly)

