# A simple ReverseShell created in Python 

# Details 
1. We have 3 files here 
    - ```server.py``` : the main tunnel for communication between the two clients
    - ```client (attacker).py``` : the client file for attacker
    - ```client (target).py``` : the client file for target

    
2. The attacker file has 4 options :
    - Transfer File (Send) : send any kind of file from your device to targets's device 
    - Transfer File (Get) : get any kind of file from target's device to yours
    - Reverse Shell : run terminal commands 
    - Close connection : if for any reason you wanted to close the ```target``` connection (to server) choose this option

3. Because of EDR Evaluation, the target file doesn't run the command directly ... it creates a .bat file incluidng the commands and then runs the .bat file 

4. Because of Persian language, i used ```arabic_reshaper``` library to show the paths, directories, etc in the correct way

5. If you wanted to convert the ```.py``` to ```.exe``` make sure to use some obfuscation ... without obfuscation it will be detected as a malicious file 


# Installation 

1. Download and extract the zip file
2. Go to downloaded file's path and in terminal run :
```bash
pip install -r requirements.txt
```
4. In all 3 ```.py``` files put the ip address and port number (Default is 127.0.0.1:12345)
5. Save the changes
6. Before you run those two client files, make sure that ```server.py``` is running so they can connect to server
