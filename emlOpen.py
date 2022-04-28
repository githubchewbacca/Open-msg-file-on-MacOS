import msgtoeml as outlookmsgfile
import tempfile, os, sys
import time

def main(file):

    dirname, basename = os.path.split(file)
    print(basename)
    eml = outlookmsgfile.load(file)
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix='.eml', dir='')
    try:
        print(tmp.name)
        tmp.write(eml.as_bytes())
    finally:
        tmp.close()
        os.system("open " + tmp.name)
        time.sleep(5)
        os.unlink(tmp.name)

if __name__ == "__main__":
    file = sys.argv[1]
    main(file)

