import serial
import time

PORT = "COM3"
BAUD = 9600

def main():
    # открытие порта
    arduino = serial.Serial(PORT, BAUD, timeout=1)
    
    # Ждем 2 секунды после открытия порта
    time.sleep(2)
    arduino.reset_input_buffer()

    print("Подкючено к Arduino")
    print("Введите угол поворота сервы( или q для выхода): ")
    try:
        while True:
            if arduino.in_waiting >= 4:
                data = arduino.read(4)
                byte1, byte2, byte3, byte4 = data[0], data[1], data[2], data[3]
                
                # high = arduino.read(1)[0]
                # low = arduino.read(1)[0]
                # data = arduino.read(2)
                # high, low = data[0], data[1]
                
                # value = (high << 8 ) | low
                value = (byte1 << 24) | (byte2 << 16) | (byte3 << 8) | byte4
                
                print(value)
    except KeyboardInterrupt:
        print("Остановлено!")
        # Закрываем порт
    finally:
        arduino.close()
        print('Порт закрыт')
    

if __name__ == "__main__":
    main()   
    
    
    
    
    

    
    



