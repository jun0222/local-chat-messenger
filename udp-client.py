import socket

# INIXドメインソケットとデータグラム（非接続型）ソケットを作成
sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

# サーバのアドレスを定義。サーバはこのアドレスでメッセージを待ち受ける
server_address = './udp_socket_file'

# クライアントのアドレスを定義。サーバはここにメッセージを返信
client_address = './udp_client_socket_file'

# サーバに送信するメッセージを定義
message = b'Message to send to the client'

# クライアントのアドレスをソケットに紐付け。UNIXドメインソケットの場合。
# サーバによって送信元として受け取られる
sock.bind(client_address)

try:
    # サーバにメッセージを送信
    print('sending {!r}'.format(message))
    sent = sock.sendto(message, server_address)

    # サーバからの応答を待ち受ける
    print('waiting to receive')

    # 最大4096バイトのデータを受信
    data, server = sock.recvfrom(4096)

    # サーバから受け取ったメッセージを表示
    print('received {!r}'.format(data))

finally:
    # 最後にソケットを閉じてリソースを解放
    print('closing socket')
    sock.close()