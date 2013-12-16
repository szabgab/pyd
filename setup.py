from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='pydigger',
      version='0.1',
      description='Diggin Py',
      long_description=readme(),
      url='http://github.com/szabgab/pyd',
      author='Gabor Szabo',
      author_email='gabor@szabgab.com',
      license='MIT',
      packages=['pydigger'],
      requires=[
          'lawyerup',
      ],
      zip_safe=False)

