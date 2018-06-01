
def comb(k, n):
   l_masseur = []
   i = 0
   while i < k:
      l_masseur.append(1)
      i = i + 1
   i = 0
   while l_masseur[k - 1] <= n:
      if l_masseur[0] <= n:
         print("combinaison num " + str(int(i)) + " = " + str(l_masseur) + "\n")
      index = 0
      while index < k - 1:
         if l_masseur[index] > n:
            l_masseur[index] = 1
            if index == 0:
               l_masseur[index] = 0
            l_masseur[index + 1] = l_masseur[index + 1] + 1
         index = index + 1
      l_masseur[0] = l_masseur[0] + 1
      i = i + 1

if __name__ == "__main__":
   comb(4, 50)