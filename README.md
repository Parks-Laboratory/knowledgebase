# knowledgebase

See the Wiki tab

## Generating a custom sidebar for a GitHub wiki 
The script _mkSidebar.py_ relies on encoded filenames to generate a sidebar with nested contents. 

Underscores are used to create the nesting in the sidebar and each file must have a unique name because the python script assumes the files exist in a flat file structure. 

The page named _DB_MSSMS_Tools_ appears in the sidebar as DB/MSSMS/Tools, where _Tools_ is stored by GitHub as _Tools.md_.

![image](https://github.com/Parks-Laboratory/knowledgebase/blob/master/images/generated_sidebar.PNG)

### Usage
1. If you have not done so, clone the wiki: `git clone https://github.com/Parks-Laboratory/knowledgebase.wiki.git`
1. Once the repo is cloned, updating the sidebar can be done by `./update.cmd ` in a BASH shell, by `update.cmd` in a Windows shell, or double-clicking it in Windows File Explorer.  _update.cmd_ is a simple script in the repo consisting of the line:     
`git pull && python mkSidebar.py && git commit -a -m "Update sidebar" && git push`

### Notes
These are the actual page names, and how GitHub sees them.

![image](https://github.com/Parks-Laboratory/knowledgebase/blob/master/images/actual_files.PNG)

### Justification for the approach
Encoding a directory hierarchy in the filenames was unavoidable from the start because GitHub's wiki generator will display only one file with a given name, making any other identically-named-files inaccessible. Therefore, even organizing files in directories does not create separate namespaces, and if you want related files to appear next to each other in the default 'Pages' navigator, you must encode that relation in the filenames. The thought, then, was to make the best of the situation and use this encoding to generate a hierarchical sidebar.

### Acknowledgments
Inspired by https://github.com/bitmovin/github_wiki_index
