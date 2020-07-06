f1 = open('check.zip', 'rb').read()
f2 = open('test.zip', 'rb').read()
f3 = open('im.png', 'rb').read()

print('f1', len(f1), 'f2', len(f2), 'f3', len(f3))
print('result', (len(f2) + len(f3)), 'lack', (len(f1) - len(f2) - len(f3)))

print()
print(f1[:len(f2)])

print()
print(f1[len(f3):len(f1)])

print()
print(f2)