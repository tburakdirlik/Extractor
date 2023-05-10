import ipaddress
import sys

# dosya yolu parametresini alın
dosya_yolu = sys.argv[1]

# dosyayı açın ve içeriği metin değişkenine atayın
with open(dosya_yolu, 'r') as dosya:
    metin = dosya.read()

# metindeki subnetleri ayıklayın
subnet_listesi = metin.split()

# subnetleri ekrana yazdırın
for subnet_str in subnet_listesi:
    try:
        subnet = ipaddress.ip_network(subnet_str)
        for ip in subnet:
            print(ip)
    except ValueError:
        print("")
