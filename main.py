from graphic import SteamStats
from logger import loger


@loger
def run_logger_demo():
    print("Тестовая функция логирования выполнена и записана в logs.csv")


@loger
def build_steam_stats():
    stat = SteamStats('steam_players.csv')
    stat.plot(top_n= 100)


if __name__ == '__main__':
    choice = input('Выберите файл для запуска: 1 - logger, 2 - steam_stats: ').strip()
    
    match choice:
        case '1':
            run_logger_demo()
        case '2':
            build_steam_stats()
        case _:
            print("Неверный ввод. Выберите 1 или 2.")