from setuptools import setup, find_packages

setup(
    name='edsajonathan',
    version='0.3',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/<username>/<package-name>',
    author='<Your Name>',
    author_email='<Your Email>'
)
