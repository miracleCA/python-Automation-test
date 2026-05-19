#!/bin/bash

export PYTHONPATH=$(pwd)

echo "🚀 Starting API..."

docker-compose up -d

echo "🧪 Running tests..."

pytest -v \
  --html=reports/report.html \
  --self-contained-html \
  --junitxml=reports/junit.xml

echo "🧹 Stopping API..."

docker-compose down