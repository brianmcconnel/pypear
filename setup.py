from setuptools import setup, find_packages

with open('requirements.txt') as f:
   requirements = [line.strip() for line in f]

setup(name='pypear',
      version='0.1.0',
      author='Brian McConnel',
      author_email='brianmcconnel@gmail.com',
      url='https://github.com/brianmcconnel/pypear',
      description='Adequate terminal based python development.',
      license='MIT',
      packages=find_packages(),
      package_data={"pypear": ["vim-bundles/plugins.zip"]},
      entry_points={'console_scripts': ['pypear = pypear.main:main']},
      classifiers=("Programming Language :: Python :: 3",
                   "License :: OSI Approved :: MIT License",
                   "Operating System :: OS Independent",),
      keywords='python tmux vim pypear',
      requires=requirements,
      zip_safe=True)
