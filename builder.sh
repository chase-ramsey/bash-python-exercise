#!/bin/bash
output_list=`python reader.py $1`
python writer.py $1 $output_list
