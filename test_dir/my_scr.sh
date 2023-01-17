
# Iteration of files in my_dir's folders, and print unic
for FILE in */*; do echo $FILE; done | grep my_dir_ | awk -F/ '{print $NF}' | sort -u
