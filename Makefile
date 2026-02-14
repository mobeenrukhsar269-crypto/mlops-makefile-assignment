# =========================
# MLOps Automation Makefile
# =========================

PYTHON := python
VENV := venv

.PHONY: help setup clean

help:
	@echo "Available commands:"
	@echo "  make setup    -> Create venv and install dependencies"
	@echo "  make clean    -> Remove venv and generated files"

setup:
	$(PYTHON) -m venv $(VENV)
	$(VENV)/Scripts/pip install --upgrade pip
	$(VENV)/Scripts/pip install -r requirements.txt

clean:
	rm -rf $(VENV)
