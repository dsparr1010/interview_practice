# given two string, s and t, validate if t is a subsequnce of s
    #  *
# s = "sdaseeh"
s = "saseedh"
    #  *
t = "deh"


# if no match -> s++
# if match -> s++, t++
# if pt == len(t) -> t is subseq
# if pt == len(s) -> t is not subseq

def is_subsequence(s, t):
  if len(t) > len(s):
    return False
    
  s_ptr = 0
  t_ptr = 0
  # when t_ptr == len(t) and also s_ptr == len(s)
  while t_ptr < len(t):
    if s_ptr == len(s):
      return False
    if t[t_ptr] != s[s_ptr]:
      s_ptr += 1
    elif t[t_ptr] == s[s_ptr]:
      s_ptr += 1
      t_ptr += 1
      
  return True
    
    
  
print(is_subsequence(s, t))
