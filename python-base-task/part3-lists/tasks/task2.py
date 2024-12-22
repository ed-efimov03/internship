def change_el(arr: list) -> list:
    if len(arr) == 0:
        return arr
    elif len(arr) == 1:
        arr = ["SINGLE"]
        return arr
    else:
        arr[0] = "START"
        arr[-1] = "END"
        return arr

lst = ["apple", "banana", "cherry"]    
print(change_el(lst))