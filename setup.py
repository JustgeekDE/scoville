#!/usr/bin/env python

from distutils.core import setup

setup(name='Scoville',
      version='0.0',
      description='A collection of helper scripts to unit test hardware',
      author='Philip Peter',
      author_email='philip.peter@justgeek.de',
      url='https://github.com/JustgeekDE/scoville',
      py_modules=['scoville/circuit', 'scoville/signal', 'scoville/spiceSimulator', 'scoville/arduinoTester',
                  'scoville/eagleSchematic', 'scoville/eagleBoard', 'scoville/genericNodeTransformations',
                  'scoville/schematicTransformations', 'scoville/boardTransformations'],
      )
