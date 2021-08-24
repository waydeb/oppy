from setuptools import setup


ver = '1.0.1'

with open('README.md', 'r') as f:
  long_desc = f.read()

setup(
  name = 'op.py',
  packages = ['oppy'],
  version = ver,
  license='MIT',
  description = 'A wrapper made for the osu! v2 API.',
  long_description= long_desc,
  long_description_content_type = 'text/markdown',
  author = 'Wayde B',
  author_email = 'wayde@alphaxdev.xyz',
  url = 'https://github.com/waydealphax/oppy',
  keywords = ['osuapi', 'osu', 'osuapiv2'],
  install_requires=[
          'aiohttp',
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.9',
  ],
)
