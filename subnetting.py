import socket
import struct


def ip2int(addr):
    return struct.unpack("!I", socket.inet_aton(addr))[0]


def int2ip(addr):
    return socket.inet_ntoa(struct.pack("!I", addr))

srcDirection = '164.92.136.0'
initialPrefix = 22

# parcial
subnet = [
    {'name': 'A', 'host': 255, 'router': 1},
    {'name': 'B', 'host': 50, 'router': 1},
    {'name': 'C', 'host': 64, 'router': 1},
    {'name': 'D', 'host': 32, 'router': 1},
    {'name': 'E', 'host': 80, 'router': 1},
    {'name': 'R', 'host': 0, 'router': 3}
]

totalSpaceNeeded = 0

for s in subnet:
    total_directions = s['host'] + s['router'] + 2  # direccion de red + direccion de broadcast 
    
    amountOfBitsNeeded = 2 # Arrancamos en 4 ya que es la red mas chica posible
    while  2 ** amountOfBitsNeeded < total_directions:
        amountOfBitsNeeded += 1
        
    s['block'] = 2 ** amountOfBitsNeeded
    s['bitsNeeded'] = amountOfBitsNeeded
    totalSpaceNeeded += s['block']

print('total space needed: %d, space assigned: %d' % (totalSpaceNeeded, 2 ** (32 - initialPrefix)))

if totalSpaceNeeded > 2 ** (32 - initialPrefix):    
    print('error there is not enough space for all the subnet')
    exit()

# this sort takes as second sort criteria the amount of real host in the subnet, please read the requirements of the exercise    
# subnetSorted = sorted(subnet, key=lambda k: (-k['block'], -k['host'], k['name'])) # take in mind the fields with '-' denote ascending sort

subnetSorted = sorted(subnet, key=lambda k: (-k['block'], k['name'])) # take in mind the fields with '-' denote ascending sort

ptrDirection = ip2int(srcDirection)
for s in subnetSorted:
    s['direction'] = int2ip(ptrDirection)
    ptrDirection += s['block']


# remember the final result must be sorted by name

subnetSorted = sorted(subnetSorted, key=lambda k: (k['name']))

print()
for s in subnetSorted:
    print('name: %s, direction: %s, prefix: %s' % (s['name'], s['direction'], '/' + str(32 - s['bitsNeeded'])))

