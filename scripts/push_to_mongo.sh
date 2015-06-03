TARGET_DIR=$1

for f in $TARGET_DIR/*
do
	mongoimport --host castleblack --db virus_total --collection analysis --jsonArray $f
done
