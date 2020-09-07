def almostIncreasingSequence(sequence):
    # create two copies of the list
    list1 = sequence[:]
    list2 = sequence[:]

    # list1 = original_list - first number from bad_pair
    # list2 = original_list - second number from bad_pair
    count = 0
    number = bad_pair(sequence)
    # print(number)
    if number == -1:
        return True
    if number == -5:
        return False
    removed1 = list1.pop(number)
    removed2 = list2.pop((number+1))

    # checking list1
        # if greater/equal number pair increase count
    for i in range(len(list1)-1):
        if list1[i] >= list1[i+1]:
            count += 1
    # checking list1
    # if greater/equal number pair increase count

    for i in range(len(list2)-1):
        if list2[i] >= list2[i+1]:
            count += 1
            
    # if count == 2, both tests failed
    if count == 2:
        return False
    return True


def bad_pair(sequence):
    # create two lists of pairs
    # all_pairs list and only the bad_pair list
    sequence_pairs = []
    all_pairs = []
    if len(sequence) <= 1:
        return -1 # sequence is increasing if length of the sequence <=1

    # creating all sequence pairs and adding them to all_pairs
    for i in range(len(sequence) - 1):
        sequences = [sequence[i], sequence[i + 1]]
        all_pairs.append(sequences)
    # print(all_pairs)

    # checking which sequence pair is bad
        # if bad_pair >=2:
            # return False
        # if bad_pair == 1:
            # return index of the pair, index_pair == index_larger_number
    for i in range(len(sequence) - 1):
        if sequence[i] >= sequence[i + 1]:
            sequences = [sequence[i], sequence[i + 1]]
            sequence_pairs.append(sequences)

    if len(sequence_pairs) == 1:
        if sequence_pairs[0] in all_pairs:
            return all_pairs.index(sequence_pairs[0]) # index
    if len(sequence_pairs) > 1:
        return -5 # False
    return -1 # True

sequence = [1, 2, 3, 4, 5, 3, 5, 6]
print(almostIncreasingSequence(sequence))