#192.168.1.5

ip = input('Enter IP: ')
parts = ip.split('.')

print(parts)

a = '.'

start = int(input('Start num: '))
end = int(input('End num: '))


for x in range(start, end + 1):
    print(parts[0] + a + parts[1] + a + parts[2] + a +str(x))

# Enter IP: 192.168.1.5
# ['192', '168', '1', '5']
# Start num: 1
# End num: 10
# 192.168.1.1
# 192.168.1.2
# 192.168.1.3
# 192.168.1.4
# 192.168.1.5
# 192.168.1.6
# 192.168.1.7
# 192.168.1.8
# 192.168.1.9
# 192.168.1.10
