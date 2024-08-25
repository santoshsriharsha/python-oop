from importlib.util import spec_from_file_location, module_from_spec
import sys
import os
from dotenv import load_dotenv

load_dotenv()

module_path = os.getenv('PATH_TO_MODULE')

spec = spec_from_file_location('module', module_path)
module = module_from_spec(spec)
sys.modules['module'] = module
spec.loader.exec_module(module)

from module import NotPrivate, _Private
obj = NotPrivate('name1')
obj2 = _Private('name')
obj.display()
obj._display()
print(obj2)




