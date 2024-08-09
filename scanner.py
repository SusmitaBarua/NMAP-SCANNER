import nmap
scanner = nmap.PortScanner()

print("Welcome, this is a simple Nmap automation tool")

ip_add = input("Enter the IP address you want to scan: ")
print("The IP you entered is", ip_add)

response = input("""\nPlease enter the type of scan you want to run:
                    1) SYN ACK Scan
                    2) UDP Scan
                    3) Comprehensive Scan \n""")
print("You have selected option:", response)

if response == '1':
    print("Nmap version:", scanner.nmap_version())
    scanner.scan(ip_add, '1-1025', '-v -sS')
    print(scanner.scaninfo())
    print("IP Status:", scanner[ip_add].state())
    print(scanner[ip_add].all_protocols())
    
    if 'tcp' in scanner[ip_add].all_protocols():
        print("Open Ports:", scanner[ip_add]['tcp'].keys())
    else:
        print("No TCP ports found.")

elif response == '2':
    print("Nmap version:", scanner.nmap_version())
    scanner.scan(ip_add, '1-1025', '-v -sU')
    print(scanner.scaninfo())
    print("IP Status:", scanner[ip_add].state())
    print(scanner[ip_add].all_protocols())
    
    if 'udp' in scanner[ip_add].all_protocols():
        print("Open Ports:", scanner[ip_add]['udp'].keys())
    else:
        print("No UDP ports found.")

elif response == '3':
    print("Nmap version:", scanner.nmap_version())
    scanner.scan(ip_add, '1-1025', '-v -sS -sV -sC -A -O')
    print(scanner.scaninfo())
    print("IP Status:", scanner[ip_add].state())
    print(scanner[ip_add].all_protocols())
    
    if 'tcp' in scanner[ip_add].all_protocols():
        print("Open Ports:", scanner[ip_add]['tcp'].keys())
    else:
        print("No TCP ports found.")

else:
    print("Please enter a valid option.")