import socket

# INIXドメインソケットとデータグラム（非接続型）ソケットを作成
sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

# もしソケットファイルが残っていたら削除
try:
    import os
    os.unlink('./udp_client_socket_file')
except FileNotFoundError:
    pass

# サーバのアドレスを定義。サーバはこのアドレスでメッセージを待ち受ける
server_address = './udp_socket_file'

# クライアントのアドレスを定義。サーバはここにメッセージを返信
client_address = './udp_client_socket_file'

# クライアントのアドレスをソケットに紐付け。UNIXドメインソケットの場合。
# サーバによって送信元として受け取られる
sock.bind(client_address)

try:
    # ユーザー入力を受け取る
    user_input = input("お元気ですか？\n1: あまり元気ではない\n2: 普通\n3: とても元気\n選択肢を入力してください: ")
    message = user_input.encode()

    # サーバにメッセージを送信
    print(f'Sending {message} to {server_address}')
    sent = sock.sendto(message, server_address)

    # サーバからの応答を待ち受ける
    print('waiting to receive')

    # 最大4096バイトのデータを受信
    data, server = sock.recvfrom(4096)

    # サーバから受け取ったメッセージを表示
    print('received {}'.format(data.decode('utf-8')))

finally:
    # 最後にソケットを閉じてリソースを解放
    print('closing socket')
    sock.close()