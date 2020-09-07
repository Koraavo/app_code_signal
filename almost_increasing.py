def almostIncreasingSequence(sequence):
    preNum = -999999
    for i in range(len(sequence)):
        num = sequence[i]
        if not num > preNum:
            index = i
            seq1 = sequence[:index] + sequence[index+1:]
            seq2 = sequence[:index+1] + sequence[index + 1 + 1:]
            seq3 = sequence[:index-1] + sequence[index + 1-1:]
            if increasingSequence(seq1) or increasingSequence(seq2) or increasingSequence(seq3):
                return True
    return False

def increasingSequence(sequence):
    preNum = -999999
    for num in sequence:
        if not num>preNum:
            return False
        preNum = num


sequence = [1, 2, 3, 4, 5, 3, 5, 6]
print(almostIncreasingSequence(sequence))