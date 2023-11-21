def convertBase(n, base):
   convertString = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
   if n < base:
      return convertString[n]
   else:
      return convertBase(n//base, base) + convertString[n % base]

t = int(input())
for _ in range(t):
   n, b = map(int, input().split())
   print(convertBase(n, b))
