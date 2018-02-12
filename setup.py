from cx_Freeze import setup, Executable
setup(name = 'myExample',
	   version = '0.1',
	   description = 'parse stuff',
	   executables = [Executable("cx-module-44.py")])