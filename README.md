## faker を venv 環境でインストール

```python3
python3 -m venv venv

# venv 環境を有効化
source venv/bin/activate

python3.13 -m pip install --upgrade pip

pip install faker
```

## クライアントアプリ起動

```python
python3 udp-client.py
```

## サーバアプリ起動

```python
python3 udp-server.py
```
