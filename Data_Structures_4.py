##% This section can be executed in isolation.
x = 1
print(x)

##% So can this section.
import time

while x < 10:
  time.sleep(0.5)
  print(x)
  x+=1

##% cProfile can be used inside a Python program.
import cProfile
import time

def foo():
    for i in range(5):
        time.sleep(0.5)
        print(i)

cProfile.run('foo()')

import time

def foo():
    for i in range(5):
        time.sleep(0.5)
        print(i)

if __name__ == '__main__':
    foo()

##% In CMD.
py -m pip install tqdm
pip install tqdm
pip freeze
pip uninstall tqdm

py -m venv virtual-test
virtual-test\Scripts\activate

##% Run Jupyter Notebook from CMD
jupyter notebook