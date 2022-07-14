import setuptools

f = open("README.md", "r")
long_description = f.read()
f.close()

setuptools.setup(
  name="frases",
  packages=["frases"],
  version="0.1.0",
  author="Luqaska",
  description="API de frases",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/Luqaska/frases.py",
  project_urls={
    "Bug Tracker": "https://github.com/Luqaska/frases.py/issues"
  },
  requires=["requests"],
  keywords=["API", "frases"]
)