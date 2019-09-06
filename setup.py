from setuptools import setup

setup(name='minecraftControl',
      author = 'Andy Lamperski',
      description = 'Controllable Vehicles in Minecraft Environment',
      url = 'https://github.com/AndyLamperski/minecraftControl',
      author_email = 'alampers@umn.edu',
      license = 'MIT',
      packages = ['minecraftControl'],
      install_requires = [
          'jupyter',
          'numpy',
          'scipy',
          'pyglet',
          'matplotlib',
      ]
      )

