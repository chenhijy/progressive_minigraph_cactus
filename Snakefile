import json
from snakemake.utils import validate

validate(config, "schema/config.schema.json")


rule cactus:
    input:
        pass
    output:
        pass
    container:
        "docker://quay.io/comparative-genomics-toolkit/cactus:v2.6.9"
    shell:
        """
        cactus --workDir ${outdir}/workDir ${outDir}/jobStore ${outDir}/seqFile ${outDir}/16gMaxSojaForSCNanalysis.hal &> ${outDir}/stdErrOut.txt
        """


