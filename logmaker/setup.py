from setuptools import setup, find_packages

setup(name='logmaker', # 패키지 명

version='1.0.0',

description='create log files ',

author='Resourcebox',

author_email='neivekim76@gmail.com',

url='https://github.com/resource-box/logmaker',

license='MIT',

py_modules=['logmaker'],

python_requires='>=3',

install_requires=[], # 패키지 사용을 위해 필요한 추가 설치 패키지

packages=['logmaker'] # 패키지가 들어있는 폴더들

)