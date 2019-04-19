import multiprocessing
import socketlib
import randomlib

f = open("log.log","a")

class JoinThread(socketlib.threading.Thread):
    def __init__(self, srv):
        super().__init__()
        self.srv = srv
    def run(self):
        while(self.srv.isalive):
            sck, addr_info = self.srv.ssocket.accept()
            packed_socket = socketlib.packed_client(addr_info[0], addr_info[1], sckt=sck)
            
            name_data = packed_socket.recv_msg(["request"])
            player_name = name_data["name"]
            packed_socket.send_msg({"type": "accpet"})

            packed_socket.username = player_name
            self.srv.add_newplayer(packed_socket)
        print("dead.")

class Game_server(multiprocessing.Process):
    def __init__(self):
        super().__init__()
        self.players = []
        # 寻找一个能够使用的端口
        sck = socketlib.socket.socket(socketlib.socket.AF_INET, socketlib.socket.SOCK_STREAM)
        while(True):
            self.port = randomlib.random.randint(15000,20000)
            try:
                sck.bind(("",self.port))
            except:
                continue
            self.ssocket = sck
            self.ssocket.listen(5)
            break
        self.status = 1
        self.isready = False
        self.isalive = True
        join_thread = JoinThread(self)
        join_thread.start()

    def run(self):
        times = 50000
        while(self.isalive):
            # 准备阶段
            times -= 1
            if times == 0:
                self.isalive = False
            if self.status == 1:
                original_pack = {"type":"update", "ready": self.isready, "port": self.port}
                # 添加最多两人
                for player_id in range(min(len(self.players), 2)):
                    original_pack.setdefault("names",[])
                    original_pack["names"].append(self.players[player_id].username)

                for p_idx in range(len(self.players)):
                    p = self.players[p_idx]
                    pack = original_pack.copy()
                    pack["id"] = p_idx
                    p.send_msg(pack)

    def add_newplayer(self, player_socket):
        f.write("Add player.\n")
        self.players.append(player_socket)

    def player_exit(self, index):
        if self.status > 1 and index > 1:
            pack = {"type":"win", "id": 1-index}
            for p in self.players:
                p.send_msg(pack)
            self.self_exit()
        else:
            del self.players[index]
            if len(self.players == 0):
                self.self_exit()

    def self_exit(self):
        self.isalive = False
        
