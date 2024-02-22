from setuptools import setup

package_name = 'move_r'

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
    maintainer='elyas',
    maintainer_email='elyasabate21@gmail.com',
    description='Move Robot to Ethiopia cities',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'move_robot = move_r.move_robot:main',
        ],
},
)
