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
print methods
