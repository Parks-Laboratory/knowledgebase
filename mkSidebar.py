import os
import sys

def createSubHierarchy(root, path, filename):
	# base case: root is file
	if len(path) < 1 or not path[0]:
		return
	# normal case: root is directory
	elif len(path) == 1:
		root[path[0]] = filename
		return

	try:
		newRoot = root[path[0]]
	except KeyError:
		newRoot = root[path[0]] = {}

	createSubHierarchy(newRoot, path[1:], filename)

def writeSubHierarchy(root, sidebar, wikiAddress):
	looseFiles = []
	for entry in sorted(root):
		subEntry = root[entry]
		# base case: root is file
		if isinstance(subEntry, str):
			looseFiles.append('<li><a href="{}">{}</a></li>\n'.format(
				wikiAddress + os.path.splitext(subEntry)[0].replace(' ', '-'),
				os.path.splitext(subEntry.split('_')[-1])[0]),
			)
		# normal case: root is directory
		else:
			sidebar.write('<details>\n<summary>{}</summary><ul>\n'.format(entry))
			writeSubHierarchy(root[entry], sidebar, wikiAddress)
			sidebar.write('</ul></details>\n\n'.format(subEntry))
	sidebar.writelines(looseFiles)

def createHierarchy(startpath, ignored, wikiAddress):
	root = {}
	for f in os.listdir(startpath):
		if f not in ignored:
			createSubHierarchy(root, f.split('_'), f)

	sidebar = open('_Sidebar.md', 'w')
	writeSubHierarchy(root, sidebar, wikiAddress)
	sidebar.close();


createHierarchy(
	startpath='.',
	ignored=[
		'.git',
		'test',
		sys.argv[0],
	],
	wikiAddress='https://github.com/Parks-Laboratory/knowledgebase/wiki/',
)
