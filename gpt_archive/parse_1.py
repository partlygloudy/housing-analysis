import sys

# Open the input and output files
with open(sys.argv[1], "r") as infile, open(sys.argv[2], "w") as outfile:
    for line in infile:
        if not line.startswith(','):
            line = line.replace(',', '\n,', 1)
        outfile.write(line)