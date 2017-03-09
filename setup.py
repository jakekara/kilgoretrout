from setuptools import setup

setup(name='tabstream',
      description='tabular stream manipulation',
      version='0.1',
      author='Jake Kara',
      author_email='jake@jakekara.com',
      license='GPL3',
      install_requires['pandas==0.19.2'],
      packages=['tabstream','tabstream/procedures'],
      scripts=['bin/ts'])
      
    
    
