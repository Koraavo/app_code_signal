from insert_extended import Element

# elements to be inserted
elements = ['(', ')', '-', " "]
# original_positions
pos = [0, 3, 6, 6]
# list where you need the elements inserted
n = [8, 9, 9, 1, 5, 4, 3, 6, 2, 1]
# # # Desired output: ['(', 8, 9, 9, ')', 1, 5, 4, '-', ' ', 3, 6, 2, 1]

print(Element.insert_multiple_elements(n, pos, elements))

###
#
# list = ["a", "b", "c"]

