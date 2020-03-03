l = ["Hippo", 3, "Camel", 5 ]
def filter_list(l):
    result = []
    for item in l:
        if isinstance(item,int):
            result.append(item)
    return result
    print(result)

filter_list(l)