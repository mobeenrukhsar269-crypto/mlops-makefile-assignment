# =========================
# MLOps Makefile - Titanic Pipeline
# =========================

PYTHON := python
VENV := venv
REQ := requirements.txt

.PHONY: help setup download-data preprocess features train predict evaluate all clean

help:
	@echo "Available commands:"
	@echo "  make setup           -> Install dependencies"
	@echo "  make download-data   -> Download dataset"
	@echo "  make preprocess      -> Clean and prepare dataset"
	@echo "  make features        -> Feature engineering"
	@echo "  make train           -> Train model"
	@echo "  make predict         -> Generate predictions"
	@echo "  make evaluate        -> Compute evaluation metrics"
	@echo "  make all             -> Run full pipeline"
	@echo "  make clean           -> Remove generated files"

# -------------------------
# Environment setup
# -------------------------
setup:
	$(PYTHON) -m venv $(VENV)
	$(VENV)/Scripts/pip install --upgrade pip
	$(VENV)/Scripts/pip install -r $(REQ)

# -------------------------
# Download raw dataset
# -------------------------
download-data:
	$(VENV)/Scripts/python src/download_data.py

# -------------------------
# Data preprocessing
# -------------------------
preprocess:
	$(VENV)/Scripts/python src/preprocess.py

# -------------------------
# Feature engineering
# -------------------------
features:
	$(VENV)/Scripts/python src/features.py

# -------------------------
# Train ML model
# -------------------------
train:
	$(VENV)/Scripts/python src/train.py

# -------------------------
# Prediction
# -------------------------
predict:
	$(VENV)/Scripts/python src/predict.py

# -------------------------
# Evaluation
# -------------------------
evaluate:
	$(VENV)/Scripts/python src/evaluate.py

# -------------------------
# Run entire pipeline
# -------------------------
all: download-data preprocess features train predict evaluate

# -------------------------
# Cleanup
# -------------------------
clean:
	rm -rf $(VENV) data/processed features results models logs/
