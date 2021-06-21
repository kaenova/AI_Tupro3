def kFold(list, totalFold):
    # Pre-requisite check
    if totalFold > len(list):
        raise Exception("TotalFold can't be more than total element in the list")

    # Variable initialization
    fold = []
    current_element = 0
    element_per_fold = len(list) // totalFold
    modulus_counter = len(list) % totalFold

    # Making a fold
    for i in range(totalFold):
        temp_fold = []
        if modulus_counter > 0:
            temp_fold.append(list[current_element])
            modulus_counter -= 1
            current_element += 1
        for j in range(current_element, current_element + element_per_fold):
            temp_fold.append(list[j])
            current_element += 1
        fold.append(temp_fold)

    # by Kaenova Mahendra Auditama
    # https://github.com/kaenova
    # If you're using this in your code, please credit the owner by write the 2 comments above

    return fold