from setuptools import setup, find_packages

setup(
    name="vm_observability",
    version="0.1",
    packages=find_packages(),
    install_requires=["psutil"],  # Dependency
    author="parth setia",
    author_email="parthsetia509@gmail.com",
    description="A library to fetch CPU, memory, disk, network, and process metrics of a VM",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/parthsetia1/vm_observability",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
