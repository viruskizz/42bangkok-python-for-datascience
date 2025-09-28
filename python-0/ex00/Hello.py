ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# your code here
# Update List
ft_list[1] = "World!"
# Update Tuple
ft_tuple_ls = list(ft_tuple)
ft_tuple_ls[1] = "Thailand"
ft_tuple = tuple(ft_tuple_ls)
# Update set
ft_set.add("Bangkok")
ft_set.remove("tutu!")
# Update dict
ft_dict["Hello"] = "42Bangkok"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
