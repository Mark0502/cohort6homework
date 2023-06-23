import sys, glob, os

# Get the directory name
if sys.platform == 'win32':                 # This states if system platform is windows 32 then declares
    hdir = os.environ['HOMEPATH']           # hdir(holding name) being equal to operating system and homepath
else:
    hdir = os.environ['HOME']

# Construct a portable wildcard pattern
pattern = os.path.join(hdir, '*')

# TODO: Use the glob.glob() function to obtain the list of filenames

file_directory = glob.glob(pattern)              # This searches the files that match the specific pattern/name (pattern)

# TODO: use os.path.getsize to find each file's size
for files in file_directory:                     # this check's the returned list against file directory
    if os.path.getsize(files) >= 0:              # check's if the files are above or equal to size over zero length
        print(files, os.path.getsize(files))     # prints the return of the size and lists the files and their corresponding size

print('')                                        # This prints a blank line in run file to create a space so text is readable
print('')                                        # again creates a blank line
# TODO: Add a test to only display files that are not zero length

for files in file_directory:                     # this check's the returned list against file directory
    if os.path.getsize(files) > 0:               # check's if the files are greater than zero length
        print(files, os.path.getsize(files))     # prints the return of the size and lists the files and their corresponding size


print('')                                        # again creates a blank line
print('')                                        # again creates a blank line

# TODO: Remove the leading directory name(s) from each filename before you print it - 
# using os.path.basename()

for files in file_directory:                     # this check's the returned list against file directory
    if os.path.getsize(files) > 0:               # check's if the files are greater than zero length
        print(os.path.basename(files), os.path.getsize(files))  # prints the return of the size and lists the files and their corresponding size but removes both leading directory's
