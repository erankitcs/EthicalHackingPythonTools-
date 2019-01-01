from scapy.all import *

def sniffer(packet):

    http_packet = packet
    #print(str(http_packet))
    print(type(str(http_packet)))

    if 'POST' in str(http_packet):
        print('In post section')
        print(str(http_packet))
        if len(str(http_packet).split("\r\n\r\n")) > 1:
            #domain = str(http_packet).split("\r\n")[1]
            data = str(http_packet).split("\r\n\r\n")[1]

            print('*'*20)
            #print('Domain: %s' % domain)
            print('Data: %s' % data)
            print('*' * 20)
            print('\n\n')

sniff(iface='Intel(R) Wireless-AC 9462', prn= sniffer , filter='tcp port 80')

