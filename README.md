# knowledgebase

See the Wiki tab

## Generating a custom sidebar for a GitHub wiki 
The script _mkSidebar.py_ relies on encoded filenames to generate a sidebar with nested contents. 

![image](https://github.com/Parks-Laboratory/knowledgebase/blob/master/images/generated_sidebar.PNG)

### Uusage
Underscores are used to create the nesting in the sidebar and each file must have a unique name because the python script assumes the files exist in a flat file structure. 

The page named _DB_MSSMS_Tools_ appears in the sidebar as DB/MSSMS/Tools, where _Tools_ is stored by GitHub as _Tools.md_.

### Notes
And these are the actual pages. 

![image](https://github.com/Parks-Laboratory/knowledgebase/blob/master/images/actual_files.PNG)

### Acknowledgments
Inspired by https://github.com/bitmovin/github_wiki_index
