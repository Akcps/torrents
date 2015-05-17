def totalmatching(input1):
    women = dict()
    for ind, input in enumerate(input1):
        women[('W'+str(ind+1))] = False
    val = recursive_call(input1, 0, women)
    if val == 0:
        return -1
    return val

def recursive_call(input1, position, women_dict):
    try:
        if position == len(input1):
            return 1
        input = input1[position]
        value = input.split('#')
        if len(value) < 2:
            return 0
        total = 0
        for women in value[1:]:
            if not women_dict[women]:
                women_dict[women] = True
                val = recursive_call(input1, position+1, women_dict)
                total += val
                women_dict[women] = False
        return total
    except Exception,e:
        return -1









print totalmatching(['M1#W1#W2#W3','M2#W1#W2#W3'])





