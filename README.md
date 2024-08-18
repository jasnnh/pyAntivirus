# pyAntivirus
An antivirus built in python using a public database of virus signatures to detect and remove infected files.

antivirus.py:

this is the main python script that we will call to perform a scan by either using cmd line or powershell to pass arguments to scan a file or coding a GUI/UI into the script. Currently the script is hardcoded to scan and read the file testVirus.txt which contains the virus string for "EICAR-STANDARD-ANTIVIRUS-TEST-FILE". There are community based and public virus signature databases of SHA1, MD5, and SHA256 hashes to identify viruses and with these signatures we can paste them into virustotal.com and identify them just by the hashes. The idea of a Antivirus is simple detect and identify infected files using their signatures and that is what I have accomplished today with this project.

How it works:

antivirus.py will scan files read their binary data and generate a MD5, SHA1, SHA256 hash and with this hash we loop check the virus signature database which i have exported to json format to efficiently load the signatures quickly. after comparing the signature with the signatures within the database if there is a match we will be prompted with a delete file message and to proceed.

testVirus.txt:

this is the example virus file that I am using to identify as an infected file it's using the "EICAR-STANDARD-ANTIVIRUS-TEST-FILE" signature.

virusDB.json:

this is a small database of compiled virus signatures and antivirus.py will loop through all of them to verify the signatures if the file is infected.

![Screenshot](https://github.com/jasnnh/pyAntivirus/blob/main/image.png)
