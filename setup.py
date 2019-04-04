from setuptools import setup, find_packages

setup(
    name='demoapp',
    version='7.0.2',
    author='Tiago Coutinho',
    author_email='coutinhotiago@gmail.com',
    description='A demo app to test setuptools entry points',
    packages=find_packages(),
    package_data={'demoapp.ws': ['public/*',
                                 'public/static/css/*',
                                 'public/static/js/*']},
    entry_points=dict(
        console_scripts=[
            'demoapp-ws = demoapp.ws:main [web]',
            'demoapp-cli = demoapp.cli:main [cli]'
        ]
    ),
    extras_require=dict(
        cli=['click'],
        web=['flask'],
        rpc=['zerorpc']
    ),
    install_requires=['gevent'])
