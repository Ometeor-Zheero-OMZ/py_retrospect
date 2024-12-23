file_path = "C:/"

def print_out():
    file_path = "C:/Program Files/bin"
    # C:/Program Files/bin
    print(file_path)

print_out()
# C:/
print(file_path)

#############
# グローバル #
#############
file_path = "C:/"

def print_out():
    global file_path

    file_path = "C:/Program Files/bin"
    # C:/Program Files/bin
    print(file_path)

print_out()
# C:/Program Files/bin
print(file_path)

###############
# 関数名を出力 #
###############
def print_out():
    # print_out
    print(print_out.__name__)
    # None
    print(print_out.__doc__)

print_out()
