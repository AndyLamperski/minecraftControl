import discoverSTEM.vehicles as vh
import discoverSTEM.minecraft as mc

layout = mc.smallLayout
x,y=  layout.start
vehicle = vh.car((-x,-1,y),controller=None)

vehicle = vh.quadcopter((-x,1,y),controller=None)

mc.generalSystem(layout,vehicle)
