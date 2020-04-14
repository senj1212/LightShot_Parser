import func
import threading

def scren():
    flow = func.Img()
    while True:
        try:
            page_r, url_two = flow.go_to_url()
            if 'has banned your IP' in page_r:
                print('Ip в бане.')
            else:
                page = flow.find_img(page_r)
                if page is not None:
                    flow.download_and_save(page, url_two)
        except OSError:
            print('Разрыв сети...(Переподключение)')


menu = [scren]

act = int(input('0: Парсер скриншотов;\n'))
enter_quantity = int(input('Количество потоков(скорость поиска и нагрузка на пк, рекомендуеться 5): '))
for i in range(0, enter_quantity):
    threading.Thread(target=menu[act]).start()
