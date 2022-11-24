from Computer import *

laptop = Computer(128)
#instaling appplications
laptop.install_application("VS Code", 16)
laptop.install_application("Google Chrome", 64)

#running appplications
laptop.run_application("VS Code")
laptop.run_application("Google Chrome")

laptop.delete_application("Dota")

laptop.display_applications_information()
laptop.display_all_information()
laptop.optimize_memory()

#Informaion about applications
print(laptop.log)

#Informaion about segments
print(laptop.information)