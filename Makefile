# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SPHINXPROJ    = MathvizHopper
SOURCEDIR     = docs/source
BUILDDIR      = docs/build
GH_PAGES_SOURCES = docs/

gh-pages:
	sphinx-apidoc -f -o docs/source/ mathviz_hopper/
	git checkout gh-pages
	rm -rf *
	git rm -rf *
	touch .nojekyll
	git checkout dev $(GH_PAGES_SOURCES)
	cd docs; make html
	mv -fv docs/build/html/* .
	git add .
	git commit -m "Generated gh-pages for `git log dev -1 --pretty=short --abbrev-commit`" && git push origin gh-pages ; git checkout dev

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)