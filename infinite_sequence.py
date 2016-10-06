import sys

def sequence_generator():
    integer = 1
    while True:
        str_int = str(integer)
        for char in str_int:
            yield char
        integer += 1

def get_position(subSeq):
    subSeqStr = str(subSeq)
    sequence = sequence_generator()
    i=0
    _subSeq = ''
    for n in sequence:
        _subSeq+=str(n)
        i+=1
        if i==len(subSeqStr):
            break
    position = 1
    if _subSeq == subSeqStr:
        return 1
    else:
        for m in sequence:
            position+=1
            _subSeq = _subSeq[1:] + m
            if _subSeq == subSeqStr:
                return position

def main(arg):
    if arg.isdigit():
        position = get_position(arg)
        print "Subsequence " + str(arg) + " positioned at " + str(position)
    else:
        print "Invalid input. Please enter a number!"


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(str(sys.argv[1]))
    else:
        print "Error!!! No sequence entered."
        print "Enter a numeric sequence!"