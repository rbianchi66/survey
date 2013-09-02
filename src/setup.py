from distutils.core import setup
import py2exe

setup(windows=[{"script" : "alimentazione.py"}], options={"py2exe" : {"includes" : ["sip", "PyQt4", "decimal", "datetime"]}})

