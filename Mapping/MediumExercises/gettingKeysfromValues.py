my_dict ={"java":100, "python":112, "c":11} 
  
# list out keys and values separately 
key_list = list(my_dict.keys()) 
val_list = list(my_dict.values()) 

print(key_list)
print(val_list)

print(key_list[val_list.index(112)])