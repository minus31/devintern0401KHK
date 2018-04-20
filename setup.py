from setuptools import setup, find_packages

setup_requires = [
    ]

install_requires = [
    'pandas==0.22.0',
    'numpy==1.14.2',
    ]

dependency_links = [
    ]

setup(
    name='devintern1804',
    version='0.1',
    description='devintern1804',
    author='Hyunkyu KIM',
    author_email='donotgetgreed@gmail.com',
    packages=["Dev"],
    include_package_data=False,
    install_requires=install_requires,
    setup_requires=setup_requires,
    dependency_links=dependency_links,
    # scripts=['manage.py'],
    entry_points={
        'console_scripts': [
            ],
        "egg_info.writers": [
                "foo_bar.txt = setuptools.command.egg_info:write_arg",
            ],
        },
    )
