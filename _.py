# encoding: utf-8
import redis, json

use = [
    {"server": "213.183.53.177", "port": "9088", "password": "f8npKgNzdkss2ytn", "cipher": "aes-256-cfb", "protocol": "ss"},
    {"server": "152.89.210.84", "port": "9027", "password": "EXN3S3eQpjE7EJu8", "cipher": "aes-256-cfb", "protocol": "ss"},
    {"server": "152.89.210.84", "port": "9059", "password": "9XwYyZsK8SNzQDtY", "cipher": "aes-256-cfb", "protocol": "ss"},
    {"server": "61.222.202.140", "port": "33792", "uuid": "e55cd182-01b0-4fb7-a510-363701a491c5", "alterId": "0", "cipher": "auto", "network": "ws", "ws-path": "/", "protocol": "vmess"},
    {"server": "213.183.53.177", "port": "9003", "password": "JdmRK9gMEqFgs8nP", "cipher": "aes-256-cfb", "protocol": "ss"},
    {"server": "185.167.117.171", "port": "9046", "password": "NvS8N4Vf8qAGPSCL", "cipher": "aes-256-cfb", "protocol": "ss"},
    {"server": "185.167.117.171", "port": "9040", "password": "p9z5BVADH2YFs3MN", "cipher": "aes-256-cfb", "protocol": "ss"},
    {"server": "185.167.117.171", "port": "9010", "password": "f63gg8EruDnUrmz4", "cipher": "aes-256-cfb", "protocol": "ss"},
    {"server": "213.183.53.177", "port": "9032", "password": "UWZQeLRWnkqgkseq", "cipher": "aes-256-cfb", "protocol": "ss"},
    {"server": "213.183.53.177", "port": "9031", "password": "BwcAUZk8hUFAkDGN", "cipher": "aes-256-cfb", "protocol": "ss"},
    {"server": "185.167.117.171", "port": "9079", "password": "TPqX8edgbAURcAMb", "cipher": "aes-256-cfb", "protocol": "ss"},
    {"server": "213.183.53.177", "port": "9001", "password": "UkXRsXvR6buDMG2Y", "cipher": "aes-256-cfb", "protocol": "ss"},
    {"server": "152.89.210.84", "port": "9037", "password": "TN2YqghxeFDKZfLU", "cipher": "aes-256-cfb", "protocol": "ss"},
    {"server": "213.183.53.177", "port": "9005", "password": "ZET59LF6DvCC8KVt", "cipher": "aes-256-cfb", "protocol": "ss"},
    {"server": "213.183.53.177", "port": "9000", "password": "a3GFYt36Sm82Vys9", "cipher": "aes-256-cfb", "protocol": "ss"},
    {"server": "213.183.53.177", "port": "9059", "password": "9XwYyZsK8SNzQDtY", "cipher": "aes-256-cfb", "protocol": "ss"},
    {"server": "213.183.53.177", "port": "9014", "password": "KnJGad3FqTvjqbaX", "cipher": "aes-256-cfb", "protocol": "ss"},
    {"server": "152.89.210.105", "port": "9088", "password": "f8npKgNzdkss2ytn", "cipher": "aes-256-cfb", "protocol": "ss"},
    {"server": "213.183.53.177", "port": "9027", "password": "EXN3S3eQpjE7EJu8", "cipher": "aes-256-cfb", "protocol": "ss"},
    {"server": "213.183.53.177", "port": "9015", "password": "ZpNDDKRu9MagNvaf", "cipher": "aes-256-cfb", "protocol": "ss"},
    {"server": "185.225.19.64", "port": "50003", "password": "8460400130", "cipher": "aes-256-cfb", "protocol": "ss"},
    {"server": "152.89.210.84", "port": "9079", "password": "TPqX8edgbAURcAMb", "cipher": "aes-256-cfb", "protocol": "ss"},
    {"server": "185.153.180.10", "port": "50003", "password": "8460400130", "cipher": "aes-256-cfb", "protocol": "ss"},
    {"server": "185.167.117.171", "port": "9070", "password": "bf7v334KKDV3YDhH", "cipher": "aes-256-cfb", "protocol": "ss"},
    {"server": "213.183.53.177", "port": "9008", "password": "y9VURyNzJWNRYEGQ", "cipher": "aes-256-cfb", "protocol": "ss"},
    {"server": "152.89.210.105", "port": "9046", "password": "NvS8N4Vf8qAGPSCL", "cipher": "aes-256-cfb", "protocol": "ss"},
    {"server": "185.167.117.171", "port": "9032", "password": "UWZQeLRWnkqgkseq", "cipher": "aes-256-cfb", "protocol": "ss"},
    {"server": "213.183.53.177", "port": "9007", "password": "kSPmvwdFzGMMW5pY", "cipher": "aes-256-cfb", "protocol": "ss"},
    {"server": "152.89.210.84", "port": "9015", "password": "ZpNDDKRu9MagNvaf", "cipher": "aes-256-cfb", "protocol": "ss"},
    {"server": "185.167.117.171", "port": "9037", "password": "TN2YqghxeFDKZfLU", "cipher": "aes-256-cfb", "protocol": "ss"},
    {"server": "213.183.53.177", "port": "9094", "password": "rpgbNnU9rDDU4aWZ", "cipher": "aes-256-cfb", "protocol": "ss"},
    {"server": "213.183.53.177", "port": "9073", "password": "daFYagqDdBdA6VTX", "cipher": "aes-256-cfb", "protocol": "ss"},
    {"server": "213.183.53.177", "port": "9070", "password": "bf7v334KKDV3YDhH", "cipher": "aes-256-cfb", "protocol": "ss"},
    {"server": "152.89.210.105", "port": "9000", "password": "a3GFYt36Sm82Vys9", "cipher": "aes-256-cfb", "protocol": "ss"},
    {"server": "45.76.71.233", "port": "46983", "uuid": "69099258-1476-46dd-a51b-84e915e941be", "alterId": "0", "cipher": "auto", "network": "ws", "ws-path": "/1tGK82lU/", "protocol": "vmess"},
    {"server": "152.69.204.149", "port": "50503", "uuid": "11b8a8c2-3548-4424-88f8-26cde886230a", "alterId": "0", "cipher": "auto", "network": "tcp", "ws-path": "/", "protocol": "vmess"},
    {"server": "150.230.96.106", "port": "57239", "uuid": "edf155b8-10e0-4a48-8bfc-6ce2d9f3ff72", "alterId": "0", "cipher": "auto", "network": "tcp", "ws-path": "/", "protocol": "vmess"},
    {"server": "217.30.10.65","port": "9025","password": "XPtzA9sCug3SPR4c","cipher": "aes-256-cfb","protocol": "ss"},
    {"server": "185.167.116.253","port": "9073","password": "daFYagqDdBdA6VTX","cipher": "aes-256-cfb","protocol": "ss"},
    {"server": "217.30.10.65","port": "9084","password": "c3NtHJ5ujV2tGDfj","cipher": "aes-256-cfb","protocol": "ss"},
    {"server": "217.30.10.65","port": "9045","password": "Lp27rqyJq72bZsqX","cipher": "aes-256-cfb","protocol": "ss"},
    {"server": "217.30.10.65","port": "9010","password": "f63gg8EruDnUrmz4","cipher": "aes-256-cfb","protocol": "ss"},
    {"server": "217.30.10.65","port": "9038","password": "gYCYXfkUQEs2TaJQ","cipher": "aes-256-cfb","protocol": "ss"},
    {"server": "217.30.10.64","port": "9007","password": "kSPmvwdFzGMMW5pY","cipher": "aes-256-cfb","protocol": "ss"},
    {"server": "217.30.10.64","port": "9070","password": "bf7v334KKDV3YDhH","cipher": "aes-256-cfb","protocol": "ss"},
    {"server": "185.167.117.171","port": "9040","password": "p9z5BVADH2YFs3MN","cipher": "aes-256-cfb","protocol": "ss"},
    {"server": "217.30.10.65","port": "9011","password": "M3t2ZEQcMGRWBjRa","cipher": "aes-256-cfb","protocol": "ss"},
    {"server": "51.195.136.209","port": "50004","password": "4415934295","cipher": "aes-256-cfb","protocol": "ss"},
    {"server": "185.167.116.252","port": "9015","password": "ZpNDDKRu9MagNvaf","cipher": "aes-256-cfb","protocol": "ss"},
    {"server": "217.30.10.65","port": "9040","password": "p9z5BVADH2YFs3MN","cipher": "aes-256-cfb","protocol": "ss"},
    {"server": "217.30.10.65","port": "9014","password": "KnJGad3FqTvjqbaX","cipher": "aes-256-cfb","protocol": "ss"},
    {"server": "217.30.10.64","port": "9003","password": "JdmRK9gMEqFgs8nP","cipher": "aes-256-cfb","protocol": "ss"},
    {"server": "217.30.10.64","port": "9001","password": "UkXRsXvR6buDMG2Y","cipher": "aes-256-cfb","protocol": "ss"},
    {"server": "217.30.10.65","port": "9019","password": "GA9KzeEgvfxNrgmM","cipher": "aes-256-cfb","protocol": "ss"},
    {"server": "217.30.10.65","port": "9018","password": "fG2artUmHfNT2cX7","cipher": "aes-256-cfb","protocol": "ss"},
    {"server": "217.30.10.64","port": "9045","password": "Lp27rqyJq72bZsqX","cipher": "aes-256-cfb","protocol": "ss"},
    {"server": "185.167.116.252","port": "9041","password": "U6qnYRhfyDmn8sgn","cipher": "aes-256-cfb","protocol": "ss"},
    {"server": "185.167.116.252","port": "9064","password": "cp8pRSUAyLhTfVWH","cipher": "aes-256-cfb","protocol": "ss"},
    {"server": "185.167.116.253","port": "9038","password": "gYCYXfkUQEs2TaJQ","cipher": "aes-256-cfb","protocol": "ss"},
    {"server": "217.30.10.64","port": "9005","password": "ZET59LF6DvCC8KVt","cipher": "aes-256-cfb","protocol": "ss"},
    {"server": "217.30.10.65","port": "9056","password": "rNBfNuuANFCAk7KB","cipher": "aes-256-cfb","protocol": "ss"},
    {"server": "217.30.10.64","port": "9041","password": "U6qnYRhfyDmn8sgn","cipher": "aes-256-cfb","protocol": "ss"},
    {"server": "217.30.10.65","port": "9079","password": "TPqX8edgbAURcAMb","cipher": "aes-256-cfb","protocol": "ss"},
    {"server": "217.30.10.65","port": "9042","password": "S7KwUu7yBy58S3Ga","cipher": "aes-256-cfb","protocol": "ss"},
    {"server": "217.30.10.64","port": "9040","password": "p9z5BVADH2YFs3MN","cipher": "aes-256-cfb","protocol": "ss"},
    {"server": "217.30.10.64","port": "9043","password": "HSZuyJQcWe8dxNdF","cipher": "aes-256-cfb","protocol": "ss"},
    {"server": "217.30.10.64","port": "9026","password": "QWDDvVE9npNurQfA","cipher": "aes-256-cfb","protocol": "ss"},
    {"server": "213.183.63.217","port": "9001","password": "UkXRsXvR6buDMG2Y","cipher": "aes-256-cfb","protocol": "ss"},
    {"server": "217.30.10.64","port": "9037","password": "TN2YqghxeFDKZfLU","cipher": "aes-256-cfb","protocol": "ss"},
    {"server": "217.30.10.64","port": "9057","password": "wjTugX3ZtHMB9c3Z","cipher": "aes-256-cfb","protocol": "ss"},
    {"server": "217.30.10.64","port": "9024","password": "BejrQvtu9sqUeNuZ","cipher": "aes-256-cfb","protocol": "ss"},
    {"server": "217.30.10.65","port": "9060","password": "ueLXVkvh4hckhErQ","cipher": "aes-256-cfb","protocol": "ss"},
    {"server": "217.30.10.65","port": "9070","password": "bf7v334KKDV3YDhH","cipher": "aes-256-cfb","protocol": "ss"},
    {"server": "217.30.10.64","port": "9033","password": "UTJA57ypk2XKQpnm","cipher": "aes-256-cfb","protocol": "ss"},
    {"server": "185.167.116.253","port": "9040","password": "p9z5BVADH2YFs3MN","cipher": "aes-256-cfb","protocol": "ss"},
    {"server": "213.183.63.217","port": "9059","password": "9XwYyZsK8SNzQDtY","cipher": "aes-256-cfb","protocol": "ss"},
    {"server": "217.30.10.64","port": "9042","password": "S7KwUu7yBy58S3Ga","cipher": "aes-256-cfb","protocol": "ss"},
    {"server": "217.30.10.64","port": "9094","password": "rpgbNnU9rDDU4aWZ","cipher": "aes-256-cfb","protocol": "ss"},
    # 稳定备用
    {"server": "cdn-cn.nekocloud.cn", "port": "19050", "uuid": "76cb50a4-9fd8-352e-99f4-a7bb5959b07b", "alterId": "0",
     "cipher": "auto", "network": "ws", "ws-path": "/catnet", "protocol": "vmess"},
    {"server": "cdn-cn.nekocloud.cn", "port": "10002", "uuid": "76cb50a4-9fd8-352e-99f4-a7bb5959b07b", "alterId": "0",
     "cipher": "auto", "network": "ws", "ws-path": "/catnet", "protocol": "vmess"},
    {"server": "cdn-cn.nekocloud.cn", "port": "19029", "uuid": "76cb50a4-9fd8-352e-99f4-a7bb5959b07b", "alterId": "0",
     "cipher": "auto", "network": "ws", "ws-path": "/catnet", "protocol": "vmess"},
]


class RedisClient:
    """
    Redis控制单例，包含4张表：
        1. valid = []  # 可用代理的列表
        2. using = {}  # 在使用中的代理字典库 {"pid":{proxyParam}}
        3. unvalid = []  # 已失效代理的列表
        4. listenport = []  # 在使用中使用的端口号
    """

    def __init__(self):
        self.db = redis.Redis(
            host="127.0.0.1",
            port=6379,
            password="meiya@2020",
            db=1,
            decode_responses=True
        )
        self.lock = False

    def list_add(self, r_list, value):
        """
        返回int类型，数值代表列表里有多少个该 value，重复值不冲突
        """
        if type(value) == dict:
            value = json.dumps(value)
        return self.db.lpush(r_list, value)

    def delete(self, key):
        """
        删除key
        """
        return self.db.delete(key)


if __name__ == '__main__':

    rr = RedisClient()

    rr.delete("valid")

    for i in use:
        rr.list_add("valid", json.dumps(i))

    rr.delete("unvaild")
    print("完成")
