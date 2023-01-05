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


 The `__import__()` won't work for modules in sub-directories. But `import` keyword and `import_module()`do.

In order to properly import module in a subdirectory, one should make subdirectory as a package. Just place a `__init__.py` file in there.

Whenever you specify a relatife import (Ex: from .foo import bar), you need a package. Otherwise, modules just work fine.

Module vs Package: They are different units of packaging code. Modules for namespacing code. But packages for grouping related modules. Use correct unit for given use-case.