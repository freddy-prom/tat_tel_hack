from pkg_resources import parse_requirements
from setuptools import setup, find_packages


def load_requirements(f_name: str) -> list:
    requirements = []
    with open(f_name, 'r') as fp:
        for req in parse_requirements(fp.read()):
            extras = '[{}]'.format(','.join(req.extras)) if req.extras else ''
            requirements.append(
                '{}{}{}'.format(req.name, extras, req.specifier)
            )
    return requirements


setup(
    name="shop",
    platforms="all",
    packages=find_packages(exclude=["tests"]),
    install_requires=load_requirements('requirements.txt'),
    entry_points={
        'console_scripts': [
            'shop-api = app.__init__:main',
            'shop-db = app.db.main:main'
        ]
    },

    include_package_data=True
)
