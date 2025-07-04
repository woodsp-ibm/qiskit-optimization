:orphan:

###############
Getting started
###############

Installation
============

Qiskit Optimization depends on Qiskit, which has its own
`installation instructions <https://quantum.cloud.ibm.com/docs/guides/install-qiskit>`__ detailing the
installation options for Qiskit and its supported environments/platforms. You should refer to
that first. Then the information here can be followed which focuses on the additional installation
specific to Qiskit Optimization.

Qiskit Optimization has some functions that have been made optional where the dependent code and/or
support program(s) are not (or cannot be) installed by default. Those are IBM CPLEX, CVXPY and Matplotlib.
See :ref:`optional_installs` for more information.

.. tab-set::

    .. tab-item:: Start locally

        The simplest way to get started is to follow the `Qiskit installation instructions <https://quantum.cloud.ibm.com/docs/guides/install-qiskit>`__

        In your virtual environment where you installed Qiskit, also install ``qiskit-optimization``:

        .. code:: sh

            pip install qiskit-optimization

        .. note::

            As Qiskit Optimization depends on Qiskit, you can though simply install it into your
            environment, as above, and pip will automatically install a compatible version of Qiskit
            if one is not already installed.

    .. tab-item:: Install from source

       Installing Qiskit Optimization from source allows you to access the most recently
       updated version under development instead of using the version in the Python Package
       Index (PyPI) repository. This will give you the ability to inspect and extend
       the latest version of the Qiskit Optimization code more efficiently.

       Since Qiskit Optimization depends on Qiskit, and its latest changes may require new or changed
       features of Qiskit, you should first follow Qiskit's `"Install from source"` instructions
       `here <https://quantum.cloud.ibm.com/docs/start/install-qiskit-source>`__

       .. raw:: html

          <h2>Installing Qiskit Optimization from Source</h2>

       Using the same development environment that you installed Qiskit in you are ready to install
       Qiskit Optimization.

       1. Clone the Qiskit Optimization repository.

          .. code:: sh

             git clone https://github.com/qiskit-community/qiskit-optimization.git

       2. Cloning the repository creates a local folder called ``qiskit-optimization``.

          .. code:: sh

             cd qiskit-optimization

       3. If you want to run tests or linting checks, install the developer requirements.

          .. code:: sh

             pip install -r requirements-dev.txt

       4. Install ``qiskit-optimization``.

          .. code:: sh

             pip install .

       If you want to install it in editable mode, meaning that code changes to the
       project don't require a reinstall to be applied, you can do this with:

       .. code:: sh

          pip install -e .


.. _optional_installs:

Optional installs
=================

* **IBM CPLEX** may be installed using ``pip install 'qiskit-optimization[cplex]'`` to enable the reading of `LP` files and the usage of
  the `CplexOptimizer`, wrapper for ``cplex.Cplex``. CPLEX is a separate package and its support of Python versions is independent of Qiskit Optimization, where this CPLEX command will have no effect if there is no compatible version of CPLEX available (yet).

* **CVXPY** may be installed using the command ``pip install 'qiskit-optimization[cvx]'``.
  CVXPY being installed will enable the usage of the Goemans-Williamson algorithm as an optimizer `GoemansWilliamsonOptimizer`.

* **Matplotlib** may be installed using the command ``pip install 'qiskit-optimization[matplotlib]'``.
  Matplotlib being installed will enable the usage of the `draw` method in the graph optimization application classes.

* **Gurobipy** may be installed using the command ``pip install 'qiskit-optimization[gurobi]'``.
  Gurobipy being installed will enable the usage of the `GurobiOptimizer`.

----

Ready to get going?...
======================

.. raw:: html

   <div class="tutorials-callout-container">
      <div class="row">

.. qiskit-call-to-action-item::
   :description: Find out about Qiskit Optimization.
   :header: Dive into the tutorials
   :button_link:  ./tutorials/index.html
   :button_text: Qiskit Optimization tutorials

.. raw:: html

      </div>
   </div>


.. Hiding - Indices and tables
   :ref:`genindex`
   :ref:`modindex`
   :ref:`search`
