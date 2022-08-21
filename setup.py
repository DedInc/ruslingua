from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="wikionary",
    version="1.2.1",
    author="Maehdakvan",
    author_email="visitanimation@google.com",
    description="Модуль для поиска Синонимов, Антонимов и т.д.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DedInc/wikionary",
    project_urls={
        "Bug Tracker": "https://github.com/DedInc/wikionary/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    install_requires=['requests', 'lxml', 'pymorphy2'],
    python_requires=">=3.6"
)
