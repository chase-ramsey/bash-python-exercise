#!/bin/bash
output_list=`python reader.py $1`
python writer.py $output_list
