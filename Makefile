# Synchronize dependencies
sync:	        
	@echo "Synchronize dependencies"
	uv sync --extra docs --extra dev

# Generate html documentation
docgen: 
	sync
	@echo "Cleaning old API documentation"
	rm -rf docs/api docs/_build
	@echo "Generating API documentation from source code"
	sphinx-apidoc -f -o docs/api src --separate --module-first --no-toc
	@echo "Generate html documentation"
	sphinx-build -b html docs docs/_build/html

# Create symbolic link for README.md in docs/
link_readme:
	@echo "Copy README.md to docs/"
	ln -s ../README.md docs/README.md