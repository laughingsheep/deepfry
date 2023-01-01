from setuptools import setup
with open('requirements.txt') as req:
  requirements = req.readlines()

with open('README.md') as read:
  readme = read.read()

setup(
  name='Deepfry',
  author='Jodo',
  author_email='deepfry@thejodo.com',
  url='https://github.com/laughingsheep/deepfry',
  version="1.1.0",
  packages=['Deepfry'],
  license='MIT',
  description='Deepfry images with ease',
  long_description=readme,
  long_description_content_type='text/markdown',
  install_requires=["Pillow==9.3.0"],
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'License :: OSI Approved :: MIT License',
    'Intended Audience :: Developers',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3',
    'Topic :: Multimedia :: Graphics :: Editors',    
    'Topic :: Internet',
    'Topic :: Software Development :: Libraries',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Utilities',
  ]
)