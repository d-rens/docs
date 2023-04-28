# Set the input and output file names
INFILES := $(wildcard *.md)
OUTFILE := output.pdf

# Define the Pandoc command
PANDOC := pandoc
PANDOC_OPTS := --toc --pdf-engine=pdflatex

all: $(OUTFILE)

$(OUTFILE): $(INFILES)
    cat $^ | $(PANDOC) $(PANDOC_OPTS) -o $@

.PHONY: clean

clean:
    rm -f $(OUTFILE)
