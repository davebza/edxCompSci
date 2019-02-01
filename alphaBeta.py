def loops( I=0, S=1 ):
    n = I
    while True:
        yield n
        n += S

def analyze(inStr):
    # empty slice (maxStr) to implement
    # str native methods
    # in the anallize search execution
    maxStr = inStr[0:0]
    # loop to read the input string (inStr)
    for i in range(len(inStr)):
        # loop to sort and compare each new substring
        # the loop uses the loops method of past
        # I = sum of:
        #     (i) current read index
        #     (len(maxStr)) current answer length
        #     and 1
        for o in loops(i + len(maxStr) + 1):
            # create a new substring (newStr)
            # the substring is taked:
            # from: index of read loop (i)
            # to:   index of sort and compare loop (o)
            newStr = inStr[i:o]

            if len(newStr) != (o - i):# detect and found duplicates
                break
            if sorted(newStr) == list(newStr):# compares if sorted string is equal to listed string
                # if success, the substring of sort and compare is assigned as answer
                maxStr = newStr
    # return the string recovered as longest substring
    return maxStr

s = 'azcbobobegghakl'

alphabet = "abcdefghijklmnopqrstuvwxyz"

answer = (analyze(s))

print("Longest substring in alphabetical order is: " + answer)


