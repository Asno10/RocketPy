Analysis
========

.. toctree::
    :maxdepth: 1
    :caption: Contents:

    ../notebooks/utilities_usage.ipynb

Ballast Optimization
--------------------

Two helper functions are available for tuning ballast mass.

``optimize_ballast_weights`` runs a series of deterministic flights and returns
the number of ballast weights that best matches a target apogee.
``optimize_ballast_weights_mode`` performs a Monte Carlo simulation for each
candidate configuration and selects the option whose apogee distribution has a
mode closest to the desired altitude.

Example::

    n, apogee = optimize_ballast_weights(
        flight,
        mass_each=0.25,
        position=0.2,
        target_apogee=1000,
    )

Monte Carlo Plots
-----------------

The :class:`rocketpy.simulation.MonteCarlo` plots object now offers an
``apogee_distribution`` method. It draws a histogram of simulated apogees,
overlays a Gaussian fit and marks the distribution mode.

.. code-block:: python

    monte_carlo.plots.apogee_distribution()
