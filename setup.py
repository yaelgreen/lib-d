import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lib-d",
    version="0.0.1",
    author="Yael Green",
    author_email="yaelgreen65@gmail.com",
    description="A Library for python-monorepo-example",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yaelgreen/lib-d",
    project_urls={
        "Bug Tracker": "https://github.com/yaelgreen/lib-d/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
)