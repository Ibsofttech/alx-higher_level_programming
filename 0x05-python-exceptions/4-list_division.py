#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    my_list = []
    for i in range(list_length):
        ans = 0
        try:
            ans = my_list_1[i] / my_list_2[i]
        except (ValueError, TypeError):
            print("wrong type")
        except IndexError:
            print("out of range")
        except ZeroDivisionError:
            print("division by 0")
        finally:
            my_list.append(ans)
    return my_list
