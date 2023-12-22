from setuptools import setup, find_packages

excluded_packages = ["docs", "tests", "tests.*"]

setup(
    name='mitlab_aiml_tools',
    version='0.1.0',
    author="MITLAB",
    license='MIT License',
    url='https://github.com/mitlab-6g-team/mitlab_aiml_tools.git',
    author_email="mitlab6g.project@gmail.com",
    packages=find_packages(exclude=excluded_packages),
    description='MITLab AI/ML tools for pipeline development.',
    install_requires=['requests', 'python-dotenv'],
    python_requires='>=3'
)
