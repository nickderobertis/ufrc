#!/bin/bash
datamodel-codegen \
  --input input_files/squeue-output-small.json \
  --input-file-type json \
  --class-name SQueueResponse \
  --output ufrc/squeue/model.py