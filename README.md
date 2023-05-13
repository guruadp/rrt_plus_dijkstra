# Project5
# RRT plus Dijkstra

## Instructions to run
- Unzip the file "proj5_rr94_guruadp.zip" (or) Clone the repository into the local workspace: https://github.com/guruadp/rrt_plus_dijkstra.git

- Get into the repo (if cloned from github)
```
cd rrt_plus_dijkstra/ 
```

- Get into the project folder (if unzipped from zip file "proj5_rr94_guruadp.zip")
```
cd proj5_rr94_guruadp/ 
```

- Open a new terminal
- Run the following command 
```
python3 main.py -selectPoint -p input/map1.jpg -s 7
```
Note: 
1. After running the command above, the image (Obstacle map) will appear on the screen.
2. Double click on the image once to select a source location(Blue dot will appear on the image confirming the selected point), and again double click on the image again to select the goal location (Blue dot will appear on the image confirming the selected point) and then press ESC key.
3. After that, the algorithms will run and provide the ouput path in the folder "output/"
4. Sometimes, the RRT algorithm may not reach the desired goal. In such cases, re-run the program again selecting different source and goal nodes

Other sample commands
```
python3 main.py -selectPoint -p input/map2.jpg -s 5
```

User input note: 
1. Select the points in the image for source and goal (double click for selecting each)
2. The obstacle map is given as image input. (Provide/modify the obstacle map in the command "input/<image_name>")
3. "-s 7" is the stepsize given as 7.   

## Output
1. The Output image (RRT path and Dijkstra path) will be available in the folder "output/"
2. All the parameters used for comparison will be displayed in the output terminal for both RRT and RRT+Dijkstra which are:
- Total Path Length
- Total Path Nodes
- Execution Time