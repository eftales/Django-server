from yolo import YOLO, detect_video
from PIL import Image
import socket


def detect_img(yolo):

    try:
        image = Image.open('YOLO0.jpg')
    except:
        print('Open Error! Try again!')
    else:
        r_image, detect_result = yolo.detect_image(image)
        # r_image.show()
        r_image.save('YOLO1.jpg')
        # print(detect_result)

    return detect_result


yolo = YOLO()
host = '127.0.0.1'
port = 1918


serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket.bind((host, port))
serversocket.listen(2)
print('socket')
while True:
    # 建立客户端连接
    clientsocket, addr = serversocket.accept()

    msg = clientsocket.recv(1024)
    print(msg.decode('utf-8'))
    detect_result = detect_img(yolo)
    #print('--**--', list(detect_result))
    #print(detect_result)
    clientsocket.sendall('YOLO is done'.encode('utf-8'))
    msg = ''
    for each in detect_result:
        msg += each + ':' + str(detect_result[each]) + '\n'
    clientsocket.sendall(msg.encode('utf-8'))
    clientsocket.close()
