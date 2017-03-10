from setuptools import setup

setup(name='kilgore',
      description='Kilgore (as in trout) - tabular data stream manipulation',
      version='0.1',
      author='Jake Kara',
      author_email='jake@jakekara.com',
      license='GPL3',
      install_requires=['pandas==0.19.2'],
      packages=['kilgoretrout','kilgoretrout/procedures'],
      scripts=['bin/kilgore'])
      
    
    
