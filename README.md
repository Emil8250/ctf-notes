# ctf-notes

## Volatility3
### Getting windows passwords
To access user password hashes: 
vol -f OtterCTF.vmem windows.hashdump.Hashdump
To get try and get them in plain text
vol -f OtterCTF.vmem windows.lsadump
Alternatively the hashes could have been cracked with John the Ripper.
