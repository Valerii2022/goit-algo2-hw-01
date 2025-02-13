import sys

def find_min_max(arr):
    def divide_and_conquer(left, right):
        if left == right:
            return arr[left], arr[left]
        
        if right - left == 1:
            return min(arr[left], arr[right]), max(arr[left], arr[right])
        
        mid = (left + right) // 2
        min1, max1 = divide_and_conquer(left, mid)
        min2, max2 = divide_and_conquer(mid + 1, right)
        
        return min(min1, min2), max(max1, max2)
    
    if not arr:
        raise ValueError("Масив не може бути порожнім")
    
    return divide_and_conquer(0, len(arr) - 1)

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Використання: python script.py число1 число2 ...")
        sys.exit(1)

    try:
        arr = list(map(float, sys.argv[1:]))  
    except ValueError:
        print("Помилка: усі аргументи мають бути числами (цілими або дробовими).")
        sys.exit(1)

    print(find_min_max(arr))
