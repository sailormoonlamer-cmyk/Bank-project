class Car:
    def __init__(self, name, price, quantity, color, year):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.color = color
        self.year = year
        
    def show_info(self):
        print("Название", self.name)
        print("Цена", self.price)
        print("Количество", self.quantity)
        print("Цвет", self.color)
        print("Год", self.year)
        
    def sale(self, quantity):
        if quantity <= self.quantity and quantity > 0:
            self.quantity - quantity
            print("Машина(ы) продана")
        else:
            print("Нет столько машин")
            
class AutoSalon:
    def __init__(self,name ):
        self.name = name
        self.cars = []
        
    def add_car(self, neme, price, quantity, color, year):
        car = Car(neme, price, quantity, color, year)
        self.cars.append(car)
        print("Машина добавлена ")
        
    def show_car(self):
            if len(self.cars) == 0:
                print("Машин пока нет!")
            else:
                for car in self.cars:
                    print(" ")
                    car.show_info()
    def search_car(self, name):
        for car in self.cars:
            if car.lower() == name.lower():
                return 
        print("машин не найденна")
        
    def sell_car(self, name, quantity):
        for car in self.cars:
            if car.lower() == name.lower():
                return 
            print("Такой машины нет! ")
            
    def delete_car(self, name):
        for car in self.cars:
            if car.lower() == name.lower():
                self.cars.remove(car)
                print("Машина удалена!")
                return
            print("Машина не найдена! ")
            
def print_menu():         
    print("="*50)
    print("\nДобавить машину")
    print("Показать все машины")
    print("Найти машину")
    print("Продать машину")
    print("Удалить машину")
    print("="*50)
            
def main(): 
    autoSalon = AutoSalon("АвтоЛидер")
    autoSalon.add_car("Ford Model T", 700000, 5, "Black", 1994)
    autoSalon.add_car("Ford Mustang", 2500000, 2, "white", 1964)
    autoSalon.add_car("Volkswagen Golf", 500000, 4, "blue", 1974)
    
    print("Добро пожаловать в АвтоЛидер! ")
    while True:
        print_menu()
        choice = input("Выберете действие: ").strip()
        
        if choice == '1':
            
                name = input("Введите название машины: ")
                price = float(input("Введите цену машины: "))
                quantity = int(input("Введите количетсво машин: "))
                color = input("Введите цвет машины: ")
                year = input("Введите год выпуска машины: ")
                
        elif choice == '2':
            autoSalon.show_cars()
                
            
if __name__ == "__main__":
    main()
        
        
            
            

    
    
            
        
    

            
        
        
    
        
        
    
    
    
        