# Bash Tips
Here is a list of useful bash shell features and programs

## Programs
- xclip - copying text from command line
- sed - replacing text
- tr - replacing or removing text
- printf - formatting strings: pad with zeros, limmit decimal places etc. 
- ldd - see what libraries are used by an executable
- lddtree - recursively see what libraries are used by an executable

## Tips
### Iterating Over Files
`files=<path>*; for f in files; do echo $f; done`

### Pattern Matching
- basic matching with `*` or `?`
- extended pattern matching with lists of patterns given as `(pattern1|pattern2|...|pattern_n)`
    - `@(pattern1|pattern2)` matches one of the patterns
    - `!()` matches none of the patterns
    - `+()` matches one or more of the patterns
    - there are others

### Parameter expansion
Useful for working with paths
- `${parameter}` basic usage expands a bash variable
- `${param/pattern/replace}` replaces a pattern `//` replaces all instances
- `${param:offset:count}` gets a substring, negative offset from end of string
#### Specific Examples
- Getting the last character of a path `f=<path>; echo ${f: -1:1}`
- Changing a series of file names by replacing a pattern `for f in <path>*; do mv $f ${f/<pattern>/<replace with>}; done`
- Iterating through dirs in a top level directory and renaming files to strip part of the name `for d in *_0[3456789]/*/; do for f in $d*.png; do f1=$(basename $f); mv ${f} $(dirname $f)/${f1/_*/}${f: -4}; done; done` example expanded result `mv ir_timelapse_09/ir_timelapse_10_norm/147_1688485662.0672388.png ir_timelapse_09/ir_timelapse_10_norm/147.png`
- Left padding zeros `printf %03d $parameter`