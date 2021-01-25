from mcpi.minecraft import Minecraft 
weed = Minecraft.create()
import time

i=0
while True:
    i=i+1
    weed.postToChat("第"+str(i)+"次")
    time.sleep(3)
