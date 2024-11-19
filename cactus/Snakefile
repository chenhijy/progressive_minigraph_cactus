import json
import os
from snakemake.utils import validate

validate(config, "schema/config.schema.json")


groupsuffix = "run"


rule all:
    input:
        config["outbase"] + ".hal"


rule makeseqfile:
    output:
        config["outbase"] + ".seqfile.txt"
    params:
        labels = [k for k in config["genomes"].keys()],
        tree = config["tree"],
        paths = [v for v in config["genomes"].values()]
    group:
        "cactus" + groupsuffix
    script:
        "scripts/build_seqfile.py"


rule cactus:
    input:
        genomes = [v for v in config["genomes"].values()],
        seqfile = rules.makeseqfile.output[0]
    output:
        config["outbase"] + ".hal"
    container:
        "docker://quay.io/comparative-genomics-toolkit/cactus:v2.6.9"
    params:
        tree = config["tree"],
        wkdir = "WkDir",
        jobstore = "jobStore"
    group:
        "cactus" + groupsuffix
    threads:
        config["threads"]
    shell:
        """
        mkdir {params.wkdir}
        cactus --workDir {params.wkdir} {params.jobstore} {input.seqfile} {output} --defaultCores {threads}
        """


