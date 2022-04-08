#!/usr/bin/env bash

set -e

gunicorn -b 0.0.0.0:1233 issue.composites.issue_api:app --reload