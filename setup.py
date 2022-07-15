import setuptools

f = open("README.md", "r")
long_description = f.read()
f.close()

setuptools.setup(
  name="frases",
  packages=["frases"],
  version="0.1.2",
  author="Luqaska",
  description="API de frases",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://frases.atico.ga/api",
  project_urls={
    "Changelog": "https://github.com/Luqaska/frases.py/releases",
    "Bug Tracker": "https://github.com/Luqaska/frases.py/issues",
    "Source Code": "https://github.com/Luqaska/frases.py"
  },
  requires=["requests"],
  keywords=["API", "frases"]
)