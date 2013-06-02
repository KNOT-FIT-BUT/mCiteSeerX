from distutils.core import setup

setup(
    name='Citeseerx',
    version='0.1.0',
    author='Martin Maga',
    author_email='xmagam00@stud.fit.vutbr.cz',
    packages=['dist'],
    scripts=['citeseerx/citeseerx.py'],
    url='https://github.com/KNOT-GIT/mCiteSeerX',
    license='LICENSE.txt',
    description='Python API module for citeseerx.ist.psu.edu',
    long_description=open('README.md').read(),
    install_requires=[
        "Beautiful Soup 4.0.1",
    ],
)
