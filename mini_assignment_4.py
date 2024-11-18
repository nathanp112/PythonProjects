from netmiko import ConnectHandler

routers = [
    {"host": "192.168.192.130", "username": "", "password": "", "secret": "cisco1", "port": 30006},
    {"host": "192.168.192.130", "username": "", "password": "", "secret": "cisco2", "port": 30007},
    {"host": "192.168.192.130", "username": "", "password": "", "secret": "cisco3", "port": 30008}
]

for i, router in enumerate(routers, start=1):
    filename = f"router{i}.txt"
    with open(filename, 'w') as file:
        file.write(f"{router['host']}\n")
        file.write(f"{router['username']}\n")
        file.write(f"{router['password']}\n")
        file.write(f"{router['port']}\n")

ospf_commands = """router ospf 1
network 0.0.0.0 0.0.0.0 area 0
distance 110
default-information originate
"""

# with open("ospf_commands.txt", 'w') as file:
#     file.write(ospf_commands)
for i in range(1, 4):
    lines = open(f"router{i}.txt", "r").readlines()
    #exit(lines)

    connection = ConnectHandler(
        device_type='cisco_ios_telnet',
        host=lines[0].strip(),
        username=lines[1].strip(),
        password=lines[2].strip(),
        secret='',
        port=lines[3].strip()
    )

    with open("ospf_commands.txt", 'r') as ospf_file:
        ospf_config = ospf_file.read()

    connection.enable()
    connection.send_config_from_file("ospf_commands.txt")
    connection.disconnect()
