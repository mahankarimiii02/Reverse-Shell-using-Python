# A simple ReverseShell created in Python 

# Details 
1. We have 3 files here 
    - ```server.py``` : the main tunel for communication between the two clients
    - ```client (attacker).py``` : the client file for attacker
    - ```client (target).py``` : the client file for target

    
2. The attacker file has 4 options :
    - Transfer File (Send) : send any kind of file from your device to targets's device 
    - Transfer File (Get) : get any kind of file from target's device to yours
    - Reverse Shell : run cmd/powershell commands 
    - Close connection : if for any reason you wanted to close the ```target``` connection (to server) choose this option

3. Because of EDR Evaluation, the target file doesn't run the command directly ... it creates a .bat file incluidng the commands and then runs the .bat file 

4. Because of Persian language, i used ```arabic_reshaper``` library to show the paths, directories, etc (in Persian or Arabic) in a correct way

5. If you wanted to convert the ```.py``` to ```.exe``` make sure to use some obfuscation ... without obfuscation it will be detected as a malcious file 
