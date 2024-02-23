import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="chemax",
    version="0.0.1",
    author="HisAtri",
    author_email="ylsymc@outlook.com",
    description="Easily calculate the m.w. and e.m of a molecule",
    install_requires=[],
    long_description=open(r'README.md', encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/HisAtri/Eccrypto",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)