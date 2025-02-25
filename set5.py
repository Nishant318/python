your_list = [1,5,1,2,3,7,2,5]
unique_list = []
[unique_list.append(x) for x in your_list if x not in unique_list]
