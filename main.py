from folders import *


folder = folders()

root = folder.selectRoot()
dest = folder.selectDestination()
# print(root)
# print(dest)

folder.copyElements(root,dest)