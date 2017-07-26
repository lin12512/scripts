import sys
import os
import json

#dict = {'drawable-mdpi': 'scale-100', "drawable-hdpi": "scale-150", "drawable-xhdpi": "scale-200", "drawable-xxhdpi": "scale-300", "drawable-xxxhdpi": "scale-400"}

def rename(old, new):
  try:
    os.rename(old, new)
  except:
    pass

def travel(basedir):
  for fn in os.listdir(basedir):
    curdir = os.path.join(basedir, fn)
    if not os.path.isdir(curdir):
      continue
    travel(curdir);
    for k, v in dict.iteritems():
      old = os.path.join(basedir, k)
      new = os.path.join(basedir, v)
      rename(old, new)
      

if __name__ == "__main__":
  js=open('config.json')
  dict=json.load(js)
  basedir = '.'
  if(len(sys.argv)>1 and os.path.isdir(sys.argv[1])):
    basedir = sys.argv[1]
  travel(basedir)
