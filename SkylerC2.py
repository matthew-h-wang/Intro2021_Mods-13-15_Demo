import os

original = os.path.abspath(__file__)

import shutil

removeDotPy = lambda x: ".".join(x.split(".")[:-1])

getBase = lambda x: "SkylerC".join(removeDotPy(x).split("SkylerC")[:-1]) + "SkylerC"

getNumber = lambda x: int(removeDotPy(x).split("SkylerC")[-1])

while os.path.exists("%s%d%s" % (getBase(original), getNumber(original)+1, ".py")):
  original = "%s%d%s" % (getBase(original), getNumber(original)+1, ".py")


print("%s%d%s" % (getBase(original), getNumber(original)+1, ".py"))

shutil.copyfile(original, "%s%d%s" % (getBase(original), getNumber(original)+1, ".py"))
