
open_bra = ["(", "[", "{"]
close_bra = [")", "]", "}"]


def validate_brackets(value):

    braket_arr = []
    for k in value:
        if k in open_bra:
            braket_arr.append(k)
        elif k in close_bra:
            result = close_bra.index(k)
            if ((len(braket_arr) > 0) and (open_bra[result] == braket_arr[len(braket_arr)-1])):
                braket_arr.pop()
            else:
                return False
    if len(braket_arr) == 0:
        return True
    else:
        return False


group1 = "{[]{}}"
print(validate_brackets(group1))

group2 = "{[][{}}"
print(validate_brackets(group2))
