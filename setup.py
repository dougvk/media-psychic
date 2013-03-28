from setuptools import setup

dependencies = [
    'numpy',
    'scipy',
    'Django',
    'nose',
    'dj-database-url',
]

project_name = 'media-psychic'
project_version = '0.1'
python_version = 'py2.7'

setup(
    name=project_name,
    version=project_version,
    author="Media Psychic",
    description=("An intelligence API"),
    license="All Rights Reserved",
    install_requires=dependencies,
    classifiers=[
    "Development Status :: 2 - Beta",
    ],
    zip_safe=False,
)
