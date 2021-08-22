import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="wikionary",
    version="1.0.0",
    author="Maehdakvan",
    author_email="visitanimation@google.com",
    description="Модуль для поиска Синонимов, Антонимов и Фразеологизмов.",
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
    packages=["wikionary"],
    install_requires=['requests', 'lxml'],
    python_requires=">=3.6"
)
