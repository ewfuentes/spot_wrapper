from setuptools import find_packages, setup

setup(
    name="spot_wrapper",
    version="1.0.0",
    description="Wrapper for Boston Dynamics Spot SDK",
    packages=find_packages(include=["spot_wrapper*"]),
    install_requires=[
        "bosdyn-client==3.3.2",
        "bosdyn-api==3.3.2",
        "bosdyn-mission==3.3.2",
        "bosdyn-core==3.3.2",
        "bosdyn-choreography-client==3.3.2",
        "bosdyn-choreography-protos==3.3.2",
        "grpcio",
        "inflection",
        "pytest"
    ],
)
