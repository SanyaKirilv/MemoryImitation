from Memory import *
from Application import *

class Computer:
    def __init__(self, memory_size):
        self.memory_size = memory_size
        self.memory = Memory(memory_size, 16)
        self.applications = []
        self.log = []
        self.information = ""

    def display_applications_information(self): #Получить информацию о приложениях и их сегментах
        self.information += self.memory.get_list_of_using_segments()
    
    def display_all_information(self): #Получить информацию о всех сегментах
        self.information += self.memory.get_list_of_all_segments()

    def find_application(self, name): #Найти приложение
        for app in self.applications:
            if app.name == name: 
                return True, app
        return False, None

    def install_application(self, name, req_memory): #Установить приложение
        if not self.find_application(name)[0]:
            self.applications.append(Application(name, req_memory, False))
            self.log.append(f"{name} was installed!\r\n")
        else: 
            self.log.append(f"Attention! {name} is already installed.\r\n")

    def delete_application(self, name): #Удлаить приложение по названию
        application = self.find_application(name)
        if application[0]:
            self.close_application(name)
            self.applications.remove(application[1])
            #self.optimize_memory()
            self.log.append(f"{name} was deleted!\r\n")
        else:
            self.log.append(f"Attention! {name} don`t be found.\r\n")

    def close_application(self, name): #Закрыть приложение по назваению
        application = self.find_application(name)
        if application[0]:
            self.memory.clear_application_memory(application[1], self.log)
        else:
            self.log.append(f"Attention! {name} don`t be found.\r\n")

    def close_all_applications(self): #Закрыть все приложения
        running_applications = self.memory.get_list_of_running_applications()
        if len(running_applications) > 0:
            for application in running_applications:
                self.close_application(application)
            self.log.append(f"All applications are closed.\r\n")
        else:
            self.log.append(f"Attention! All applications is already closed.\r\n")

    def run_application(self, name): #Запуск приложения по названаю
        application = self.find_application(name)
        if application[0]:
            self.memory.use_memory(application[1], self.log)
        else:
            self.log.append(f"Attention! {name} don`t be found.\r\n")

    def optimize_memory(self): #Оптимизация памяти
        running_applications = self.memory.get_list_of_running_applications()
        self.close_all_applications()
        for application in running_applications:
            self.run_application(application)

    def get_log_information(self):
        data = ""
        for line in self.log:
            data += line
        return data 
        