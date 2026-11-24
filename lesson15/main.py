
from environs import Env
from pydantic import BaseModel

# Создаем объект 
env = Env()
# Читаем переменные окружения 
env.read_env()


login = env('LOGIN')
password = env('PASSWORD')
bot_id = env('BOT_ID')

# print(login, password, bot_id)

class LogData(BaseModel):
    log: str = None
    pasw: str = None
    bot: str = None 


class WeathetData(BaseModel):
    city: str = None
    temp: float = None
    hun: float = None
    description: str = None

class Config(BaseModel):
    log_data: LogData
    WeathetData: WeathetData
    







# conf = Config(log=login, pasw=password, bot=bot_id)

# print(conf.bot)
# print(conf.log)
# print(conf.pasw)


conf = Config(
    log_data=LogData(log=env('LOGIN'), pasw=password('PASSWORD'), bot=bot_id('BOT_ID'))
    Weathet_data=WeathetData(city='Чебоксары', temp=0, hum=80, discription='Прохладно и сыро')
)

print(f'Данные пользователя: {conf.log_data.log}')
print(f'Прогноз погоды: в городе {conf.WeathetData.city} | температура: {conf.WeathetData.temp} | {conf.WeathetData.description}')