# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SPHINXPROJ    = MathvizHopper
SOURCEDIR     = source
BUILDDIR      = build
GH_PAGES_SOURCES = source Makefile

gh-pages:
	git checkout gh-pages
	rm -rf build _sources _static
	git checkout dev $(GH_PAGES_SOURCES)
	git reset HEAD
	make html
	mv -fv build/html/* ./
	rm -rf $(GH_PAGES_SOURCES) build
	git add .
	git commit -m "Generated gh-pages for `git log dev -1 --pretty=short --abbrev-commit`" && git subtree push --prefix docs origin gh-pages ; git checkout dev

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)