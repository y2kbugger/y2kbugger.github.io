VENV_BIN?=$(CURDIR)/.venv/bin
PY?=$(VENV_BIN)/python
PELICAN?=$(VENV_BIN)/pelican
GHP_IMPORT?=$(VENV_BIN)/ghp-import

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
PUBLISHCONF=$(BASEDIR)/publishconf.py

GITHUB_PAGES_BRANCH=master

livereload:
	$(PY) devserver.py

publish:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS)

github: publish
	$(GHP_IMPORT) --no-jekyll -m"$$(git log -1 --pretty='%h %s')" -b $(GITHUB_PAGES_BRANCH) $(OUTPUTDIR)
	git push origin $(GITHUB_PAGES_BRANCH)
	git push origin write

.PHONY: livereload publish github
