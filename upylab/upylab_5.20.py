def replace(in_path, out_path, pattern, subst):

    fout = open(out_path, "w")

    with open(in_path, encoding="utf-8") as fin:
        for l in fin:
            fout.write(l.replace(pattern, subst))

    fout.close()

replace("Zola.txt", "res.txt", "et", "ET")