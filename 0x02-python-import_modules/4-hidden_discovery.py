#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    search = dir(hidden_4)
    for my_name in search:
        if my_name[:2] != '__':
            print("{}".format(my_name))
