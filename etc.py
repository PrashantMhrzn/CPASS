def heading():
    print('''
    <:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>
    <:>                                             <:>
    <:> ░█████╗░██████╗░░█████╗░░██████╗░██████╗    <:>
    <:> ██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝    <:>
    <:> ██║░░╚═╝██████╔╝███████║╚█████╗░╚█████╗░    <:>
    <:> ██║░░██╗██╔═══╝░██╔══██║░╚═══██╗░╚═══██╗    <:>
    <:> ╚█████╔╝██║░░░░░██║░░██║██████╔╝██████╔╝    <:>
    <:> ░╚════╝░╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═════╝░    <:>
    <:>                                             <:>
    <:>   𝔠𝔬𝔪𝔪𝔬𝔫𝔩𝔶 𝔲𝔰𝔢𝔡 𝔭𝔞𝔰𝔰𝔴𝔬𝔯𝔡 𝔩𝔦𝔰𝔱 𝔤𝔢𝔫𝔢𝔯𝔞𝔱𝔬𝔯     <:>
    <:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>

    [+] Insert information regarding the subject to create a list
    [+] Hit enter if you don't know the answer
        ''')


def ending(file_name):
    print(f'''
    [+] making a dictionary...
    [+] Sorting list and removing duplicates...
    [+] Saving dictionary to {file_name}.txt.
    - Please check under this directory, cpass/{file_name}.txt
    - Thanks for using CPASS, Best Wishes!
    ''')