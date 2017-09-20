import os
import json
import argparse
import logging
from distutils.dir_util import copy_tree

def update(source_dir, target_dir):
  for k, v in mappings.iteritems():
    if k in excludes:
      continue;
    source = os.path.join(source_dir, k)
    target = os.path.join(target_dir, v)
    if os.path.isdir(source):
      copy_tree(source, target)
    else:
      logging.warning(source + " doesn't exist!")


if __name__ == "__main__":
  parser = argparse.ArgumentParser()

  parser.add_argument(
      "-f", "--config", help="config file that stores key pairs")
  parser.add_argument("-s", "--source_dir", help="source dir")
  parser.add_argument("-t", "--target_dir", help="target dir")

  args = parser.parse_args()

  
  if args.source_dir:
    source_dir = args.source_dir

  target_dir = '.'
  if args.target_dir:
    target_dir = args.target_dir

  config = 'strings.json'
  if args.config:
    config = args.config

  try:
    js = open(config)
    data = json.load(js)
    mappings = data['mappings']
    excludes = data['excludes']
  except IOError, ex:
    logging.warning(ex)
    exit(1)

  update(source_dir,target_dir)
