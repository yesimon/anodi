from setuptools import setup

requirements = {
    'install': [
        'distribute>=0.6.34',
        'backports.inspect>=0.0.2',
        ],
    'extras': {
        'docs': [
            'sphinx>=1.1',
            'agoraplex.themes.sphinx>=0.1.3',
            ],
        'tests': [
            'nose>=1.2.1',
            'coverage>=3.6',
            'pinocchio>=0.3.1',
            'xtraceback>=0.3.3',
            ],
        },
    }

# write requirements for Travis and ReadTheDocs to use...
with open("reqs/travis.txt", "w") as travis:
    travis.write('\n'.join(requirements['extras']['tests']) + '\n')

with open("reqs/rtfd.txt", "w") as rtfd:
    rtfd.write('\n'.join(requirements['extras']['docs']) + '\n')

setup(
    name='anodi',
    version='0.0.2',
    author='Tripp Lilley',
    author_email='tripplilley@gmail.com',
    packages=['anodi'],
    namespace_packages=[],
    url='https://github.com/agoraplex/anodi',
    license='BSD',
    description='A decorator-based backport of PEP-3107 function annotations to Python 2.7, and related tools.',
    long_description=open('README.rst').read(),

    install_requires=requirements.get('install', None),
    tests_require=requirements.get('extras', {}).get('tests', None),
    extras_require=requirements.get('extras', None),

    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Topic :: Documentation",
        "Topic :: Software Development :: Documentation",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ]
)
