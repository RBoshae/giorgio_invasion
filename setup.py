import cx_Freeze

executables = [cx_Freeze.Executable("./src/giorgio_invasion.py")]

cx_Freeze.setup(
    name='giorgio_invasion',
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["./src", "./images", "./sound"]}},
    executables = executables,
    version='1.0',
    author='Rick Boshae',
    author_email='',
    description=''
)
