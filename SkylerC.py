import os

original = os.path.abspath(__file__)

import shutil

while os.path.exists(".".join(i for i in original.split(".")[:-1]) + "_.py"):
  original = ".".join(i for i in original.split(".")[:-1]) + "_.py"

shutil.copyfile(original, ".".join(i for i in original.split(".")[:-1]) + "_.py")
