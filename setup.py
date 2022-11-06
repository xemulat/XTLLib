from distutils.core import setup
setup(
  name = 'XTLLib',
  packages = ['XTLLib'],
  version = '0.4',
  license='mit',
  description = "Xemulated's Library for XToolBox",
  long_description= "Basic library to save space for XToolBox",
  author = 'Xemulated',
  author_email = 'xemulated@tuta.io',
  url = 'https://github.com/xemulat',
  download_url = 'https://github.com/xemulat/XTLLib/archive/refs/tags/0.4.tar.gz',
  keywords = ['QOL', 'xemulated', 'downloader'],
  install_requires=['psutil', 'XeLib', 'colorama'],
  classifiers=[
    'Development Status :: 3 - Alpha',      # "3 - Alpha", "4 - Beta" or "5 - Production/Stable"
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.11',
    'Programming Language :: Python :: 3.10',
  ],
)