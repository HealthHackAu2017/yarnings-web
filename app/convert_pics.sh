for img in *.png
do
    convert ${img} -resize 50% new_${img}
    mv ${img} orig_${img}
    mv new_${img} ${img}
done

for img in *.png
do
    convert ${img} -transparent white -resize 50% new_${img}
    rm -f ${img}
    mv new_${img} ${img}
done