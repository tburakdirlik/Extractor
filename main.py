import ipaddress

subnet_list = input("Subnet Listesi Giriniz ").split()
print("\n")
for subnet_str in subnet_list:
    try:
        subnet = ipaddress.ip_network(subnet_str)
        for ip in subnet:
            print(ip)
    except ValueError:
        print("")
