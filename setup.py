from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.readlines()

# with open('README.md') as f:
#     long_description = f.readlines()

setup(name='pypear',
      version='0.1.0',
      author='Brian McConnel',
      author_email='brianmcconnel@gmail.com',
      url='https://github.com/brianmcconnel/pypear',
      description='Adequate terminal based python development.',
      # long_description=long_description,
      # long_description_content_type ="text/markdown",
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      entry_points={'console_scripts': ['pypear = pypear.main:main']},
      classifiers=("Programming Language :: Python :: 3",
                   "License :: OSI Approved :: MIT License",
                   "Operating System :: OS Independent",),
      keywords='python tmux vim pypear',
      requirements=requirements,
      zip_safe=True)
