import pytest

# List of dependencies
dependencies = [
    "colored_logging",
    "matplotlib",
    "numpy",
    "rasters",
    "dateutil",
    "shapely"
]

# Generate individual test functions for each dependency
@pytest.mark.parametrize("dependency", dependencies)
def test_dependency_import(dependency):
    __import__(dependency)
