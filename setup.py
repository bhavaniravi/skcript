from setuptools import setup

setup(
    name="magic",
    version='0.1',
    py_modules=['cli'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        magic=cli:magic
	longest=cli:longest
    ''',
)
