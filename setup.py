import setuptools

with open('requirements.txt', 'r') as f:
    install_requires = f.read().splitlines()

entry_points = {
    'console_scripts': [
        'simplesig = simplesig.console:main',
    ]
}
setuptools.setup(name='simplesig',
                 packages=['simplesig'],
                 install_requires=install_requires,
                 python_requires='>=3.8',
                 entry_points=entry_points)
