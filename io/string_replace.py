import os
import argparse
import fnmatch

def findReplace(directory, find, replace, filePattern):
  for path, dirs, files in os.walk(os.path.abspath(directory)):
    for filename in fnmatch.filter(files, filePattern):
      filepath = os.path.join(path, filename)
      with open(filepath) as f:
        s = f.read()
        s = s.replace(find, replace)
        with open(filepath, "w") as f:
          f.write(s)
  
if __name__ == "__main__":

  parser = argparse.ArgumentParser()

  parser.add_argument("-o", "--old", help="original name")
  parser.add_argument("-n", "--new", help="new name")
  parser.add_argument("-d", "--dir", help="base dir")
  parser.add_argument("-p", "--pattern", help="file pattern")

  args = parser.parse_args()

  basedir = '.'
  if args.dir:
    basedir = args.dir

  if not args.new and not args.old:
    pass

  findReplace(basedir, args.old, args.new, args.pattern)
