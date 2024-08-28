# just --working-directory . --justfile test/justfile

default: lint typecheck

lint:
  pylint plover_steno_engine_hooks_logger

typecheck:
  mypy plover_steno_engine_hooks_logger

