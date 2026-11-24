
import serial
import time 

PORT = "COM3"
BAUD = 9600     

# Константы протокола - [START1][START2][CMD][LEN][DATA][CRC] - один пакет данных 


# ДОЛЖНЫ БЫТЬ УНИКАЛЬНЫЕ
SYNC1 = 0xAA
SYNC2 = 0x55

# команды
CMD_SET_LED = 0x01
CMD_SET_SERVO = 0X02
CMD_BLINK = 0x03
CMD_BUZZER = 0x04

def build_packet(command: int, data: bytes):
    #собираем пакет [START1][START2][CMD][LEN][DATA..][CRC]
    # CRC = сумма (LEN + CMD + DATA)
    length = len(data)
    crc = (length + command + sum(data)) & 0xFF
    
    packet = bytes([SYNC1, SYNC2, command, length]) + bytes(data) + bytes([crc])
    
    return packet

# print(build_packet(CMD_SET_SERVO, [1, 90]))

def send_packet(arduino: serial.Serial, command: int, data: bytes):
    packet = build_packet(command, data)
    
    arduino.write(packet)
    
def main():
    arduino = serial.Serial(PORT, BAUD, timeout=1)
    time.sleep(2)
    arduino.reset_input_buffer()
    
    print("Команды:")
    print(" 1 - SET_LED")
    print(" 2 - SET_SERVO")
    print(" 3 - SET_BLINK")
    print(" 4 - SET_BUZZER")
    print(" 5 - exit ")
    
    while True:
        cmd = input("Введите команду:")
        if cmd == '5':
            break
    
        if cmd == '1':
            try:
                brightness = int(input("Яркость 0-255: ").strip())
                if not (0 <= brightness <= 255):
                    print("Нужно вывести 0-255!")
                    continue
            except ValueError:
                print("Введите число!")
                continue
            
            send_packet(arduino, CMD_SET_LED, bytes([brightness]))

        elif cmd == '2':
            try:    
                angle = int(input("Угол поворота 0-180: ").strip())
                if not (0 <= brightness <= 180):
                    print("Нужно вывести 0-255!")
                    continue
            except ValueError:
                print("Введите число!")
                continue
                
            
            send_packet(arduino, CMD_SET_SERVO,  bytes([angle]))
                
        elif cmd == '3':
            try:
                count = int(input("Количество миганий").strip())
                if (0 <= count <= 10):
                    print("Макс.кол-во  миганий 10")
                    continue
            except ValueError:
                print("Введите число 0-10")        
                continue
            
            send_packet(arduino, CMD_BLINK,  bytes([count]))
                
                
        elif cmd == '4':  
            try:
                freq = int(input("Чистота звучания 0-255: ").strip())
                if (0 <= count <= 255):
                    print("Введите 0-255")
                    continue
            except ValueError:
                print("Введите число 0-10")        
                continue   
    
            send_packet(arduino, CMD_BUZZER,  bytes([freq]))
                
    arduino.close()
    print("Соединения закрыто! ")            
                
                
                
                
                
                
                
                
    
if __name__ == "__main__":
    main() 