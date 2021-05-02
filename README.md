# cpass
Commonly Used Password List Generator

## About
CPASS(Commonly Used Password List Generator) is a python program that, as the name suggests, generates
commonly used passwords using information about the subject.
Enter in the information and you have a wordlist of possible combination of passwords to use while pentesting.

## Requirements
CPASS requires Python3 on the device.

## Installation

Clone the Repository;
```bash
$ git clone https://github.com/PrashantMhrzn/cpass.git
```

CD into the cloned directory;
```bash
$ cd  cpass/
```

Run cpass.py;
```
$ python3 cpass.py
```
## Usage

```bash
$ python3 cpass.py

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
[+] Hit enter if you dont know the answer
    
> Firstname: test
> Lastname: doe
> Nickname: jane
> Birthdate(DDMMYYYY): 24111998


> Do you want special characters in the list?(y/n) n
> Keywords you might want to include(sperated by a coma, ex:samsepi,mrrobot) hacker
```

## Liscense
[GNU](https://github.com/PrashantMhrzn/cpass/blob/main/LICENSE)