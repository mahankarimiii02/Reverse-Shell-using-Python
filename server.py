import socket 
import threading 

ip = '127.0.0.1'    # Enter the Ip
port = 12345        # Enter the Port
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#server.bind(('87.248.145.79' , 22222)) 
server.bind((ip , port)) 
server.listen(3) 




def delete_target() : 
    try : 
        del clients['target']
    except : 
        pass 
    

def delete_main() : 
    try : 
        del clients['main']
    except : 
        pass 

         
    

   
def target() : 
   
    while True :
        try :
            message = target_con.recv(4096).decode('utf-8',errors='ignore')
        except :
            delete_target()
            break
        try :
            if int(message) : 
                size = int(message)
                try :
                    main_con.send(str(size).encode('utf-8',errors='ignore'))
                except : 
                    delete_main()
                    break 
                
                
                result = b''
                
                try :
                    while True : 
                        result+=target_con.recv(4096)
                        if result[-4:] == b'done' : 
                            break 
                        
                      
                except : 
                    delete_target()
                    break 
                
                
                try :
                    main_con.sendall(result)    
                except :
                    delete_main()
                    break
        except : 
            try : 
                main_con.sendall(message.encode('utf-8',errors='ignore'))
            except :
                delete_main()
                break
            
      
    


def main() :
    while True :
        try :
            message = main_con.recv(4096).decode('utf-8',errors='ignore')
            
        except  :
            delete_main() 
            break
        
        try :
            if int(message) : 
                
                size = int(message)
                try :
                    target_con.send(str(size).encode('utf-8',errors='ignore'))
                except : 
                    delete_target()
                    break 
                
                i=0
                result = b''
                
                try :
                    while True : 
                        result+=main_con.recv(4096)
                        if result[-4:] == b'done' : 
                            break
                        i+=4096
                except : 
                    delete_main()
                    break 
                
                
                try :
                    target_con.sendall(result)    
                except :
                    delete_target()
                    break
        except : 
            
            try : 
                target_con.sendall(message.encode('utf-8',errors='ignore'))
            except :
                delete_target()
                break
        
        


clients = {}
while True : 
    con , addr = server.accept() 
    a = con.recv(1024).decode('utf-8')
    if a == 'main' : 
        clients['main'] = con 
        main_con = clients['main']
    elif a == 'target' : 
        clients['target'] = con 
        target_con = clients['target']
    
    if len(clients) == 2  : 
        main_con.send('connected'.encode('utf-8',errors='ignore'))
        threading.Thread(target=target).start() 
        threading.Thread(target=main).start()
                    
