# cs466finalproject
string_generator.py was used to create the test input files. it generates sequences of the characters "A" "C" "T" "G" of varying lengths.

alignment.py is the implementation of fitting and local alignments. To run, execute:
python alignment.py "input_file.txt" "output_file.txt" "alignment type ('fitting' or 'local')

For example:
python alignment.py input_1.txt output_1_local.txt local

The input file must be in the following format:
match score
mismatch score
gap score
sequence 1
sequence 2

The final alignment and its alignment score is written to the specified output_file.txt in the format:
sequence 1 alignment
sequence 2 alignment
score
