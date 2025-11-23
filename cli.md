```shell
# .bashrc examples

# personal configuration should be added in a separate file
if [ -f ~/.bash_config ]; then
. ~/.bash_config
fi

# >> .bash_config
# Add time stamp to history
# see strftime documentation for other formatting options
# the last space allows to add a space with the content - this is not a typo :)
HISTTIMEFORMAT="%F %T %z $ "
```

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

___

whoami

man

clear

pwd  # print working directory

ls  # list

cd  #change directory. parent folder: .. ,home:~(alt+n)

mkdir -p f1/f2

touch man.txt test.pdf top.png
touch man.txt  # update timestamp

rmdir  # remove empty directory

rm -v  # verbose remove
rm -r  # f is dangerous
rm -i  # interactive

open  # macos
xdg-open  # ubunutu

mv  # move - rename
mv a b c dest/  # move a,b,c to dest/

cp

head  # first 10th lines
tail  # last 10th lines
-n 50
-f  # live update to log files

date

```shell
> output   # redirection - replace content of output
>> output  # append content to output
```

cat  # conCATenate - print the entire file(s)
cat f1 f2 > output
-n  # display line number

less name
/search

echo "Super" > conf.txt
echo *.??  # wildchars
echo {a,b,c}.txt
echo app.{py,html}
echo {1..99}  # 1 and 99 in

wc  # line/ word/ byte
-l  # line number
-w  # word number

|  # pipe
ls | wc

sort
-n  # sort number
-r  # reverse
-u  # unique only

uniq 
-d  # duplicate
-u  # unique
-c  # count

diff f1 f2
-y  # side by side
-u  # add context

find dir/ -name '*.js'
find dir/ -iname '*.js'  # case insensitive
find dir/ -type d  # directory
find dir/ -type f  # files
find dir/ -type f  -size +100k -size -1M
find dir/ -type f  -size +100k -size -1M -exec cat {} \;

grep  # global regex print
grep -n word file  # find word in file and display line number
-C 2  # 2 lines before/after
-i  # case insensitive

du dir/
-h  # human
du -h | sort -h | tail

df
-h

history
!21  # replay 21th

ps  # process status
ps axww | grep "Visual Studio"

top
-d 5  # refresh every 5s

continue... https://youtu.be/ZtqBQ68cfJc?t=10453