from setuptools import setup,find_packages
print (find_packages())
setup(
    name="wordmagic",
    version='0.1',
    packages = find_packages(),
    py_modules=['solution'],
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        magic=solution.cli:magic
        longest=solution.cli:longest
    ''',
)
