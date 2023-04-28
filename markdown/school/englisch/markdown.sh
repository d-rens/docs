#!/bin/bash

# Combine all markdown files into a single file
cat *.md > combined.md

# Convert combined markdown file to PDF using Pandoc
pandoc combined.md -o combined.pdf

# Remove the combined markdown file
rm combined.md
