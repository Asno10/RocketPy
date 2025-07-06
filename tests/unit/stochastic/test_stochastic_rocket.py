from rocketpy.rocket.rocket import Rocket


def test_str(stochastic_calisto):
    assert isinstance(str(stochastic_calisto), str)


def test_create_object(stochastic_calisto):
    """Test create object method of StochasticRocket class.

    This test checks if the create_object method of the StochasticCalisto
    class creates a StochasticCalisto object from the randomly generated
    input arguments.

    Parameters
    ----------
    stochastic_calisto : StochasticCalisto
        StochasticCalisto object to be tested.

    Returns
    -------
    None
    """
    obj = stochastic_calisto.create_object()
    assert isinstance(obj, Rocket)


def test_validate_drag_table(simple_rocket_2d_drag):
    from rocketpy.stochastic import StochasticRocket

    table = [[0, 0, 0.5], [1, 1000, 0.4]]
    rocket = StochasticRocket(
        rocket=simple_rocket_2d_drag,
        power_on_drag=[table],
    )
    assert isinstance(rocket, StochasticRocket)
