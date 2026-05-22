from setuptools import setup, find_packages

setup(
    name="erpnext_core",
    version="0.0.0",
    description="ERPNext Core — Accounts, Buying, Selling, Stock, Assets. Manufacturing and Quality Management removed.",
    packages=["erpnext"],
    include_package_data=True,
    install_requires=[
        "Unidecode~=1.4.0",
        "barcodenumber~=0.5.0",
        "rapidfuzz~=3.14.3",
        "holidays~=0.87",
        "googlemaps~=4.10.0",
        "plaid-python~=7.2.1",
        "python-youtube~=0.9.8",
        "pypng~=0.20220715.0",
        "mt-940>=4.26.0",
    ],
    python_requires=">=3.10",
    # Use the same metadata as pyproject.toml where appropriate
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/balaji-001-gif/erpnext_core",
    author="Your Org",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
