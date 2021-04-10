from math import gcd
def modulus_gcd_check(moduli):
    x = gcd(moduli[0],moduli[1])

    for i in range(len(moduli)):
        if(gcd(moduli[i],x)!=1):
            print('moduli are not pairwise corpime')
            exit()
    return True


num_of_equations = int(input('number of equations: '))

values_of_m = []
for t in range(num_of_equations):
    n = int(input('give the values of m: '))
    values_of_m.append(n)

if modulus_gcd_check(values_of_m) !=1:
    exit()

values_of_a = []
for h in range(num_of_equations):
    a = int(input('give the values of a: '))
    values_of_a.append(a)

M = 1
M_i = []
for g in values_of_m:
    M*=g
for g in values_of_m:
    M_i.append(M//g)


y_i = []
for l in range(len(M_i)):
    y_i.append(pow(M_i[l],-1,values_of_m[l]))

X_product = 0
for q in range(len(y_i)):
    X_product+=M_i[q]*y_i[q]*values_of_a[q]
X = X_product%M
print(X)
