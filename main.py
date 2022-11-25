from Computer import *

laptop = Computer(128)

laptop.install_application("VS Code", 16)
laptop.install_application("Word", 32)
laptop.install_application("Google Chrome", 64)

laptop.run_application("Word")
laptop.run_application("VS Code")
laptop.run_application("Word")

laptop.delete_application("Word")
laptop.run_application("Google Chrome")

laptop.display_applications_information()
laptop.display_all_information()
print(laptop.get_log_information())
print(laptop.information)

laptop.optimize_memory()

laptop.display_applications_information()
laptop.display_all_information()
print(laptop.get_log_information())
print(laptop.information)
