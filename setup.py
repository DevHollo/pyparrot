from setuptools import setup

with open('README.md', 'r') as mdfile:
    des = mdfile.read()

setup(
    name='PyParrotSay',
    version='0.0.7',
    scripts=['pyparrotsay.py'],
    author="Hollo",
    author_email="colin.boyett10@gmail.com",
    long_description=des,
    long_description_content_type="text/markdown",
    install_requires=[
        "colorama==0.4.6"
    ],
    url="https://github.com/DevHollo/pyparrotsay"
)
