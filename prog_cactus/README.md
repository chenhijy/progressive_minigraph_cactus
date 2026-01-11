## For reference, a list of commands used to generate pCactus axts via EC2 nodes:


### Benchmark (re)creation of 16 genome assembly on AWS - decided to kill this job after it wasn't done running after ~15 days

```
snakemake -p --use-singularity --tibanna
    --default-remote-prefix salk-tm-dev/heidi/data1/hechen/MUsoyGenomes \
    --tibanna-config root_ebs_size=32 log_bucket=salk-tm-logs \
    --default-resources disk_mb=2000000 mem_mb=500000 \
    --configfile configs/16glycineSCN.json --cores 128 -j 10
```
