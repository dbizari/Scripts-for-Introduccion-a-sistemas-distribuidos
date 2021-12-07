### datos parcial

packet = 1500 * 8 # en bits

ida = [
    {'distancia': 0.15,  'ancho': 10e6,  'propagacion': 1.7e5 },
    {'distancia': 8,     'ancho': 150e6, 'propagacion': 1.7e5 },
    {'distancia': 80,    'ancho': 150e6, 'propagacion': 1.7e5 },
    {'distancia': 0.025, 'ancho': 50e6,  'propagacion': 2e5 }
]

vuelta = [
    {'distancia': 0.025, 'ancho': 50e6,  'propagacion': 2e5 },
    {'distancia': 1,     'ancho': 100e6, 'propagacion': 1.7e5 },
    {'distancia': 7,     'ancho': 100e6, 'propagacion': 2e5 },
    {'distancia': 0.15,  'ancho': 10e6,  'propagacion': 1.7e5 }
]


# Round scientific number to 2 significative decimals
def r2(n):
    return float('{:0.2e}'.format(n))

# partial values of latency
print('insercion IDA')
print(list(map(lambda x: r2(packet / x['ancho']), ida)))
print('insercion VUELTA')
print(list(map(lambda x: r2(packet / x['ancho']), vuelta)))
print('propagacion IDA')
print(list(map(lambda x: r2(x['distancia'] / x['propagacion']), ida)))
print('propagacion VUELTA')
print(list(map(lambda x: r2(x['distancia'] / x['propagacion']), vuelta)))

RTT = 0
RTT_partialRound = 0

for e in ida:
    RTT += packet / e['ancho']
    RTT += e['distancia'] / e['propagacion']

    RTT_partialRound += r2(packet / e['ancho'])
    RTT_partialRound += r2(e['distancia'] / e['propagacion'])

for e in vuelta:
    RTT += packet / e['ancho']
    RTT += e['distancia'] / e['propagacion']

    RTT_partialRound += r2(packet / e['ancho'])
    RTT_partialRound += r2(e['distancia'] / e['propagacion'])

print()
print('Without rounding ',RTT * 1000)
print('Rounding in intermediate steps', RTT_partialRound * 1000)
