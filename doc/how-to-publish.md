How to publish to PyPI
=========================


1.
Create a Source Distribution:
```
python setup.py sdist
```

2.
Upload to test pypi
```
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```

3.
test using test pypi,
install from test pypi
```
pip install --index-url https://test.pypi.org/simple/ hypnolog
```

4.
Upload to real PyPI
```
twine upload dist/*
```
