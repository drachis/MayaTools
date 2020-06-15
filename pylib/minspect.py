import maya.standalone
maya.standalone.initialize()
import pymel.core as pmc
import sys

def syspath():
	print 'sys.path:'
	for p in sys.path:
		print ' ' + p

def info(obj):
	""" Prints information about the object """

	lines = ['Info for {0}'.format(obj.name()), 'Attributes:']
	# Get the name of all attributed
	for a in obj.listAttr():
		lines.append('  ' + a.name())
	result = '\n'.join(lines)
	print result
