class Soltuion:
    def deletion_distance(self,str1,str2):
        len1 = len(str1)
def deletion_distance(str1, str2):
  len1 = len(str1)
  len2 = len(str2)
  result_max = 0
  def helper_function(index1,index2,same_sofar,result_max):
    if index1==len1 or index2 ==len2:
      result_max = max(result_max,same_sofar)
      return result_max
    for ind1 in range(index1,len1):
      for ind2 in range(index2,len2):
        if str1[ind1]==str2[ind2]:
          return helper_function(ind1+1,ind2+1,same_sofar+1,result_max)
  return len1+len2-2*helper_function(0,0,0,result_max)