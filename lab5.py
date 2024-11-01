
def second_largest(nums):
    if len(nums) < 2 or all(num == nums[0] for num in nums):
        return "No second largest element"
    else:
        return sorted(nums)[-2]

def main_1():
    nums = [2,3,6,2,5,6,8]
    print(second_largest(nums))
    
    
    
def duplicates(arr):
    
    for i in arr:
        try:   
            if arr[i] == arr[i+1]:
                return True
        except IndexError:
            if arr[-1] == arr[-2]:
                return True
            else:
                return False
    return False

def main_2():
    arr = [1,3,4,5,6,8]
    print(duplicates(arr))



def missing_num(n):

    for i in range(1, n[-1]):
        if i not in n:
            return i
    

def main_3():
    arr = [1,2,3,4,5,6,8]
    print(missing_num(arr))
    
    
    
def merge(arr1,arr2):
    
    merged = arr1 + arr2
    
    for i in range(len(merged)):
        for j in range(0, len(merged)-i-1):
            if merged[j] > merged[j+1]:
                merged[j], merged[j+1] = merged[j+1], merged[j]
    return merged
    
    
def main_4():
    arr1 = [64, 34, 25, 12, 22, 11, 90]
    arr2 = [33,45,32,1,3]
    print(merge(arr1,arr2))

    
    
    
    
def intersection(arr1, arr2):
    intersections = []
    for a,b in zip(arr1,arr2):
        if a == b:
            intersections.append(a)
    return intersections
    
    
def main_5():
    arr1 = [1,2,3,7,15]
    arr2 = [1,10,3,8,15]
    print(intersection(arr1,arr2))

#main_1()
#main_2()
#main_3()
#main_4()
#main_5()




    
