from cx_Freeze import *
includefiles=['kingbondl.ico','text_translator.py','google_language_find.py','kingbondl.ico']
excludes=[]
packages=[]
base=None
if sys.platform=='win32':
	base='Win32GUI'
shortcut_table=[(
	'DesktopShortcut', #Shortcut
	'DesktopFolder', #Directory_
	'KingbondL Text Translator', #Name
	'TARGETDIR', #Component_
	'[TARGETDIR]\text_translator.exe', #Target
	None, #Arguments
	None, #Description
	None, #Hottkey
	None, #Icon
	None, #IconIndex
	None, #ShowCmd
	'TARGETDIR', #WkDir
	)
]
msi_data={'Shortcut':shortcut_table}
bdist_msi_options={'data':msi_data}
setup(
	version='0.1',
	description='It is a beta version of Text Translator with python and It is developed for educational purpose.If you have any other project ideas or some modification required in this application then you can contact me on my social account social account: insta-kingbondl,github-kingbond470,twitter-@mausamsingh470',
	author='Mausam Singh',
	name='KingbondL Text Translator',
	options={'build_exe':{'include_files':includefiles},'bdist_msi':bdist_msi_options,},
	executables=[
	Executable(
		script='text_translator.py',
		base=base,
		icon='kingbondl.ico',
		)
	]
)