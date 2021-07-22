import socket
# Mark's Pi server is 31.125.90.16
# Polho dxantix server is 80.229.141.232
HOST = '80.229.141.232'
PORT = 4472
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    input_prompt = 'Message text (leave blank to end the program) '
    while True:
        message=input(input_prompt)
        if message == '':
            break
        else:
            data_out=bytes(message,'utf-8')
            s.sendall(data_out)
            data_in = s.recv(1024)
            print('---- Sent ---- ', repr(data_out))
            print('-- Received -- ', repr(data_in))
