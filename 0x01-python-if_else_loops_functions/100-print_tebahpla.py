#!/usr/bin/python3
print(''.join(["{:c}".format(122 - i // 2) if i % 2 == 0 else "{:c}".format(90 - i // 2) 
               for i in range(26)]))
