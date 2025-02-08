
infix = 'a+b*(c-d)/'
infix = 'a*(b+c)-d/e' # 1*(9+1) - 6/3 = 8
infix = 'a+(b-c)*(d+e)' # 1+(2-1)*(3+5) = 9

from Wp import Wp

e = Wp.evaluatePostfix("191+*63/-")
print(e)

