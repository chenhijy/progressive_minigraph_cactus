# 5 G. max

```
snakemake -p --use-singularity --tibanna \
    --default-remote-prefix salk-tm-dev/heidi/data1/hechen/MUsoyGenomes \
    --tibanna-config root_ebs_size=32 log_bucket=salk-tm-logs \
    --default-resources disk_mb=2000000 mem_mb=500000 \
    --configfile configs/5_gMax.json --cores -j 10

kRgexxaU8HXQ	SUCCEEDED	snakemake-job-kRgexxaU8HXQ-rule-generateAssemblyHub	2023-10-26 19:44	2023-10-26 19:54
Bp2PlIceH9yT	SUCCEEDED	snakemake-job-Bp2PlIceH9yT-group-minigraphCactus_run	2023-10-26 17:32	2023-10-26 19:43

```

# 5 G. soja
```
snakemake -p --use-singularity --tibanna \
    --default-remote-prefix salk-tm-dev/heidi/data1/hechen/MUsoyGenomes \
    --tibanna-config root_ebs_size=32 log_bucket=salk-tm-logs \
    --default-resources disk_mb=2000000 mem_mb=500000 \
    --configfile configs/5_gSoj.json --cores -j 10 -n

LHqXgtX9gEYv    SUCCEEDED       snakemake-job-LHqXgtX9gEYv-rule-generateAssemblyHub     2023-10-26 20:59        2023-10-26 21:10
bOxlSHzr0Qaf    SUCCEEDED       snakemake-job-bOxlSHzr0Qaf-group-minigraphCactus_run    2023-10-26 17:32        2023-10-26 20:59
```

# 5 G. max + 5 G. soja (same assemblies as above)
```
snakemake -p --use-singularity --tibanna \
    --default-remote-prefix salk-tm-dev/heidi/data1/hechen/MUsoyGenomes \
    --tibanna-config root_ebs_size=32 log_bucket=salk-tm-logs \
    --default-resources disk_mb=2000000 mem_mb=500000 \
    --configfile configs/10_gSojMax.json --cores -j 10 -n

For MGC rule:
## Starting...
Fri Oct 27 00:35:43 UTC 2023
Done
Fri 27 Oct 2023 07:00:21 AM UTC
Snake marked it as failed but all files were present

qV5JovGs30yq	SUCCEEDED	snakemake-job-qV5JovGs30yq-rule-generateAssemblyHub	2023-10-27 09:39	2023-10-27 09:49

```

# 82 G. max

```
snakemake -p --use-singularity --tibanna \
    --default-remote-prefix salk-tm-dev/heidi/data1/hechen/MUsoyGenomes \
    --tibanna-config root_ebs_size=32 log_bucket=salk-tm-logs \
    --default-resources disk_mb=2000000 mem_mb=500000 \
    --configfile configs/82_gMax.json --cores 128 -j 10 -n

Snake marked it as failed but all files were present:
7cSvVPONdwjC	FAILED	snakemake-job-7cSvVPONdwjC-group-minigraphCactus_run	2023-10-27 09:41	2023-10-29 17:39
```

# 114 G. max and G. soja anchoring to 3 references

### Attempt 1
```
snakemake -p --use-singularity --tibanna \
    --default-remote-prefix salk-tm-dev/heidi/data1/hechen/MUsoyGenomes \
    --tibanna-config root_ebs_size=32 log_bucket=salk-tm-logs \
    --default-resources disk_mb=800000 mem_mb=100000 \
    --configfile configs/114maxAndSoja.json --cores 64 -n
```
Failed -- not enough memory
    raise InsufficientSystemResources(requirer, resource, available)
toil.batchSystems.abstractBatchSystem.InsufficientSystemResources: The job 'minigraph_construct' kind-minigraph_construct/instance-smfbwqh_ v1 is requesting 400,073,848,651 bytes [400+ G] of memory, more than the maximum of 132319395840 bytes of memory that SingleMachineBatchSystem was configured with, or enforced by --maxMemory. Scale is set to 1.0.

### Attempt 2
```
snakemake -p --use-singularity --tibanna \
    --default-remote-prefix salk-tm-dev/heidi/data1/hechen/MUsoyGenomes \
    --tibanna-config root_ebs_size=32 log_bucket=salk-tm-logs \
    --default-resources disk_mb=1000000 mem_mb=500000 \
    --configfile configs/114maxAndSoja.json --cores 64 -j 2 -n
```
Space requirement might be lacking in /tmp, so try setting --workDir

(snake) [ hechen@10.7.30.227:/data1/hechen/workflows/soybean-graph-pangenome/snakemake_mgc/logFor114assemblies ]$ grep space Ys7oMyqv5Ag4.log 
	[2023-12-10T16:25:58+0000] [MainThread] [W] [toil.fileStores.nonCachingFileStore] Starting job files/for-job/kind-export_hal/instance-3dyfxz5r/cleanup/file-c02ff6fe14e042ebb51f31523ef23a99/stream with less than 10%% of disk space remaining.
	OSError: [Errno 28] No space left on device: '/tmp/a30af7ef9fba5e62a1347bb2b988b35d/c779/e359/tmpmv91lm_v/Anc0.hal' -> '/data1/snakemake/cactus/mgc/hub_114_GmaxAndGsoja_GmaxWm82A5ref_231206_mgc/js/files/for-job/kind-export_hal/instance-3dyfxz5r/file-3dce2f3c1d2d40ac87a362455a7088c6/Anc0.hal.f1371417-5de8-4207-acd6-12720bed6200.tmp.hal'
	OSError: [Errno 28] No space left on device: '/tmp/a30af7ef9fba5e62a1347bb2b988b35d/7db8/a9e4/tmp03lzu5aw/Anc0.c2h' -> '/data1/snakemake/cactus/mgc/hub_114_GmaxAndGsoja_GmaxWm82A5ref_231206_mgc/js/files/for-job/kind-cactus_cons/instance-thkd6ng9/file-9c00e431462b459788cc02b587efcb43/Anc0.c2h.dc01924f-83bf-4e80-91f8-1361d5f50763.tmp.c2h'
	[2023-12-10T18:43:26+0000] [MainThread] [W] [toil.fileStores.nonCachingFileStore] Starting job files/for-job/kind-export_hal/instance-3dyfxz5r/cleanup/file-c02ff6fe14e042ebb51f31523ef23a99/stream with less than 10%% of disk space remaining.
	OSError: [Errno 28] No space left on device: '/tmp/a30af7ef9fba5e62a1347bb2b988b35d/8ff2/a550/tmpa_9re8yi/Anc0.hal' -> '/data1/snakemake/cactus/mgc/hub_114_GmaxAndGsoja_GmaxWm82A5ref_231206_mgc/js/files/for-job/kind-export_hal/instance-3dyfxz5r/file-bcc8a627d02543478f3e79e6255e07bb/Anc0.hal.38d30005-91cd-496d-bae1-5052c571d596.tmp.hal'
### Attempt 3 -- killed when not done running on 12/18/23

```
(snake) [ hechen@10.7.30.227:/data1/hechen/workflows/soybean-graph-pangenome/snakemake_mgc ]$ snakemake -p --use-singularity --tibanna     --default-remote-prefix salk-tm-dev/heidi/data1/hechen/MUsoyGenomes     --tibanna-config root_ebs_size=32 log_bucket=salk-tm-logs     --default-resources disk_mb=2000000 mem_mb=600000     --configfile configs/114maxAndSoja.json --cores 64 -j 2 &> logFor114assemblies/runStarted231210_stderrout.txt

(snake) [ hechen@10.7.30.227:/data1/hechen/workflows/soybean-graph-pangenome/snakemake_mgc/logFor114assemblies ]$ lTibanna 
jobid	status	name	start_time	stop_time	instance_id	instance_type	instance_status	ip	key	password
lNG7vf0H3QiT	RUNNING	snakemake-job-lNG7vf0H3QiT-group-minigraphCactus_run	2023-12-10 13:25		i-0234c16ce9e7b1217	r5a.24xlarge	running	44.234.104.150	-	-

```
### Attempt 4 -- finished after 4.7 days
Also try running locally again
```
baseDir=/data1/hechen/MUsoyGenomes/cactus/mgc/mgc_114maxAndSoja
nice apptainer run --nv --bind /data1/`whoami`,${baseDir}/run:/run \
  /data1/hechen/MUsoyGenomes/cactus/cactus-gpu.sif \
  cactus-pangenome ${baseDir}/js \
  ${baseDir}/114seqFile \
  --outDir ${baseDir} --outName mgc_114maxAndSoja \
  --reference GmaxWm82A5_ref Gsoj_PI483463_ref GmaxLeeA3_ref \
  --vcf --giraffe --gfa --gbz --workDir . --maxCores 55

```

## For investigating compute costs later...
```
(snake) [ hechen@10.7.30.227:/data1/hechen/workflows/soybean-graph-pangenome/snakemake_mgc ]$ tibanna stat -l -n 10 -t RUNNING
jobid	status	name	start_time	stop_time	instance_id	instance_type	instance_status	ip	key	password
NYjyeNRjoOrC	RUNNING	snakemake-job-NYjyeNRjoOrC-group-minigraphCactus_run	2023-10-25 23:25		i-0c94eccfada3cb669	m6a.32xlarge	running	18.236.150.255	-	-
FfedJBS1NSsd	RUNNING	snakemake-job-FfedJBS1NSsd-group-minigraphCactus_run	2023-10-25 19:24		i-06ca5b241db0efecc	r6a.16xlarge	running	52.32.202.8	-	-
6NnAjBKFxWol	RUNNING	snakemake-job-6NnAjBKFxWol-group-minigraphCactus_run	2023-10-25 19:23		i-083208cefb0b2993b	r6a.16xlarge	running	34.220.204.80	-	-
ZKFOQSU2CCK9	RUNNING	snakemake-job-ZKFOQSU2CCK9-group-minigraphCactus_run	2023-10-25 19:16		i-02647403abeab4319	r6a.16xlarge	running	35.91.139.187	-	-
o0qDjLFFGVGu	RUNNING	snakemake-job-o0qDjLFFGVGu-group-cactus_run	2023-10-25 18:15		i-0470ee38202c95d15	m6a.32xlarge	running	44.242.150.32	-	-

```
