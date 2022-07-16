from optimal_route import main
import pytest  # noqa


def test_main(capfd):
    argv = ["-i", "tests/test_cities2.json"]
    main(argv)
    out, err = capfd.readouterr()

    assert (
        out
        == "The optimal order to visit the cities is:\n1. Brno"
        + " - 0 meters\n2. Jihlava - 77736 meters\n3. Beroun - 125733"
        + " meters\n4. Prague - 28421 meters\n5. Hradec Kralove - 101330 meters\n6."
        + " Brno - 125455 meters\n\nThe total distance is: 458675 meters\n"
    )
