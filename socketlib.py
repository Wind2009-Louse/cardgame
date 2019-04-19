import socket
from multiprocessing import Queue
import json
import threading
import struct
import randomlib

class MR_thread(threading.Thread):
    def __init__(self, client):
        super().__init__()
        self.packed_client = client
        self.running = True
    def run(self):
        while(self.running):
            try:
                header = self.packed_client.ssocket.recv(4)
                msg_size = struct.unpack('i',header)[0]

                msg_byte = b''
                while(msg_size > 0):
                    recv_size = min(1024,msg_size)
                    msg_byte += self.packed_client.ssocket.recv(recv_size)
                    msg_size -= len(msg_byte)

                msg_json = msg_byte.decode(encoding='utf-8')
                msg = json.loads(msg_json)
                self.packed_client.alive = 3
                self.packed_client.recv_queue.put(msg)
            except:
                self.packed_client.alive -= 1
        

class packed_client():
    def __init__(self, ip, port, sckt=None, tout=None):
        if sckt is None:
            self.ssocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            if tout:
                self.ssocket.settimeout(tout)
            try:
                self.ssocket.connect((ip, port))
            except Exception as e:
                raise e
        else:
            self.ssocket = sckt
        self.id = "%s:%d"%(ip, port)
        self.recv_queue = Queue()
        self.recv_thread = MR_thread(self)
        self.recv_thread.start()
        self.alive = 3
    def send_msg(self, msg):
        if msg is None:
            return
        msg_str = json.dumps(msg)
        msg_byte = msg_str.encode(encoding="utf-8")
        msg_length = len(msg_byte)
        msg_header = struct.pack('i',msg_length)
        try:
            self.ssocket.send(msg_header)
            self.ssocket.send(msg_byte)
            self.alive = 3
        except:
            self.alive -= 1
    def recv_msg(self, fliter, b=True):
        while(True):
            try:
                recv_data = self.recv_queue.get(block=b)
            except Exception as e:
                return None
            self.alive = 3
            if recv_data["type"] not in fliter:
                self.recv_queue.put(recv_data)
                if not b:
                    return None
                continue
            return recv_data
    def check_state(self):
        pass