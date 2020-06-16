#!"C:\Program Files\Autodesk\Maya2018\bin\mayapy.exe"
import sys
print sys.version, sys.executable, sys.path
import maya
maya.standalone.initialize()
print help(maya)