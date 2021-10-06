def local(outfile, infile):
    outfile.write(infile.read())
    outfile.close()
    infile.close()

def s3(client, infile, bucket, name):
    client.upload_fileobj(infile, bucket, name)