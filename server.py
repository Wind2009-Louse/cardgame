import multiprocessing
import socketlib
import randomlib

class JoinThread(socketlib.threading.Thread):
    def __init__(self, srv):
        super().__init__()
        self.srv = srv
    def run(self):
        while(True):
            sck, addr_info = self.srv.socket.accept()
            packed_socket = socketlib.packed_client(addr_info[0], addr_info[1], socket=sck)
            self.srv.players.append(packed_socket)

class Game_server(multiprocessing.Process):
    def __init__(self):
        # 寻找一个能够使用的端口
        sck = socketlib.socket.socket(socketlib.socket.AF_INET, socketlib.socket.SOCK_STREAM)
        while(True):
            self.port = randomlib.random.randint(15000,20000)
            try:
                sck.bind(("",self.port))
            except:
                continue
            self.socket = sck
            break
        self.players = []
        self.status = 1
        self.isready = False
        self.join_thread = JoinThread(self)
        self.join_thread.start()
        sck.listen(5)
    def run(self):
        while(True):
            # 准备阶段
            if self.status == 1:
                original_pack = {"type":"update", "ready": self.isready, "port": self.port}
                for p_idx in range(len(self.players)):
                    p = self.players[p_idx]
                    pack = original_pack.copy()
                    pack["id"] = p_idx
                    p.send_msg(pack)
    def player_exit(self, index):
        if self.status > 1 and index > 1:
            pack = {"type":"win", "id": 1-index}
            for p in self.players:
                p.send_msg(pack)
            self.self_exit()
    def self_exit(self):
        pass

        
