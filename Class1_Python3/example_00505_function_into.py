def subtraction(number_1, number_2):
    result = number_1 - number_2
    return result

def difference(number_1, number_2):
    result = number_1 - number_2
    if result>=0:
        return result
    else:
        return -result

#assertions fehlen (siehe Slack) assertions sind Tests! Erst wenn man Tests gemacht hat, Code schreiben

difference(-2, 3)

print("Succes!")

