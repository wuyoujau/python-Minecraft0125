from mcpi.minecraft import Minecraft 
weed = Minecraft.create()

weed.postToChat("I'm watching you")
 
while True:
     x,y,z = weed.player.getTilePos()
     weed.postToChat(" X:"+str(x)+" Y:"+str(y)+" Z:"+str(z))