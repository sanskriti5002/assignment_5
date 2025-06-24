# 1.   Creates a list of numbers from 1 to 10.
# 2.   Extracts the first five elements from the list.
# 3.   Reverses these extracted elements.
# 4.   Prints both the extracted list and the reversed list
 

number =  list(range(1,11))
first_five = number[:5]
reversed_five = first_five[::-1]
print("Original list:",number)
print("Extracted first five element:", first_five)
print("reversed extracted element:",reversed_five)