from .University import *
university=University()
def close():
        return
MENU = [
        ["добавить студента", university.new_stu],
        ["добавить старосту", university.new_sta],
        ["вывести список на экран", university.read],
        ["записать список в файл", university.write_f],
        ["считать список из файла", university.read_f],
        ["редактировать объект", university.change],
        ["очистить список", university.clear],
        ["выход", close],
    ]
def main():
    print("------------------------------")
    i = 0
    for item in MENU:
        print("{0:2}. {1}".format(i, item[0]))
        i += 1
    print("------------------------------")
    opt = int(input())
    MENU[opt][1]()
    if opt != 7:
                main()
                
if __name__ == "__main__":
        try:
                main()
        except:
                print("неверный ввод")


