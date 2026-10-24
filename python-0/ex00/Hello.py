ft_list = ["Hello"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# your code here
# Update List
ft_list.append("World!")
# Tuples has created to new one with concrete values by +
ft_tuple = ft_tuple[:1] + ("Thailand!",)
# Update set
ft_set.add("Bangkok!")
ft_set.remove("tutu!")
# Update dict
ft_dict["Hello"] = "42Bangkok!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
