import setuptools

setuptools.setup(
    name="otus_tests",
    version="0.0.1",
    author="avdvnk",
    author_email="avdvnk@example.com",
    description="Package for otus tests",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/avdvnk/qa-otus-course",
    packages=setuptools.find_packages(),
    setup_requires=[
        "pytest", "requests", "selenium", "datetime"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    zip_safe=False
)
