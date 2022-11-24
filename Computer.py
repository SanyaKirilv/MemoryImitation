from Memory import *
from Application import *

class Computer:
    def __init__(self, memory_size):
        self.memory_size = memory_size
        self.memory = Memory(memory_size, 16)
        self.applications = []
        self.log = ""
        self.information = ""

    def display_applications_information(self):
        self.information += self.memory.get_list_of_using_segments()
    
    def display_all_information(self):
        self.information += self.memory.get_list_of_all_segments()

    def find_application(self, name):
        for app in self.applications:
            if app.name == name: 
                return True, app
        return False, None

    def install_application(self, name, req_memory):
        if not self.find_application(name)[0]:
            self.applications.append(Application(name, req_memory, False))
            self.log += f"{name} was installed!"
        else: 
            self.log += f"Attention! {name} is already installed."

    def delete_application(self, name):
        application = self.find_application(name)
        if application[0]:
            self.close_application(name)
            self.applications.remove(application[1])
            #self.optimize_memory()
            self.log += f"{name} was deleted!"
        else:
            self.log += f"Attention! {name} don`t be found."

    def close_application(self, name):
        application = self.find_application(name)
        if application[0]:
            self.memory.clear_application_memory(application[1], self.log)
        else:
            self.log += f"Attention! {name} don`t be found."

    def close_all_applications(self):
        running_applications = self.memory.get_list_of_running_applications()
        if len(running_applications) > 0:
            for application in running_applications:
                self.close_application(application)
            self.log += f"All applications are closed."
        else:
            self.log += f"Attention! All applications is already closed."

    def run_application(self, name):
        application = self.find_application(name)
        if application[0]:
            self.memory.use_memory(application[1], self.log)
        else:
            self.log += f"Attention! {name} don`t be found."

    def optimize_memory(self):
        running_applications = self.memory.get_list_of_running_applications()
        self.close_all_applications()
        for application in running_applications:
            self.run_application(application)
        