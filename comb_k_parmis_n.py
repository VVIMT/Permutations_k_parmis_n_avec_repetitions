
def comb(k, n):
   l_elem = []
   i = 0
   while i < k:
      l_elem.append(1)
      i = i + 1
   i = 0
   while l_elem[k - 1] <= n:
      if l_elem[0] <= n:
         print("combinaison num " + str(int(i)) + " = " + str(l_elem) + "\n")
      index = 0
      while index < k - 1:
         if l_elem[index] > n:
            l_elem[index] = 1
            if index == 0:
               l_elem[index] = 0
            l_elem[index + 1] = l_elem[index + 1] + 1
         index = index + 1
      l_elem[0] = l_elem[0] + 1
      i = i + 1

if __name__ == "__main__":
   comb(4, 50)