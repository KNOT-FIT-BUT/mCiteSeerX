from distutils.core import setup

setup(
    name='Citeseerx',
    version='0.1.0',
    author='Martin Maga',
    author_email='xmagam00@stud.fit.vutbr.cz',
    packages=['citeseerx'],
    url='https://github.com/KNOT-GIT/mCiteSeerX',
    license='LICENSE.txt',
    description='Python API module for citeseerx.ist.psu.edu',
    long_description=open('README.md').read(),
    install_requires=[
        "beautifulsoup4 >= 4.0.1",
    ],
)
