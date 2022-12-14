from Application import *

class Memory:
    def __init__(self, memory_size, segment_size = 64):
        self.memory_size = memory_size
        self.segment_size = segment_size
        self.segments = [[i, None] for i in range(0, int(self.memory_size/self.segment_size))]

    def get_count_of_free_segments(self): #Получить свободные сегменты
        count = 0
        for segment in self.segments:
            if segment[1] == None: 
                count += 1
        return count

    def get_list_of_running_applications(self): #Получить список запущенных приложений в памяти
        applications = []
        for segment in self.segments:
            if not segment[1] == None and not segment[1] in applications:
                applications.append(segment[1])
        return applications

    def get_list_of_using_segments(self): #Получить список используемых сегментов
        running_applications = self.get_list_of_running_applications()
        data = "Using segments: \n\r"
        for application in running_applications:
            data += f"Application: {application} use "
            for segment in self.segments:
                if segment[1] == application:
                    data += f"[{str(segment[0])}]"
            data += " segment/s\n\r"
        return data

    def get_list_of_all_segments(self): #Получить список всех сегментов памяти 
        data = "All segments: \n\r"
        for segment in self.segments:
            data += f"Segment: [{segment[0]}], Application: [{segment[1]}]\n\r"
        return data

    def use_memory(self, application, log): #Использование памяти после запуска приложения
        if not application.status:
            self.req_segments = application.req_memory/self.segment_size
            if self.get_count_of_free_segments() >= self.req_segments:
                for segment in self.segments:
                    if segment[1] == None and self.req_segments > 0: 
                        segment[1] = application.name
                        self.req_segments -= 1
                application.status = True
                log.append(f"{application.name} is open!\n\r")
        else: 
            log.append(f"Attention! {application.name} is already open.\n\r")

    def clear_application_memory(self, application, log): #Очистка памяти после закрытия приложения
        if application.status:
            for segment in self.segments:
                if segment[1] == application.name: segment[1] = None
            application.status = False
            log.append(f"{application.name} is finally closed!\n\r")
        else: 
            log.append(f"Attention! {application.name} is already closed.\r\n")
