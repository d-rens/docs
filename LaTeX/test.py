# write a script that checks all sub directories for .tex files and compiles them

import os
import subprocess

# get all subdirectories
subdirs = [x[0] for x in os.walk('.')]
subdirs = subdirs[1:]

# compile all .tex files in subdirectories
for subdir in subdirs:
    for file in os.listdir(subdir):
        if file.endswith('.tex'):
            print(f'Compiling {file} in {subdir}')
            subprocess.run(['pdflatex', file], cwd=subdir)

# clean up
for subdir in subdirs:
    for file in os.listdir(subdir):
        if file.endswith('.log') or file.endswith('.aux'):
            print(f'Removing {file} in {subdir}')
            os.remove(os.path.join(subdir, file))

# move all pdfs to root directory
for subdir in subdirs:
    for file in os.listdir(subdir):
        if file.endswith('.pdf'):
            print(f'Moving {file} to root directory')
            os.rename(os.path.join(subdir, file), os.path.join('.', file))


# Print a message that you did it.
print('Done!')
