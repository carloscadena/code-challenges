from setuptools import setup

dependencies = ['pytest', 'pytest-cov']
extra_packages = {
    'testing': ['tox']
}

setup(
    name='Code Katas',
    description="""Auto generate thank you letters""",
    version='0.1',
    author='Carlos Cadena',
    author_email="cs.cadena@gmail.com",
    license="MIT",
    py_modules=['highest_profit'],
    package_dir={'': 'src'},
    install_requires=dependencies,
    extras_require=extra_packages,
    entry_points={'console_scripts': ['highest_profit = highest_profit:main']}
      )
