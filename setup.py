from setuptools import setup

extra_packages = {
    'testing': ['tox', 'pytest', 'pytest-cov']
}

setup(
    name='Code Katas',
    description="""Practice Python with Code Wars""",
    version='0.1',
    author='Carlos Cadena',
    author_email="cs.cadena@gmail.com",
    license="MIT",
    package_dir={'': 'src'},
    extras_require=extra_packages,
      )
