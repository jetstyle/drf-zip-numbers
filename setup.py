from distutils.core import setup


classifiers = [
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
]

setup(
    name='drf-zip-numbers',
    version='0.0.1',
    description='Parser for zipped strings.',
    author='Ivan Zverev',
    author_email='ffsavft@mail.ru',
    packages=['drf_zip_numbers'],
    url='https://github.com/elivin/drf-zip-numbers',
    license='MIT',
    keywords='django rest fields',
    long_description='Parser for zipped strings.',
    classifiers=classifiers,
)
