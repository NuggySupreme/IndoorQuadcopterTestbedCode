from setuptools import setup

package_name = 'test_bed'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='OSU',
    maintainer_email='caleb.goodart@okstate.edu',
    description='Controlers for Quadcopter Test Bed',
    license='osu',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
			'FanNode = test_bed.FanNode:main',
			'ActuatorNode = test_bed.ActuatorNode:main',
			'controllerActuator = test_bed.linear_actuator_controller:main',
			'controllerPowerSupply = test_bed.power_supply_controller:main',
			'testerPowerSupply = test_bed.power_supply_tester:main',
			'off = test_bed.power_supply_off:main',
			'controllerFans = test_bed.fan_controller:main',
        ],
    },
)
