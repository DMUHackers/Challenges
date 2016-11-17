from Crypto.Cipher import ARC4
f = open('secret.txt')
key = f.readline().strip()

o = open('challenge.txt','w')
f = open('book.txt')
for line in f:
    cipher = ARC4.new(key)
    print >>o, cipher.encrypt(line).encode('hex')

print "Wrote challenge.txt"
