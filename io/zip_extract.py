import os
import zipfile
import argparse

def extract(rootdir, targetdir):
  for f in os.listdir(rootdir):
    cur = os.path.join(rootdir, f)
    if not os.path.isdir(cur) and zipfile.is_zipfile(cur):
      with zipfile.ZipFile(cur,"r") as zip_ref:
        try:
          zip_ref.extractall(targetdir)
        except Exception, ex:
          print ex
    elif os.path.isdir(cur):
      extract(cur, targetdir)
      
if __name__ == "__main__":
  parser = argparse.ArgumentParser()

  parser.add_argument("-d", "--dir", help="root dir")
  parser.add_argument("-t", "--targetdir", help="target dir")
  
  args = parser.parse_args()

  basedir = '.'
  if args.dir:
    basedir = args.dir

  targetdir = '.'
  if args.targetdir:
    targetdir = args.targetdir
  extract(basedir, targetdir)
