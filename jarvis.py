n = int(input()) 
lst = []
for i in range(0, n): 
    ele = int(input()) 
  
    lst.append(ele)
def split(word): 
    return [char for char in word]
for elment in lst:
    split_lst = split(str(elment))
    if '0' in split_lst:
        if int(max(split_lst)) < len(split_lst):
            print("YES")
        else:
            print("NO")
    else:
        if int(max(split_lst)) <= len(split_lst):
            print("YES")
        else:
            print("NO")




