def snakemain():
    genomeInfo = snakemake.params["genomeInfo"]
    with open(snakemake.output[0], "w") as fout:
        for l, p in genomeInfo.items():
            fout.write(f"{l}\t{p}\n")


if(__name__ == "__main__"):
    snakemain()

