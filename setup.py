from setuptools import setup, find_packages
import os



try:
    import pypandoc
    read_md = lambda f: pypandoc.convert(f, 'rst')
except ImportError:
    print('Warning: pypandoc module not found.')
    read_md = lambda f: open(f, 'r').read()


# PyDAIR version
with open(os.path.join(os.path.dirname(__file__), 'PyDAIR', '__init__.py')) as fh:
    for buf in fh:
        if buf.startswith('__version__'):
            exec(buf)
            break


setup(
    name        = 'PyDAIR',
    version     = __version__,
    description = 'Python library for diversity analysis of immune repertoire.',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
    ],
    keywords     = 'blast, bioinformatics',
    author       = 'Jianqiang Sun, Xi Fu',
    author_email = 'wukong@bi.a.u-tokyo.ac.jp',
    url          = 'https://github.com/jqsunac/PyDAIR',
    license      = 'GNU',
    packages     = find_packages('PyDAIR', exclude=['examples', 'tests']),
    package_dir  = {'': 'PyDAIR'},
    package_data = {'': ['PyDAIR/templates/*html']},
    scripts      = ['PyDAIR/bin/pydair-parseseq',
                    'PyDAIR/bin/pydair-analysis'],
    test_suite   = 'test',
    include_package_data = True,
    zip_safe = True,
    long_description = read_md('README.md'),
    install_requires = ['matplotlib>=1.4', 'pandas', 'biopython'],
)




