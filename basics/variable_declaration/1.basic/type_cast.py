name = '23'

num = int(name)

# 23 <class 'int'>
print(num, type(num))

#####################################################################
#                                                                   #
#               Much more details on type casting                   #
#                                                                   #
#####################################################################

######################
# convert to integer #
######################
# 1
print(int(1.74))

# 12
print(int("12"))

####################
# convert to float #
####################

# 3.0
print(float(3))

# 3.14
print(float("3.14"))

#############################
# convert to complex number #
#############################

# (1+2j)
print(complex(1, 2))

#(3+4j)
print(complex("3+4j"))

#####################
# convert to string #
#####################

# "23"
print(str(23))

# "3.14"
print(str(3.14))

###################
# convert to list #
###################

parenthesis = (1, 2, 3)
curly_bracket = {1, 2, 3}

# [1, 2, 3]
print(list(parenthesis))

# [1, 2, 3]
print(list(curly_bracket))

####################
# convert to tuple #
####################

parenthesis = (1, 2, 3)
curly_bracket = {1, 2, 3}

# (1, 2, 3)
print(tuple(parenthesis))

# (1, 2, 3)
print(tuple(curly_bracket))

##################
# convert to set #
##################

bracket = [1, 2, 3]
str = "01001000 01000101 01001100 01010000"

# {1, 2, 3}
print(set(bracket))
# {' ', '1', '0'}
print(set(str))

###################
# convert to bool #
###################

# True
print(bool(1))

# False
print(bool(0))

# True
print(bool([]))

# False
print(bool([1, 2]))

####################
# convert to bytes #
####################

s = "リトルバスターズ！"
unicode = "utf-8"

# b'\xe3\x83\xaa\xe3\x83\x88\xe3\x83\xab\xe3\x83\x90\xe3\x82\xb9\xe3\x82\xbf\xe3\x83\xbc\xe3\x82\xba\xef\xbc\x81'
print(bytes(s, unicode))

# bytearray(b'\xe3\x83\xaa\xe3\x83\x88\xe3\x83\xab\xe3\x83\x90\xe3\x82\xb9\xe3\x82\xbf\xe3\x83\xbc\xe3\x82\xba\xef\xbc\x81')
print(bytearray(s, unicode))