#!/bin/bash

# For requirements.txt
echo "Exporting requirements.txt"
poetry export --without-hashes --format=requirements.txt > requirements.txt

# For requirements-dev.txt
echo "Exporting requirements-dev.txt"
poetry export --without-hashes --with dev --format=requirements.txt > requirements-dev.txt