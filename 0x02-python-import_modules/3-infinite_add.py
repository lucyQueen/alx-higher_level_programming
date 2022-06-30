#!/usr/bin/python3
def addition():
    for i in dir(hidden_4):
        if i[0:2] != "__":
            print(i)


if __name__ == "__main__":
    import hidden_4
    addition()
