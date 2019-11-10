# use the list: particles = ["protons", "neutronen", "elektronen"]
# open a file and write the elements of the list seperated by a comma into the file
particles = ["protons", "neutronen", "elektronen"]
filename = "particles.txt"

with open(filename, "w") as f:
    f.write(",".join(particles))
