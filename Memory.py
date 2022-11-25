from Application import *

class Memory:
    def __init__(self, memory_size = 256, segment_size = 64):
        self.memory_size = memory_size
        self.cell_size = segment_size
        self.cells = [[i, None] for i in range(0, int(self.memory_size/self.cell_size))]

    def free_cells(self):
        n = 0
        for cell in self.cells:
            if cell[1] == None: n += 1
        return n

    def running_apps(self):
        apps = []
        for cell in self.cells:
            if not cell[1] == None and not cell[1] in apps:
                apps.append(cell[1])
        return apps

    def using_cells(self):
        running_apps = self.running_apps()
        data = "Используемые ячейки: \n\r"
        for app in running_apps:
            data += f"{app} использует "
            for cell in self.cells:
                if cell[1] == app:
                    data += f"[{str(cell[0])}]"
            data += " ячейки/s\n\r"
        return data

    def all_cells(self): 
        data = "Все ячейки: \n\r"
        for cell in self.cells:
            data += f"Ячейка: [{cell[0]}], Приложение: [{cell[1]}]\n\r"
        return data

    def use_memory(self, app, log):
        if not app.status:
            self.req_cell = app.req_memory/self.cell_size
            if self.free_cells() >= self.req_cell:
                for cell in self.cells:
                    if cell[1] == None and self.req_cell > 0: 
                        cell[1] = app.name
                        self.req_cell -= 1
                app.status = True
                log.append(f"{app.name} открыто!\n\r")
        else: 
            log.append(f"{app.name} уже открыто.\n\r")

    def clear_memory(self, app, log):
        if app.status:
            for segment in self.cells:
                if segment[1] == app.name: segment[1] = None
            app.status = False
            log.append(f"{app.name} закрыто!\n\r")
        else: 
            log.append(f"{app.name} уже закрыто.\r\n")
