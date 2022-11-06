from distutils.core import setup
setup(
  name = 'XTLib',
  packages = ['XTLib'],
  version = '0.1',
  license='mit',
  description = "Xemulated's Library for XToolBox",
  author = 'Xemulated',
  author_email = 'xemulated@tuta.io',
  url = 'https://github.com/xemulat',
  download_url = 'https://github.com/xemulat/XTLib/archive/refs/tags/0.1.tar.gz',
  keywords = ['QOL', 'xemulated', 'downloader'],
  install_requires=['psutil', 'XeLib'],
  classifiers=[
    'Development Status :: 3 - Alpha',      # "3 - Alpha", "4 - Beta" or "5 - Production/Stable"
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.11',
    'Programming Language :: Python :: 3.10',
  ],
)