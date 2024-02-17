from setuptools import setup

setup(
    name='PyParrotSay',
    version='0.0.1',
    scripts=['pyparrotsay.py'],
    author="Hollo",
    author_email="colin.boyett10@gmail.com",
    long_description="# PyParrot\nMake a funny parrot say anything!\nUsage:\n```py\nfrom pyparrotsay import Parrotsay\nparrot = ParrotSay()\n\nparrot.say(\"Hello!\")\n```",
    long_description_content_type="text/markdown",
    requires=[
        "colorama"
    ],
    url="https://github.com/DevHollo/pyparrotsay"
)
