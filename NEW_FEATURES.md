# New Features

## Altitude-based Drag Curves

RocketPy now accepts drag coefficient tables with Mach number and altitude columns. The `Rocket` initializer automatically detects the number of inputs and sets the proper labels. When altitude information is present, drag coefficient evaluation inside `Flight` passes both Mach number and altitude to the drag functions.

```python
rocket = Rocket(
    ...,  # radius, mass, inertia, etc.
    power_off_drag="off_drag.csv",
    power_on_drag="on_drag.csv",
)
```

`off_drag.csv` and `on_drag.csv` may contain either two columns (`Mach`, `Cd`) or three columns (`Mach`, `Altitude`, `Cd`).

`rocket.plots.drag_curves()` will show a 3‑D surface of Mach, altitude and coefficient whenever altitude data is provided.

## Configurable Ballast Weights

The new `Ballast` class allows installing removable weights. Use `Rocket.add_ballast` to specify the mass of each weight, the number of installed weights and their position along the rocket axis.

```python
calisto.add_ballast(mass_each=0.25, number=4, position=0.20)
```

To tune the amount of ballast you can call:

```python
n, apogee = optimize_ballast_weights(flight, mass_each=0.25, position=0.20, target_apogee=1000)
```

or

```python
n, mode = optimize_ballast_weights_mode(
    flight,
    mass_each=0.25,
    position=0.20,
    target_apogee=1000,
    simulations=50,
)
```

The latter uses Monte Carlo simulations and selects the configuration whose apogee distribution has a mode closest to the target altitude.

## Monte Carlo Apogee Plot

`MonteCarlo.plots.apogee_distribution()` draws a histogram of simulated apogees, overlays a Gaussian fit and marks the mode.

```python
mc = MonteCarlo("example", s_env, s_rocket, s_flight)
mc.simulate(number_of_simulations=50)
mc.plots.apogee_distribution()
```

These additions extend RocketPy's ability to model altitude-dependent drag, optimize ballast mass and visualize stochastic results.
