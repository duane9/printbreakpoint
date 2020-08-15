============================
PrintBreakpoint
============================

Install with pip:

::

    pip install printbreakpoint

Update the PYTHONBREAKPOINT environment variable (available starting in Python
3.7):

::

    export PYTHONBREAKPOINT=printbreakpoint.pb

Now when you add a breakpoint() to your code, it will show the output from pb.

.. code:: python

    def reverse_str(text):
        breakpoint()
        return text[::-1]

Prints

::

    pb | some_file.py:3 in reverse_str

Any data you pass to the breakpoint() will be added to the output.

Change the environment variable back to the default when you're ready to
continue using pdb.

::

    export PYTHONBREAKPOINT=
    
