**PrintBreakpoint**

Use ``breakpoint()`` to print out filename, line number, and data. For Python 3.7+

Install ``printbreakpoint`` with pip.

::

    pip install printbreakpoint

Update the ``PYTHONBREAKPOINT`` environment variable (available starting in Python
3.7).

::

    export PYTHONBREAKPOINT=printbreakpoint.pb

Now when you add ``breakpoint()`` to your code, it will show the output from
``printbreakpoint``.

.. code:: python

    def some_function(a):
        breakpoint()
        return a

Prints

::

    pb | some_file.py:3 in some_function

Any data you pass to the ``breakpoint()`` will be added to the output.

Change the environment variable back to the default when you're ready to
continue using ``pdb``.

::

    export PYTHONBREAKPOINT=

