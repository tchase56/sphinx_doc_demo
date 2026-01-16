# Synchronize dependencies
sync:	        
	@echo "Synchronize dependencies"
	uv sync --extra docs --extra dev

# Generate html documentation
docgen: 
	sync
	@echo "Cleaning old build"
	rm -rf docs/_build
	@echo "Generate html documentation with autodoc2"
	sphinx-build -b html docs docs/_build/html

# Create symbolic link for README.md in docs/
link_readme:
	@echo "Copy README.md to docs/"
	ln -s ../README.md docs/README.md