def code(message,offset):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    message = str(message)
    message = message.lower()
    output = []
    for i in message:
        if alphabet.count(i) == 0:
            output.append(i)
        else:
            index = alphabet.index(i)
            offset = (abs(offset)*(-1))
            index += offset
            if index > (len(alphabet)-1):
                corrected_index = (index - len(alphabet))
                output.append(alphabet[corrected_index])
            else:
                output.append(alphabet[index])
    
    return "".join(output)
