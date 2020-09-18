import ssl
import websocket

# from websocket import create_connection

ws = websocket.WebSocket(sslopt={"cert_reqs": ssl.CERT_NONE})
ws.connect("wss://remakeaon.com/ws/upload/")

# message = """
# {"type":"pic", "name":"pic1.png", "msg":"https://i.imgur.com/ssCZLi2.png"} """
# ws.send(message)

# result =  ws.recv()
# print(result)

try:
    with open('urls.txt', 'rt') as urls:
        count = 0
        line = urls.readline()

        while line != '':
            count += 1
            ws.send(line.strip())
            result =  ws.recv()
            print(result)
            line = urls.readline()
except Exception as e:
    print(e)

result = ws.send('statistics')
print(result)

ws.close()