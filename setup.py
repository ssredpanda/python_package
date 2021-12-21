from setuptools import setup, find_packages

setup(
    name="mypackage",
    version="1.2",
    description="Pythonのディレクトリ構成のテスト用",
    author="Firstname Lastname",
    author_email="aaa@example.com",
    url="https://github.com/ssredpanda/python_package",
    packages=find_packages(),
    entry_points="""
      [console_scripts]
      mypackage = mypackage.cli:execute
    """,
    install_requires=open("requirements.txt").read().splitlines(),
)
