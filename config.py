# -*- coding: utf-8 -*-
import os
import sys
import glob
import yaml

yamls = {}
suffix = '.yaml'
eagle_path=os.path.dirname(os.path.abspath(__file__))


main_configuration=yaml.load(open('main.yaml'))
rules_folder=main_configuration['rules_folder']

yaml_rules=os.path.join(eagle_path,rules_folder)

files=[f for f in os.listdir(yaml_rules) if os.path.isfile(os.path.join(yaml_rules,f))]

for filename in files:
	filename=os.path.join(eagle_path+"/"+rules_folder+"/"+filename)
	with open(filename) as f:
		yamls.update(yaml.load(f))
