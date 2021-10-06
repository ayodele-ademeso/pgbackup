def local(outfile, infile):
    outfile.write(infile.read())
    outfile.close()
    infile.close()