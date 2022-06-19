from setuptools import setup , find_packages

classifiers = [
    'Development Status :: 1 - Planning',
    'Intended Audience :: Developers',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='aniwrapper',
    version='1.0.0a',
    description='a python api wrapper for the anime image generator api',
    long_description=open('README.md').read(),
    long_description_content_type = 'text/markdown',
    url="https://github.com/infinite31/aniwrapper",
    author="INFINITE_.",
    author_email='work4infinite@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords=['python', 'image', 'anime', 'api', 'wrapper', 'py'],
    install_requires=['requests'],
    packages=find_packages()
)

