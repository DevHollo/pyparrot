from setuptools import setup

setup(
    name='PyParrotSay',
    version='0.0.4',
    scripts=['pyparrotsay.py'],
    author="Hollo",
    author_email="colin.boyett10@gmail.com",
    long_description="# PyParrotSay\nMake a funny parrot say anything!<br/>\nUsage:\n```py\nfrom pyparrotsay import ParrotSay\n\nparrot = ParrotSay()\n\nparrot.say(\"Hello!\")\n```",
    long_description_content_type="text/markdown",
    install_requires=[
        "colorama==0.4.6"
    ],
    url="https://github.com/DevHollo/pyparrotsay"
)
