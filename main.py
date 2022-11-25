from Computer import *

pc = Computer(256)

pc.install("Paint", 16)
pc.install("PowerPoint", 42)
pc.install("MS Edge", 32)

pc.run("Paint")
pc.run("PowerPoint")

pc.delete("Paint")
pc.run("MS Edge")

pc.info()
print(pc.get_log_information())
print(pc.information)
