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
        	'ActuatorNode = test_bed.ActuatorNode:main'
        ],
    },
)
