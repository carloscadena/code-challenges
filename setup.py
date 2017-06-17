from setuptools import setup

dependencies = ['pytest', 'pytest-cov']
extra_packages = {
    'testing': ['tox']
}

setup(
    name='Code Katas',
    description="""Practice Python with Code Wars""",
    version='0.1',
    author='Carlos Cadena',
    author_email="cs.cadena@gmail.com",
    license="MIT",
    py_modules=[],
    package_dir={'': 'src'},
    install_requires=dependencies,
    extras_require=extra_packages,
    entry_points={}
      )
