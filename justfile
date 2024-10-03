# just --working-directory . --justfile test/justfile

default: lint typecheck

lint:
  pylint src

typecheck:
  mypy src
