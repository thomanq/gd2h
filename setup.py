from distutils.core import setup
 
setup(
    name='gd2h',
    version='0.1.0',
    packages=[],
    license='',
    description='Git diff to HTML',
    long_description=open('README.md').read(),
    author='Thomas Anquetin',
    author_email='',
    install_requires=[''],
    entry_points={
        'console_scripts': [
            'gd2h = gd2h:main',
        ]
    }
)