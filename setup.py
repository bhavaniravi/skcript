from setuptools import setup

setup(
    name="skcript-cli",
    version='0.1',
    py_modules=['cli'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        magic=solution.cli:magic
        longest=solution.cli:longest
    ''',
)
