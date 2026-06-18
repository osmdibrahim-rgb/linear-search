# Sorting numbers based on user choice

numbers = [50, 20, 40, 10, 30]

choice = int(input("Enter 1 for Max to Min, Enter 2 for Min to Max: "))

if choice == 1:
    numbers.sort(reverse=True)  # Descending order
    print("Sorted list (Max to Min):", numbers)

elif choice == 2:
    numbers.sort()  # Ascending order
    print("Sorted list (Min to Max):", numbers)

else:
    print("Invalid choice! Please enter 1 or 2.")