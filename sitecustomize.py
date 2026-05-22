import sys
import importlib

# Ensure that any import of erpnext.manufacturing resolves to the shim package.
try:
    importlib.import_module('erpnext.manufacturing')
except ModuleNotFoundError:
    sys.modules['erpnext.manufacturing'] = importlib.import_module('erpnext._shims.manufacturing')
