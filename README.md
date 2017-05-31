# knowledgebase

See the Wiki tab

## Generating a custom sidebar for a GitHub wiki 
The script _mkSidebar.py_ relies on encoded filenames to generate a sidebar with nested contents. 

Underscores are used to create the nesting in the sidebar and each file must have a unique name because the python script assumes the files exist in a flat file structure. 

The page named _DB_MSSMS_Tools_ appears in the sidebar as DB/MSSMS/Tools, where _Tools_ is stored by GitHub as _Tools.md_.

![image](https://github.com/Parks-Laboratory/knowledgebase/blob/master/images/generated_sidebar.PNG)

### Usage
1. If you have not done so, clone the wiki: `git clone https://github.com/Parks-Laboratory/knowledgebase.git`
1. Put a copy of the script _mkSidebar.py_ in the directory containing all your Wiki pages
1. Next, run `python mkSidebar.py`, which will generate the \_Sidebar.md file used by GitHub Wiki to display the sidebar/navigation pane
1. Then, just do `git push` to update the wiki

### Notes
And these are the actual pages. 

![image](https://github.com/Parks-Laboratory/knowledgebase/blob/master/images/actual_files.PNG)

### Acknowledgments
Inspired by https://github.com/bitmovin/github_wiki_index
