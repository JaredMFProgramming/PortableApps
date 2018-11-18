splash = '''Piskel Portable v0.14.0 by Julian Descottes

Powered by JPAL, by Jared "M.F." Newsom'''

import time, sys, os

if __name__ == '__main__':
    print(splash)
    print('\nLoading...')
    for i in range(100+1):
        time.sleep(0.02)
        sys.stdout.write(('='*i)+(''*(100-i))+("\r [ %d"%i+"% ] "))
        sys.stdout.flush()
    sys.stdout.write('\n')
    print('Ready!')
    os.system(r'App\Piskel\Piskel.exe')
