


def snakemain():
    genomepaths = snakemake.params["paths"]
    genomenames = snakemake.params["labels"]
    tree = snakemake.params["tree"]
    with open(snakemake.output[0], "w") as fout:
        fout.write(tree)
        fout.write("\n\n")
        for l, p in zip(genomenames, genomepaths):
            fout.write(f"{l}\t{p}\n")


if(__name__ == "__main__"):
    snakemain()

