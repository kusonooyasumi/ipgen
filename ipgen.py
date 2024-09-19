import ipaddress

def list_ip_addresses(network):
    # Create an IPv4Network object
    net = ipaddress.IPv4Network(network)
    # Iterate through all addresses in the network
    for ip in net:
        print(ip)

# Get user input for the IP range
user_input = input("Enter the IP range (e.g., 192.168.0.0/24): ")

# Use the function to list all IPs in the user-specified range
list_ip_addresses(user_input)
