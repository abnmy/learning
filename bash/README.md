cat FILE

diff FILE1 FILE2
diff -rq FOLDER1 FOLDER2

ls -l
ls [Ss]*  # list elemnts which begins with an S or s

grep pattern FILE
grep -i pattern FILE  # insensitive
grep "^the" FILE  # lines of FILE which starts with "the"
grep "!$" FILE  # lines of FILE which ends with "!"

find . -type f -name "S*"  # find file which starts with 'S' in the current directory
find . -type f -exec cat {} \; | grep pattern   # {} receive the filenames
find DIRECTORY -type f -name 'piper' -exec grep pattern '{}' ';'  # without pipe

head FILE  # first ten lines of FILE
head -n 3 FILE  # first three lines of FILE

tail FILE  # last ten lines of FILE
tail -n 5 FILE  # last five lines of FILE

mv file1 file2 file3 destination/  # move all three files to the folder named destination/
mv source/* destination/  # move everything from source to destination

ln -s /path/file /path/link

sort FILE