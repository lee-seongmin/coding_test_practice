"""
1번 풀이
"""
def solution(numer1, denom1, numer2, denom2):
    b = (numer1*denom2+numer2*denom1) # 분자
    c = (denom1*denom2) # 분모
    def gcd(a,b):
        while b > 0:
            a,b = b, a % b
        return a
    x = gcd(b,c)
    answer = [b/x,c/x]

    return answer
"""
2번 풀이
"""
from fractions import Fraction

def solution(denum1, num1, denum2, num2):
    answer = Fraction(denum1, num1) + Fraction(denum2, num2)
    return [answer.numerator, answer.denominator] # 분자, 분모

"""
3번 풀이
"""
import math

def solution(denum1, num1, denum2, num2):
    denum = denum1 * num2 + denum2 * num1 # 분자
    num = num1 * num2 # 분모
    gcd = math.gcd(denum, num)
    return [denum//gcd, num//gcd]
