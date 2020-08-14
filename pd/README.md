# pd - Print debugging with Python 3 breakpoint()

Python 3 `breakpoint()` makes it easy to switch between print debugging and using
a debugger. Using `breakpoint()` by default allows you to access `pdb`, (The Python
Debugger)[https://docs.python.org/3/library/pdb.html]. By modifying the `PYTHONBREAKPOINT`
environment variable, you can also use `breakpoint()` with `pd` for print debugging.

```
pip install pd
```

In your shell:

```
export PYTHONBREAKPOINT=pd.pd
```

Or in Python:

```python
import os
os.environ['PYTHONBREAKPOINT'] = 'pd.pd'
```

Now when you add a `breakpoint()` to your code, it will show the output from `pd`.

```python

def some_function():
    breakpoint()
    return None
```

Prints

```
pd | some_file.py:2 in some_function()
```

You can also print out data:
```python

def some_function():
    breakpoint('yep')
    return None
```

Prints

```
pd | some_file.py:2 in some_function() | yep
```

Now if you switch the environment variable back to the default and rerun the code,
it will use `pdb` as usual.

```python
# Switch back to pdb
import os
os.environ['PYTHONBREAKPOINT'] = ''
```

`pd` is an intentionally simple function with no dependencies. You can easily copy
and paste it into your Django local settings for example, making it easy to use in
any environment.

