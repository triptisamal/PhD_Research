import re


def insideOrNot(a):
    print(a)

    arr = a.split(', ')
    print(float(arr[0]))
    print(float(arr[1]))
    print(float(arr[2]))



packet = "EventID:RECEIVE_008, node:198, time: 1, details: The packet is {'pID': 0, 'dLoc': (0.57229507, 0.025313331, 0.18988311), 'tLoc': (0.17912914, 0.76912647, 0.88080639), 'sLoc': (0.26650634, 0.79798305, 0.8773067), 'myLoc': (0.17912914, 0.76912647, 0.88080639), 'eccentricity': 0.6, 'tUB1': 0.002, 'tUB2': 0.0005, 'zoneType': 'SINGLE'}"



substring = re.findall(r"'myLoc': (.*?), 'eccentricity'",packet)
print(substring[0])

subsubstring = re.findall(r"\((.*?)\)",substring[0])
print(subsubstring[0])
insideOrNot(subsubstring[0])
