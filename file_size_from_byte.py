import math


def verify_number():
    while True:
        try:
            v = int(input().strip())
        except:
            print("This is not an integer, please enter again: ")
            continue
        else:
            return v
            break


def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return f"{s} {size_name[i]}"


print('Please enter an integer:')
print(convert_size(verify_number()))
