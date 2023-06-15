import sys, glob, os

# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']

# Construct a portable wildcard pattern
pattern = os.path.join(hdir,'*')

# TODO: Use the glob.glob() function to obtain the list of filenames

file_list = glob.glob(pattern)

# TODO: use os.path.getsize to find each file's size
for x in file_list:
    if os.path.getsize(x) > 0:
        print(x, os.path.getsize(x))

print('')
print('')
# TODO: Add a test to only display files that are not zero length

for x in file_list:
    if x == 0:
        list.remove(x)
        print(x, os.path)

# TODO: Remove the leading directory name(s) from each filename before you print it - 
# using os.path.basename()

