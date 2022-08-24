from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="Bitdesc",
    version='0.1.5',
    description="Bio-Inspired Texture Descriptor",
    py_modules=["ClassBit", "Channel_Split", "BiT", "Biodiversity", "Taxonomic"],
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=["opencv-python ~= 4.5.1.48", "Scipy ~= 1.6.2", "Numpy", "Pillow ~= 8.2.0"],
    extras_require = {
        "dev":[
            "pytest>=3.7",
        ],
    },
    find_packages = find_packages(),
    url="https://github.com/stmata/BiT",
    author="Steve Ataky & Alessandro Koerich",
    author_email="steve.ataky@nca.ufma.br",
    keywords='texture descriptor, invariant, bio-inspired, texture-classification',
    licence='BSD',
    include_package_data=True
)