#! /usr/bin/env python3
import xml.etree.ElementTree as etree
import shutil
import os

# deletes 'lastsaid' blist.xml entries
if os.path.exists("/home/user/.purple/blist.xml"):
	tree = etree.parse("/home/user/.purple/blist.xml")

	buddies = tree.findall(".//buddy")      
	for buddy in buddies:
		nodes = buddy.findall("setting")    
		for node in nodes:
			if node.attrib == {"type": "string","name": "lastsaid"}:
				buddy.remove(node)

tree.write("/home/user/.purple/blist.xml")


# deletes chat log files if they exist
if os.path.exists("/home/user/.purple/logs"):
	shutil.rmtree("/home/user/.purple/logs")
