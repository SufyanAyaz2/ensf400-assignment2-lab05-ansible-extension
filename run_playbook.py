import ansible_runner
import os


def playbook():
    # Setting environment variable ANSIBLE_CONFIG
    os.environ['ANSIBLE_CONFIG'] = os.path.join(os.getcwd(), 'ansible.cfg')

    # Run the ansible-playbook command
    print("Running Playbook command please wait...")
    result = ansible_runner.run_command(
        executable_cmd='ansible-playbook',
        cmdline_args=['hello.yml']
    )

    outputString = result[0]

    # Print the output
    print("\n\nResult of Running Playbook:")
    print(outputString)

    # Verify and print the response from the NodeJS servers
    if 'Check list of Node.js apps running.' in outputString:
        if "changed" or "ok" or "skipping" in outputString:
            if 'Start example Node.js app.' in outputString:
                if "changed" or "ok" or "skipping" in outputString:
                    print("\n\nResponse from NodeJS servers is Node.js apps started successfully")
                else:
                    print("\n\nResponse from NodeJS servers is failure to start Node.js app")
            else:
                print("\n\nResponse from NodeJS servers is failure to start Node.js app")
        else:
            print("\n\nResponse from NodeJS servers is failure to start Node.js app")
    else:
        print("\n\nResponse from NodeJS servers is failure to start Node.js app")

    

def main():

    # Run the playbook and print the result as well as response from NodeJS servers
    playbook()


if __name__ == "__main__":
    main() # Call main function