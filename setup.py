from setuptools import setup

setup(
    name='Athena',
    version='0.0.0a',
    long_description=__doc__,
    packages=['Athena'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask>=0.10.0'
    ]
)
