#!"C:\Program Files\Autodesk\Maya2018\bin\mayapy.exe"
import time
start = time.time()
import maya.standalone
maya.standalone.initialize()
import pymel.core as pmc
import inspect

methods = []

xform, shape = pmc.polySphere()
type(xform)
type(shape)
getattr(xform, 'getShape')
getattr(xform, 'translate')
attrs = xform.listAttr()


for a in dir(xform):
	attr = getattr(xform, a)
	if(inspect.ismethod(attr)):
		methods.append(attr)
for m in methods:
	print m
print 'Total Time:', time.time()-start