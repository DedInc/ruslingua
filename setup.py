from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="ruslingua",
    version="1.0.0",
    author="Maehdakvan",
    author_email="visitanimation@google.com",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DedInc/ruslingua",
    project_urls={
        "Bug Tracker": "https://github.com/DedInc/ruslingua/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    install_requires=['requests', 'lxml'],
    python_requires=">=3.6"
)
