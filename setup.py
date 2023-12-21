from setuptools import setup, find_packages

setup(
    name='mitlab_aiml_tools',
    version='0.1.0',
    author="MITLAB",
    author_email="mitlab6g.project@gmail.com",
    packages=find_packages(),
    install_requires=['requests', 'python-dotenv'],
    python_requires='>=3'
)
