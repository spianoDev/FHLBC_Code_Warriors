# https://www.codewars.com/kata/57f4ccf0ab9a91c3d5000054
# Level 6kyu

## Directions ##

# Lot of junior developer can be stuck when they need to change the access permission to a file or a directory in
# an Unix-like operating systems.
#
# To do that they can use the chmod command and with some magic trick they can change the permission of a file or a
# directory. For more information about the chmod command you can take a look at the wikipedia page.
#
# chmod provides two types of syntax that can be used for changing permissions. An absolute form using octal to denote
# which permissions bits are set e.g: 766. Your goal in this kata is to define the octal you need to use in order to set
# your permission correctly.
#
# Here is the list of the permission you can set with the octal representation of this one.
#
# User
# read (4)
# write (2)
# execute (1)
# Group
# read (4)
# write (2)
# execute (1)
# Other
# read (4)
# write (2)
# execute (1)

# The method take a hash in argument this one can have a maximum of 3 keys (owner,group,other).
# Each key will have a 3 chars string to represent the permission,
# for example the string rw- say that the user want the permission read, write without the execute.
# If a key is missing set the permission to ---
#
# Note: chmod allow you to set some special flags too (setuid, setgid, sticky bit) but to keep some simplicity for this
# kata we will ignore this one.

## Function ##
def chmod_calculator(perm):
    numbers = {
        'r': 4,
        'w': 2,
        'x': 1,
        '-': 0
    }
    chmod = 0
    if 'user' in perm:
        user = (numbers[perm['user'][0]] + numbers[perm['user'][1]] + numbers[perm['user'][2]]) * 100
        chmod += user
    else:
        pass
    if 'group' in perm:
        group = (numbers[perm['group'][0]] + numbers[perm['group'][1]] + numbers[perm['group'][2]]) * 10
        chmod += group
    else:
        pass
    if 'other' in perm:
        other = (numbers[perm['other'][0]] + numbers[perm['other'][1]] + numbers[perm['other'][2]])
        chmod += other
    else:
        pass
    return str(chmod).zfill(3)

    # print(perm['user'])


## Test Cases ##

# chmod_calculator({"user": 'rwx', "group": 'r-x', "other": 'r-x'}) # => "755"
# chmod_calculator({"user": 'rwx', "group": 'r--', "other": 'r--'}) # => "744"
# chmod_calculator({"user": 'r-x', "group": 'r-x', "other": '---'}) # => "550"
# chmod_calculator({"group": 'rwx'})  # => "070"
chmod_calculator({}) # => "000"
