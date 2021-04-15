import argparse
import csv
from pathlib import Path

if __name__ == "__main__":

	parser = argparse.ArgumentParser()
	parser.add_argument('filename')
	args = parser.parse_args()

	with open(args.filename, newline='') as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		next(reader) # Skip header
		
		with open(Path(args.filename).with_suffix('.txt'), 'w') as tasscriptfile:

			for linenumber, row in enumerate(reader, 1):

				if all(x == '' for x in row): continue

				buttonnames = [
					"KEY_A",
					"KEY_B",
					"KEY_X",
					"KEY_Y",
					"KEY_ZR",
					"KEY_ZL",
					"KEY_R",
					"KEY_L",
					"KEY_DRIGHT",
					"KEY_DLEFT",
					"KEY_DUP",
					"KEY_DDOWN",
					"KEY_PLUS",
					"KEY_MINUS",
					"KEY_LSTICK",
					"KEY_RSTICK"
				]

				# Readable python code
				leftstick = ';'.join([n if n else '0' for n in row[:2]])
				rightstick = ';'.join([n if n else '0' for n in row[2:4]])
				buttons = ';'.join([buttonnames[i] for i, x in enumerate(row[4:]) if x]) or 'NONE'

				tasscriptfile.write(f"{linenumber} {buttons} {leftstick} {rightstick}\n")