# mathviz
A python package for examining mathematics equation embeddings.

Documentation: https://samghelms.github.io/mathviz/

This has a sister repository that contains the javascript used to develop the visualizations:

https://github.com/samghelms/mathviz-js-components

# Instructions

Install dependencies with pip and then run the jupyter notebook for an example of how to use the table tool.

`pip install mathviz_hopper`

## Running examples

git clone this repository, navigate to the repository, then:

1. `cd examples`
2. `pip install -r requirements.txt`
3. `jupyter notebook`
4. Open the `example.ipynb` file and run the example code. Make sure your kernel has the package in it (you might need to switch kernels from `env` to `python 2`)

## Running on a server

TODO: add a public address feature to table and server

## Building the docs

### for local use
Run `make html` in the `docs` directory

### for github pages
Run `make gh-pages` in the root directory of the repository

## distributing 

Run `python setup.py sdist`
and then
`twine upload dist/<dist>`
	