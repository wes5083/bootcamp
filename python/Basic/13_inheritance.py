from Chef import Chef
from ChineseChef import ChineseChef


myChef = Chef()
myChef.make_chicken()
myChef.make_special_dish()

myChineseChef = ChineseChef()
# inherit from Chef
myChineseChef.make_chicken()
myChineseChef.make_fried_rice()
