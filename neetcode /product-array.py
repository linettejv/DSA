# given a an array, we need to print of the product of the array without that element
def product_array(arr: list[int]):
    prod = 1
    for i in arr:
        prod = prod * i
    new_arr = [prod] * len(arr)
    for i in range(len(new_arr)):
        new_arr[i] = new_arr[i]//arr[i]
    return(new_arr) 
    
print(product_array([1,2,3,4]))    

# done using prefix and postfix arrays. 
# extra array for result only taken

def product_array_optimial(arr : list[int]):
    res = [1] * len(arr)
    prefix = 1
    suffix = 1
    # making the prefix array :
    for i in range(len(arr)):
        res[i] = prefix
        prefix *= arr[i]

    # making the suffix array :
    for i in range(len(arr)-1, -1, -1):
        res[i] = res[i] * suffix
        suffix *= arr[i]

    return(res)  

print(product_array_optimial([1,2,3,4]))  