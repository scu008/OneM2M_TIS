import os
from threading import *
from socket import *



# Server thread for file transfer
class Stream_thread(Thread):
    
    def __init__(self, conn, addr):
        Thread.__init__(self)
        self.conn = conn
        self.addr = addr

        
    def run(self):
        # Update a file list for the directory
        dir_path = 'C:\Users\LWS\Desktop\Cloud'
        cloud_list = os.listdir(dir_path)
        
        # Print information of the files in the list
        for name in cloud_list:
    
            # Create file path
            file_path = os.path.join(dir_path, name)
            
            # Open file
            f = open(file_path, 'rb')
            f.seek(0,2)
            size = f.tell()
            f.seek(0,0)
            
            print 'Transmission of', name
            print 'Size:', size / 10.0**6, 'Mbyte\n'
            buff_size = 2048
            
            
            # Start file transfer
            self.conn.send(name)
            data = f.read(buff_size)
            while data:
                self.conn.send(data)
                data = f.read(buff_size)
            self.conn.sent('END')
            
            print 'The file ', name, 'is transfered'
            
            
            # Close the file pointer
            f.close()
            
        

#==================================================================
    
# Start of the wifi_main thread 

# Socket information
port = 3601
host = ''
serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('', port))
serverSock.listen()
print 'Waiting the binding....'


# Thread list
thread_arr = []


# Routine
while True:
    
    # Accept the access
    conn, addr = serverSock.accept()
    print 'The client is accessed from ', addr
    
    # Start new thread for file transfer
    thread = Stream_thread(conn, addr)
    thread_arr.append(thread)
    thread.start()
    
    
    