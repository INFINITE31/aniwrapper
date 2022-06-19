from setuptools import setup

classifiers = [
    'Development Status :: 3',
    'Intended Audience :: Anime',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.8'
]

setup(
    name='aniwrapper',
    version='0.0.1a',
    description='a python api wrapper for the anime image generator api',
    long_description=open('README.md').read() + '\n\n' +
    open('CHANGELOG.md').read(),
    url="https://github.com/infinite31/aniwrapper",
    author="INFINITE_.",
    author_email='work4infinite@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords=['python', 'image', 'anime', 'api', 'wrapper', 'py'],
    install_requires=['requests']
)
