import serial
import time

PORT = "COM3"
BAUD = 9600

def main():
    # открытие порта
    arduino = serial.Serial(PORT, BAUD, timeout=1)
    
    # Ждем 2 секунды после открытия порта
    time.sleep(2)

    print("Подкючено к Arduino")
    print("Введите угол поворота сервы( или q для выхода): ")
    
    while True:
        angle = input("Угол  -> ").strip()
        if angle == "q":
            print("Выходим...")
            break
     
        # Проверка на число
        try:
            angle = int(angle)
            # if not (0 <= angle <= 180):
            #     print("Угол должен быть от 0 до 180")
            #     continue
        except ValueError:
            print("Введите число!!! ")
            continue
                
                
        # Отправляем байт в ардуино 
        # arduino.write(bytes([angle]))
        # print(f'Отправлено: {angle}')
        high = (angle >> 8) & 0xFF
        low = angle & 0xFF
        
        arduino.write(bytes([low, high]))
        
        
        # Читаем ответ от ардуино
        time.sleep(0.1)
        if arduino.in_waiting > 0:
            response = arduino.readline().decode("utf-8").strip()
            print(f'Получено от Ардуино: {response}')
            

        # Закрываем порт
    arduino.close()
    print('Порт закрыт')

if __name__ == "__main__":
    main()   
    
    
    
    
    

    
    



