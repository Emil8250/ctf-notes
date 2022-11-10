# ctf-notes

## Volatility3
### Getting windows passwords
To access user password hashes: 

vol -f OtterCTF.vmem windows.hashdump.Hashdump

To get try and get them in plain text

vol -f OtterCTF.vmem windows.lsadump

Alternatively the hashes could have been cracked with John the Ripper.

### Getting windows computer hostname (and other regs)
vol -f OtterCTF.vmem windows.registry.printkey.PrintKey --key 'ControlSet001\Control\ComputerName\ComputerName'

### Getting windows computer IP
vol -f OtterCTF.vmem windows.netscan.NetScan

### Finding malware
To find potential malware: 

vol -f flounder-pc-memdump.elf windows.malfind.Malfind > malfindHtb.txt

To get .exe files found in the output

cat malfindHtb.txt | grep .exe

To check the potential malwares in the cmd line 

vol -f flounder-pc-memdump.elf windows.cmdline.CmdLine --pid 2752

In this case it resulted in an encrypted powershell script, which contained the flag
