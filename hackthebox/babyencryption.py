import codecs
def decrypt(b):
    result = ""

    for char in b:
        for x in range(33, 126):
            if(123 * x + 18) % 256 == char:
                result += chr(x)

    return result

f = open('./msg.enc','r')
decodedBytes = codecs.decode(f.read(), 'hex_codec')
result = decrypt(decodedBytes)
print(result)
