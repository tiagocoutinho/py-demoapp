import gevent
# just to force checking the dependency
import flask

def run():
    print('DemoApp webserver up and running!')
    for i in range(10000):
        print('waiting for {}s'.format(i), end='\r', flush=True)
        gevent.sleep(1)


def main():
    try:
        run()
    except KeyboardInterrupt:
        print('Ctrl-C pressed. Bailing out!')
        
