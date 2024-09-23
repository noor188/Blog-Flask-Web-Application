from setuptools import setup, find_packages

setup(
    name="microblog",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Flask",
        "flask-wtf",
        "flask-migrate",
        "Flask-SQLAlchemy",
        "flask-login",
        "email-validator"
    ],
)