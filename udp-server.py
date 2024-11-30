import socket
import os
import faker
import random

# faker.Fakerクラスのインスタンスを作成
fake = faker.Faker()

# socket.socket関数で新規ソケット作成
# AF_UNIXはUNIXドメインソケット、SOCK_DGRAMはUDPソケット
sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

# サーバが接続を待ち受けるUNIXドメインソケットのパス
server_address = './udp_socket_file'

try:
    # もしソケットファイルが残っていたら削除
    os.unlink(server_address)
except FileNotFoundError:
    # ファイルが存在していない場合は何もしない
    pass

# ソケットが起動していることを表示
print('starting up on {}'.format(server_address))

# sockオブジェクトのbindメソッドを使って、ソケットを特定のアドレスに関連付ける
sock.bind(server_address)

# ソケットはデータの受信を永遠に待ち続ける
while True:
    print('\nwaiting to receive message')

    # ソケットからのデータを受信。4096は一度に受信できる最大バイト数
    data, address = sock.recvfrom(4096)

    # 受信したデータのバイト数と送信元のアドレスを表示
    print('received {} bytes from {}'.format(len(data), address))
    print(data)

    # 受信したデータをそのまま送信元に返す
    if data:
        response = ""
        if data == b'1':
            response = "お大事にしてください。"
        elif data == b'2':
            response = "へえ。"
        elif data == b'3':
            response = "それは良かったです！"
        else:
            response = "無効な選択肢です。"

        # ランダムな占いや絵文字を追加
        random_message = fake.sentence() + " " + random.choice(["😊", "🌟", "🍀", "🎉"])
        response += " " + random_message

        sent = sock.sendto(response.encode('utf-8'), address)
        print('sent {} bytes back to {}'.format(sent, address))