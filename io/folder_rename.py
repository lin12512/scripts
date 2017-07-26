import sys
import os
import json
import argparse

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
  parser = argparse.ArgumentParser()

  parser.add_argument("-f", "--config", help="config file that stores key pairs")
  parser.add_argument("-d", "--dir", help="base dir")

  args = parser.parse_args()

  basedir = '.'
  if args.dir:
    basedir = args.dir

  config = 'config.json'
  if args.config:
    config = args.config

  try:  
    js=open(config)
    dict=json.load(js)
  except Exception, ex:
    print ex
    
  travel(basedir)
