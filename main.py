#coding:utf-8

# ************ METHODS DEFINITON ************

# This method checks that sequences are only made of ATCGs
def check_sequence(sequence):
    sequence = sequence.upper()
    sequence = sequence.replace("A", "")
    sequence = sequence.replace("T", "")
    sequence = sequence.replace("C", "")
    sequence = sequence.replace("G", "")
    if not sequence:
        return True
    else:
        return False

# This method converts a sequence into its reverse complement
def reverse_complement(sequence):
    sequence = sequence.upper()
    sequence = sequence.replace("A","t",-1)
    sequence = sequence.replace("T","a",-1)
    sequence = sequence.replace("C","g",-1)
    sequence = sequence.replace("G","c",-1)
    sequence = sequence.upper()
    sequence = sequence[::-1]
    return(sequence)

# This method returns the list of matches between the primer and the target
def find_matches(primer_sequence, target_sequence):
    matches = []
    i = 0
    while i <= len(target_sequence)-len(primer_sequence):
        if target_sequence[i:i+len(primer_sequence)] in primer_sequence:
            matches.append(i + 1)
            i += 1
        else:
            i += 1
    return matches




# ************ MAIN PROGRAM ************

# Input sequences
target = "AGAAAGGGGAAAAGGAGGGC"
primerF = "AGA"
primerR = "GCC"

# Check that the sequences are in the right format
seqcheck = check_sequence(target)
if seqcheck == False:
    print("\nTarget sequence must only contain A, T, C and G")
    print("\n*******Program stopped*******")
    exit()
seqcheck = check_sequence(primerF)
if seqcheck == False:
    print("\nForward primer sequence must only contain A, T, C and G")
    print("\n*******Program stopped*******")
    exit()
seqcheck = check_sequence(primerR)
if seqcheck == False:
    print("\nReverse primer sequence must only contain A, T, C and G")
    print("\n*******Program stopped*******")
    exit()

# Create reverse complements of the reverse primer
primerR_RC = reverse_complement(primerR)

# Search for matches (the method returns a list for each primer)
matches_primerF = find_matches(primerF, target)
matches_primerR_RC = find_matches(primerR_RC, target)

# Count the number of matches for each primer
nb_matches_primerF = len(matches_primerF)
nb_matches_primerR_RC = len(matches_primerR_RC)

# Print the result if design is OK, or give details on the problems (no match or more than 1 match)
if nb_matches_primerF == 1 and nb_matches_primerR_RC == 1:
    print("\nDesign is correct.\nAmplicon size = {} bp (position {} to {} of the target sequence).".format(matches_primerR_RC[0] + len(primerR_RC) - matches_primerF[0], matches_primerF[0], matches_primerR_RC[0] + len(primerR_RC) - 1))
    print("Amplified sequence : {}".format(target[matches_primerF[0] - 1 : matches_primerR_RC[0] + len(primerR_RC) - 1]))
else:
    print("\nDesign is incorrect.")
    if nb_matches_primerF == 0: print("Forward primer does not match target.")
    if nb_matches_primerF == 1: print("Forward primer matches target at one site on position {}.".format(matches_primerF))
    if nb_matches_primerF > 1:
        print("Forward primer matches target at {} different sites on positions {}.".format(nb_matches_primerF, matches_primerF))
    if nb_matches_primerR_RC == 0: print("Reverse primer does not match target.")
    if nb_matches_primerR_RC == 1: print("Reverse primer matches target at one site on position {}.".format(matches_primerR_RC))
    if nb_matches_primerR_RC > 1:
        print("Reverse primer matches target at {} different sites on positions {}.".format(nb_matches_primerR_RC, matches_primerR_RC))
