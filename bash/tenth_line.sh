# not sure how to get one line
head -10 file.txt

# The sed command is used to edit a stream of text, and -n option is used to suppress the output.
# The 10p command prints only the 10th line of the input file. So, '10p' prints the 10th line.
sed -n '10p' file.txt

# Solution 1
cnt=0
while read line && [ $cnt -le 10 ]; do let 'cnt = cnt + 1' if [ $cnt -eq 10 ]; then
    echo $line
    exit 0
  fi
done < file.txt

# Solution 2
awk 'FNR == 10 {print }'  file.txt
# OR
awk 'NR == 10' file.txt

# Solution 3
sed -n 10p file.txt

# Solution 4
tail -n+10 file.txt|head -1