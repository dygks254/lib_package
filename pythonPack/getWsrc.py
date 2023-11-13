import os
import pathlib
import argparse
import json
import sys
from jinja2 import Environment, BaseLoader
import subprocess

'''
Get source by Browser
'''

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
GIT_TOP = os.path.join(THIS_DIR, "../..")
sys.path.append(GIT_TOP)

import lib_package.pythonPack as pyPack

def parser():
  parse = argparse.ArgumentParser(description="Get Source by Browser")
  parse.add_argument("--json", type=pyPack.checkPath.validFileType, required=True)
  parse.add_argument("--start_num", type=int, default=0)
  parse.add_argument("--end_num", type=int, default=100)
  return parse

def main(args : dict):
  with open(args.get('json')) as f_json:
    jsonData = json.load(f_json)
    
  for eachHtml in jsonData:
    for each in range(args.get('start_num'), args.get('end_num')+1):
      rtemplate = Environment(loader=BaseLoader).from_string(eachHtml)
      data = rtemplate.render(each=each)
      subprocess.run(data.split(" "))


if __name__ == '__main__':
  args = vars(parser().parse_args())
  main(args)