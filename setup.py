
from distutils.core import setup
setup(
  name = 'gimpysolver',         # How you named your package folder (MyLib)
  packages = ['gimpysolver'],   # Chose the same as "name"
  version = '0.0.1',      # Start with a small number and increase it with every change you make
  license='GPL',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'a small package to solve Gimpy Captcha with 92 porcent of accuracy.',   # Give a short description about your library
  author = 'César Cortez',                   # Type in your name
  author_email = 'cc@digitaliatec.com',      # Type in your E-Mail
  url = 'https://github.com/user/reponame',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['CAPTCHA', 'CAPTCHASOLVER', 'GIMPY','GIMPYSOLVER','SOLVER'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'keras',
          'io',
	   'PIL',
	'opencv-python',
'importlib',
'io'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)