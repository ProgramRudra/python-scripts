dhcp = []
file = open('dhcp.log','r')
i = file.readlines()
for line in i:
    if '#' in line:
        continue
    else:
        text = line.split("\t")
        dhcp.append(text)
#print (dhcp)
#print (dhcp[0][6],'|', dhcp[0][7])
#End of dhcp
device = []
filedevice = open('known_devices.log', 'r')
x = filedevice.readlines()
for linedevice in x:
    if '#' in linedevice:
        continue
    else:
        textdevice = linedevice.split("\t")
        device.append(textdevice)
#countdhcp = dhcp[]
#for prosess in dhcp:
#    if dhcp[/]
#print (device)
#print (dhcp)
#for count in
dhcp_counter = 0
device_counter = 0

for mac in range (len(dhcp)):
    #print (dhcp[dhcp_counter][6])
    dhcpmac = dhcp[dhcp_counter][6]
    #dhcp_counter += 1
    #print (dhcpmac)
    device_counter = 0
    for i in range (len(device)):

        devicemac = device[device_counter][1]
        #print(' matching ' + dhcpmac + ' with ' + devicemac)
        #device_counter += 1
        #print(devicemac)
        if dhcpmac in devicemac:
            print (devicemac,device[device_counter][2])
            device_counter +=1

        else:
            device_counter += 1
    dhcp_counter += 1
