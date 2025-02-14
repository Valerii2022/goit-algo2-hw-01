from task_1 import find_min_max

def quick_select(arr, k):
    if not (1 <= k <= len(arr)):
        raise ValueError("k має бути в межах довжини масиву")
    
    def partition(left, right):
        pivot = arr[right]
        i = left
        for j in range(left, right):
            if arr[j] <= pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[right] = arr[right], arr[i]
        return i
    
    left, right = 0, len(arr) - 1
    while left <= right:
        pivot_index = partition(left, right)
        if pivot_index == k - 1:
            return arr[pivot_index]
        elif pivot_index < k - 1:
            left = pivot_index + 1
        else:
            right = pivot_index - 1

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 3:
        print("Використання: python task_2.py k число1 число2 ...")
        sys.exit(1)
    
    try:
        k = int(sys.argv[1])
        arr = list(map(int, sys.argv[2:]))  
    except ValueError:
        print("Помилка: усі аргументи мають бути числами.")
        sys.exit(1)

    print("Мінімум і максимум:", find_min_max(arr))
    print(f"{k}-й найменший елемент:", quick_select(arr, k))