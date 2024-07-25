def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    counter = 0
 
    while low <= high:
        counter += 1
        mid = (high + low) // 2

        # Порівняння значень з урахуванням допустимої похибки
        if abs(arr[mid] - x) < 1e-9: 
            return (counter, mid)
        
        # якщо x більше за значення посередині списку, ігноруємо ліву половину
        elif arr[mid] < x:
            low = mid + 1
 
        # якщо x менше за значення посередині списку, ігноруємо праву половину
        elif arr[mid] > x:
            high = mid - 1
 
    # якщо елемент не знайдений
    return (counter, -1)

arr = [0.1, 0.5, 1.3, 1.5, 2.2, 3.4, 4.8, 5.9]
x = 1.2
result = binary_search(arr, x)
if result[1] != -1:
    print(f"Element is present at index {result[0]}, in {result[1]} iterations")
else:
    print(f"Element is not present in array, in {result[0]} iterations")
