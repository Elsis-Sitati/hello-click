# making the installer for this python pacakage

try:
    # setuptools allows you to specify all the various attributes for this package
    # all systems may not have set up tools installed thats why we try
    from setuptools import setup
except ImportError:
    # all versions of python come with distutils so it will fall back to
    # distutils incase setuptools is not found
    from distutils.core import setup

# do not specify the version so that the latest is installed on install
dependencies = ['Click']

setup(
    # name for the application
    name="HelloWorld",
    version="1.0",
    install_requires=dependencies,
    # defining the module we should install
    py_modules=["hello", ],
    # we have an executable called hello accessing the hello module and
    # executing the click function

    entry_points='''
		[console_scripts]
		hello=hello:cli
	''',
)
