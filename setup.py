from distutils.core import setup

setup(
    name='shapely2geojson',
    packages=['shapely2geojson'],
    version='0.1',
    license='MIT',
    description='This is a repo which contains code to convert shapely objects to geojson features',
    author='Ashish Dhiman',
    author_email='ashish.dhiman.nith@gmail.com',
    url='https://github.com/aashishd',
    download_url='https://github.com/aashishd/shapely2geojson/v_01.tar.gz',
    keywords=['shapely', 'geojson', 'conversion', 'shapely-to-geojson', 'convert', 'convert-shapely'],
    install_requires=[
        'Shapely',
    ],
    classifiers=[
        'Development Status :: 4 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
