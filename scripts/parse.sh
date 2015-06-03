SOURCE_DIR=$1
TARGET_DIR=$2

echo $1
echo $2

mkdir -p $TARGET_DIR

for f in $SOURCE_DIR/*
do
	filename=$(basename $f)
	outname=$TARGET_DIR/$filename.json
	head -n -2 $f | tail -n +3 > $outname
	python classify.py $outname $3
done
