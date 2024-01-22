#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    lists = []
    for i in range(list_length):
        try:
            newlist = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            newlist = 0
        except ZeroDivisionError:
            print("division by 0")
            newlist = 0
        except IndexError:
            print("out of range")
            newlist = 0
        finally:
            lists.append(newlist)
    return lists
