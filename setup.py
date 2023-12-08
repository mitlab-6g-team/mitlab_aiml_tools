from setuptools import setup, find_packages

setup(
    name='mitlab-aiml-pipeline-utils',
    version='0.1',
    author="MITLAB",
    author_email="mitlab6g.project@gmail.com",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=['requests', 'dotenv'],
    python_requires='>=3'
)
