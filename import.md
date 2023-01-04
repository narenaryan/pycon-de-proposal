## Types of imports
* Module imports
* Package imports

## Types of import in programs
* `import` keyword
* importlib.import_module() function
* __import__() function

* Calling __import__ directly can cause side-effects
* `import` keyword calls `__import__()` function with correct args
* importlib.import_module() uses a different implementation

## Pycache files
* When a Python source file is imported for the first time, a __pycache__ directory will be created in the package directory, if one does not already exist.
* Pycache files use a magic tag format which appends Python version as a number at the end of file name.

```python
import importlib
importlib.util.source_from_cache("project/__pycache__/strutil.cpython-310.pyc")
importlib.util.cache_from_source("project/strutil.py")
```
