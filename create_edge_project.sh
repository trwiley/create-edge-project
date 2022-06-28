id=`python3 make_id.py`

mkdir $id

python3 make_config.py $id
arg1="/home/edge/edge_dev/edge_ui/EDGE_output//${id}/config.txt"
arg2="/home/edge/edge_dev/edge_ui/EDGE_output//${id}"
echo $arg1
echo $arg2
perl /home/edge/edge/runPipeline -c $arg1 -o $arg2 -cpu 5 -noColorLog -u /home/edge/edge_dev/edge_ui/EDGE_input//916f765d4ae21ed5b2edf1de56479d55/MyUploads/FAR53983_pass_barcode02_359474b4_0.fastq
