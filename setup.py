from setuptools import setup, find_packages

setup(
    name='mitlab-aiml-tools',
    version='0.1',
    author="MITLAB",
    author_email="mitlab6g.project@gmail.com",
    packages=find_packages(),
    install_requires=['requests', 'python-dotenv'],
    python_requires='>=3'
)
