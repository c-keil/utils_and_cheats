# Bash Tips
Here is a list of useful bash shell features and programs

## Programs
- xclip - copying text from command line
- sed - replacing text
- tr - replacing or removing text

## Tips
### Iterating Over Files
`files=<path>*; for f in files; do echo $f; done`

### Parameter expansion
Useful for working with paths
- `${parameter}` basic usage expands a bash variable
- `${param/pattern/replace}` replaces a pattern `//` replaces all instances
- `${param:offset:count}` gets a substring, negative offset from end of string
#### Specific Examples
- Getting the last character of a path `f=<path>; echo ${f: -1:1}`
- Changing a series of file names by replacing a pattern `for f in <path>*; do mv $f ${f/<pattern>/<replace with>}; done`