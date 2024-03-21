import ansible_runner
import yaml
import os
import sys

def ping():
    # Setting environment variable ANSIBLE_CONFIG
    os.environ['ANSIBLE_CONFIG'] = os.path.join(os.getcwd(), 'ansible.cfg')

    out, err, rc = ansible_runner.run_command(
        executable_cmd='ansible',
        cmdline_args=['all:localhost', '-m', 'ping'],
        input_fd=sys.stdin,
        output_fd=sys.stdout,
        error_fd=sys.stderr
    )


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
    
    print()
    # Ping the hosts and print the result
    ping()


if __name__ == "__main__":
    main() # Call main function