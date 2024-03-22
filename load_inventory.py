import ansible_runner
import yaml
import os
import sys

def ping():
    # Setting environment variable ANSIBLE_CONFIG
    os.environ['ANSIBLE_CONFIG'] = os.path.join(os.getcwd(), 'ansible.cfg')

    # Running command to ping hosts
    results = ansible_runner.run_command(
        executable_cmd='ansible',
        cmdline_args=['all:localhost', '-m', 'ping']
    )

    output = results[0]

    return output


def main():

    # Load in the inventory file 'hosts.yml'
    with open('hosts.yml') as f:
        result = yaml.load(f, Loader=yaml.FullLoader)

    # Using inventory file 'hosts.yml' that is loaded in, 
    # print out information for the hosts including group names, host names, and IP addresses
    for group, info in result.items():
        print(f"\nGroup Name: {group}")
        for host, hostInfo in info['hosts'].items():
            print(f"\nHost Name: {host}")
            if hostInfo != None:
                if host != 'localhost':
                    print(f"    IP Address: {hostInfo['ansible_host']}")
                    print(f"    Connection Type: {hostInfo['ansible_connection']}")
                else:
                    print(f"    Connection Type: {hostInfo['ansible_connection']}")
            else:
                print("Information for this host has already been defined in another grouping.")
    
    
    # Ping the hosts and get the result
    pingResults = ping()

    # Print the results of pinging the hosts
    print("\n Ping Results:\n\n")
    print(pingResults)




if __name__ == "__main__":
    main() # Call main function