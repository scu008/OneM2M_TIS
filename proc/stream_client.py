from socket import *
import subprocess
import os, sys


# Socket information
host = sys.argv[1]
port = int(sys.argv[2])
buff_size = 2048
ADDR = (host, port)


# Socket open
conn = socket(AF_INET, SOCK_STREAM)
conn.connect(ADDR)
print 'Socket is connected!'


# Variables Initialization
video_list = []
arr_data = ''
buffer = ''
name = ''
start = 0


# Initialize the file reception
name = conn.recv(buff_size)


# Data reception
while True:
    
    
    try :
        
        # Load to buffer
        data = conn.recv(buff_size)
        buffer = buffer + data        


            
            
            elif ctname == 'Video' and con == 'END':
                
                if start == 1 :
                    
                    # Open VLC Player
                    print 'End of file'
                    video_file = open(name, 'wb')
                    #video_file.write( binascii.unhexlify(arr_data) )
                    video_file.write( base64.decodestring(arr_data) )
                    video_file.close()
                    subprocess.Popen('vlc -fL ' + name)
                    
                    # Connection Initialization
                    conn.close()
                    conn = socket(AF_INET, SOCK_STREAM)
                    conn.connect(ADDR)
                    conn.send( encoder.encode(ctname, 'on') )
                    ack = conn.recv(buff_size)
                    
                    # Variables Initialization
                    arr_data = ''
                    buffer = ''
                    name = ''
                    start = 0
                    print 'Reset'
                    continue
                
                
            elif ctname == 'Video':
                arr_data = arr_data + con
                
                
            else :
                continue
        
    except :
        continue
    