from mcpi.minecraft import Minecraft 
import time
weed = Minecraft.creat()

x=200
y=200
z=100

weed.player.setTilePos(x,y,z)
time.sleep(2)

x=x-50
y=y-50

weed.player.setTilePos(x,y,z)
time.sleep(2)

x=x-50
y=y-50

weed.player.setTilePos(x,y,z)