import sys, glob, os

# Get the directory name
if sys.platform == 'win32':                 # This states if system platform is windows 32 then declares
    hdir = os.environ['HOMEPATH']           # hdir(holding name) being equal to operating system and homepath
else:
    hdir = os.environ['HOME']

# Construct a portable wildcard pattern
pattern = os.path.join(hdir, '*')

# TODO: Use the glob.glob() function to obtain the list of filenames

file_directory = glob.glob(pattern)  # This

# TODO: use os.path.getsize to find each file's size
for i in file_directory:
    if os.path.getsize(i) >= 0:
        print(i, os.path.getsize(i))

print('')
print('')
# TODO: Add a test to only display files that are not zero length

for i in file_directory:
    if os.path.getsize(i) > 0:
        print(i, os.path.getsize(i))


print('')
print('')

# TODO: Remove the leading directory name(s) from each filename before you print it - 
# using os.path.basename()

for i in file_directory:
    if os.path.getsize(i) > 0:
        print(os.path.basename(i), os.path.getsize(i))