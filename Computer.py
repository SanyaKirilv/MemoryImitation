from Memory import *
from Application import *

class Computer:
    def __init__(self, memory_size):
        self.memory_size = memory_size
        self.memory = Memory(memory_size, 16)
        self.apps = []
        self.log = []
        self.information = ""

    def info(self):
        self.information += self.memory.using_cells()
        self.information += self.memory.all_cells()

    def find(self, name):
        for app in self.apps:
            if app.name == name: return True, app
        return False, None

    def install(self, name, req_memory):
        if not self.find(name)[0]:
            self.apps.append(Application(name, req_memory, False))
            self.log.append(f"{name} установлено!\r\n")
        else: 
            self.log.append(f"{name} уже установлено.\r\n")

    def delete(self, name):
        app = self.find(name)
        if app[0]:
            self.close(name)
            self.apps.remove(app[1])
            self.log.append(f"{name} удалено!\r\n")
        else:
            self.log.append(f"{name} не найдено.\r\n")

    def close(self, name):
        application = self.find(name)
        if application[0]:
            self.memory.clear_memory(application[1], self.log)
        else:
            self.log.append(f"{name} не найдено.\r\n")

    def close_all_applications(self):
        running_applications = self.memory.running_apps()
        if len(running_applications) > 0:
            for application in running_applications:
                self.close(application)
            self.log.append(f"Все приложения закрыты.\r\n")
        else:
            self.log.append(f"Все приложения уже закрыты.\r\n")

    def run(self, name):
        application = self.find(name)
        if application[0]:
            self.memory.use_memory(application[1], self.log)
        else:
            self.log.append(f"{name} не найдено.\r\n")

    def get_log_information(self):
        data = ""
        for line in self.log:
            data += line
        return data 
        