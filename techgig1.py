def admin_condition(scores, num):
    if len(scores) < num or num == 0 or len(scores) == 0:
        return -1
    grade = list()
    grade.append(1)
    current = 1
    prev = 0
    for index, score in enumerate(scores[:num-1]):
        val = score - (prev+current)
        grade.append(val)
        current = val
        prev = grade[index]
        if val > 1:
            return -1
    return val


val = admin_condition([2,2,2,2,1], 0)
print val






