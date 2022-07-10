import setuptools

with open("README.md", encoding="utf8") as readme, open(
    "requirements.txt", encoding="utf8"
) as requirements:
    long_description = readme.read()
    requires = requirements.read().splitlines(keepends=False)

setuptools.setup(
    name="python_sak",
    packages=setuptools.find_packages(),
    version="6.0.4",
    license="MIT",
    description="Asynchronous Python Wrapper For S.A.R API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="SakirBey1",
    author_email="sakirhack81@gmail.com",
    url="https://github.com/SakirBey1/Python_SAK",
    keywords=["API", "SAK_API", "Python-SAK", "SAK", "S.A.K"],
    install_requires=requires,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
