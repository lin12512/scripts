import os
import argparse

def rename(old, new, rootdir):
  try:
    for fn in os.listdir(rootdir):
      curdir = os.path.join(rootdir, fn)
      if not os.path.isdir(curdir):
        os.rename(curdir, curdir.replace(old, new))
      else:
        rename(old, new, curdir)
  except Exception,ex:
    print ex
  
if __name__ == "__main__":

  parser = argparse.ArgumentParser()

  parser.add_argument("-o", "--old", help="original name")
  parser.add_argument("-n", "--new", help="new name")
  parser.add_argument("-d", "--dir", help="base dir")

  args = parser.parse_args()

  basedir = '.'
  if args.dir:
    basedir = args.dir

  if not args.new and not args.old:
    pass

  rename(args.old, args.new, basedir)
