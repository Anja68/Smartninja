# use the list: particles = ["protons", "neutronen", "elektronen"]
# open a file and write the elements of the list seperated by a comma into the file

particles = ["protons", "neutronen", "elektronen"]

with open("meineparticles.txt","w") as f:
    content = ",".join(particles)
    f.write(content)