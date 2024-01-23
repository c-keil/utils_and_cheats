# GTK Issues
OpenCV uses gtk for some graphics rendering things. I have run into issues on larger projects where there are version conflicts between gtk2 and gtk3. This manifested as:
```
Gtk-ERROR **: GTK+ 2.x symbols detected. Using GTK+ 2.x and GTK+ 3 in the same process is not supported
```
We want only gtk3. There were 2 problems. One was that the correct version of gtk3 was not being found by cmake when building opencv. This was solved with:
```
apt install libgtk-3-dev
```
But I was still getting the error. This turned out to be becasue one of my compiled libraries was finding a different version of opencv, which still used gtk2. I found this issue by using `lddtree` to track down wich project was using gtk2 libraries. The solution was to rebuild that library with `-DOpenCV_DIR=<path to opencv build>`.