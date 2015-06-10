SOURCE_DIR=$1

echo $1

for f in $SOURCE_DIR/*
do
	outname=$f
	head -n -5 $f | tail -n +6 > /tmp/out && mv /tmp/out $outname
	echo "{" | cat - $outname > /tmp/out && mv /tmp/out $outname
	sed -i '$s/,$//' $outname
	echo "}" >> $outname
done
