from queue import PriorityQueue
import time
import pygame as pyg
import numpy as np
import cv2

start = time.time()

###########################################################################################################################
################################# MAP #########################################
##########################################################################

X_SIZE = 600
Y_SIZE = 250

map_size = (Y_SIZE, X_SIZE)

obs_map = np.zeros(map_size)
obs_map.fill(255)

def flip_points(points, height):
    return (points[0], height - points[1])

def map1():
    rectangle_map = obs_map.copy()
    cv2.rectangle(rectangle_map, flip_points((350,50),Y_SIZE), flip_points((350 + 100, 50 + 150), Y_SIZE), (0,0,0), -1)
    #cv2.imshow("rectangle_map", rectangle_map)
    #cv2.waitKey(0)
    return rectangle_map

def map2():
    circle_map = obs_map.copy()
    cv2.circle(circle_map,flip_points((400,125),Y_SIZE), 75, (0,0,0), -1)
    cv2.imshow("circle_map", circle_map)
    cv2.waitKey(0)
    return circle_map

def map3():
    irregular_map = obs_map.copy()
    cv2.rectangle(irregular_map, flip_points((350,50),Y_SIZE), flip_points((350 + 100, 50 + 150), Y_SIZE), (0,0,0), -1)

    cv2.circle(irregular_map,flip_points((400,125),Y_SIZE), 75, (0,0,0), -1)

    cv2.circle(irregular_map,flip_points((350,50),Y_SIZE), 10, (0,0,0), -1)
    cv2.circle(irregular_map,flip_points((450,50),Y_SIZE), 10, (0,0,0), -1)

    cv2.circle(irregular_map,flip_points((350,200),Y_SIZE), 10, (0,0,0), -1)
    cv2.circle(irregular_map,flip_points((450,200),Y_SIZE), 10, (0,0,0), -1)

    cv2.imshow("irregular_map", irregular_map)
    cv2.waitKey(0)
    return irregular_map


# map1()
# map2()
#map3()


def createMap():
    map = []

    # Starting clearance for wall
    for i in range(0,601):
        for j in range(0,6):
            map.append((i,j))

    for i in range(0,601):
        for j in range(245,251):
            map.append((i,j))

    for i in range(0,6):
        for j in range(0,251):
            map.append((i,j))

    for i in range(595,601):
        for j in range(0,251):
            map.append((i,j))
    # Ending clearance for wall
    
    # Rectangle
    for i in range(100,151):
        for j in range(0,101):
            map.append((i,j))

    # Clearance
    for i in range(95,100):
        for j in range(0,101):
            map.append((i,j))

    for i in range(95,100):
        for j in range(145,151):
            map.append((i,j))
    
    ## Rectangle clearance and obstacle
    for i in range(100,151):
        for j in range(101,106):
            map.append((i,j))
        for j in range(145,151):
            map.append((i,j))

    for i in range(151,156):
        for j in range(0,106):
            map.append((i,j))
        for j in range(145,250):
            map.append((i,j))
    
    for i in range(100,151):
        for j in range(150,251):
            map.append((i,j))
    
    for i in range(95,100):
        for j in range(150,251):
            map.append((i,j))

    for i in range(95,100):
        for j in range(100,105):
            map.append((i,j))
    
    for i in range(100,151):
        for j in range(101,105):
            map.append((i,j))
    

    ############ Triangle 

    for i in range(455,460):
        for j in range(20,230):
            map.append((i,j))
    
    for i in range(450,601):
        for j in range(20,230):
            if (2*i - j <= 895) and (2*i+j <= 1145):
                map.append((i,j))
    
    for i in range(450,601):
        for j in range(20,230):
            if (2*i+j <= 1156.18) and (2*i - j <= 906.18):
                map.append((i,j))
    
    ## Printing Hexagon shape
    for i in range(220,380):
        for j in range(40,230):
            if  (j - (0.577)*i - (32.692)) < 0 and (j + (0.577)*i - (378.846)) < 0 and (j - (0.577)*i + (128.846)) > 0 and (j + (0.577)*i - (217.307)) > 0 and (230 <= i <= 370):
                map.append((i,j))
    
    return map

# The below function is used to convert the coordinates to pygame coordinates (bottom left => top left)
def flip_coordinates(coordinates, ht):
    return (coordinates[0], ht-coordinates[1])

def flip_rectangle_coords(coordinates, ht, obj_ht):
    return (coordinates[0], ht - coordinates[1] - obj_ht)

def pygame_plot(closed_list, backtrack_nodes):
    pyg.init()
    display_plot = pyg.display.set_mode((600,250))
    condn = False
    clk = pyg.time.Clock()


    rect_1 = flip_rectangle_coords([95, 0], 250, 105)
    rect_2 = flip_rectangle_coords([95, 145], 250, 105)

    triangle_vertex_1 = flip_coordinates([455, 20], 250)
    triangle_vertex_2 = flip_coordinates([463, 20], 250)
    triangle_vertex_3 = flip_coordinates([515.5, 125], 250)
    triangle_vertex_4 = flip_coordinates([463, 230], 250)
    triangle_vertex_5 = flip_coordinates([455, 230], 250)

    hexagon_vertex_1 = flip_coordinates([300, 205.76], 250)
    hexagon_vertex_2 = flip_coordinates([230, 165.38], 250)
    hexagon_vertex_3 = flip_coordinates([230, 84.61], 250)
    hexagon_vertex_4 = flip_coordinates([300, 44.23], 250)
    hexagon_vertex_5 = flip_coordinates([370, 84.61], 250)
    hexagon_vertex_6 = flip_coordinates([370, 165.38], 250)

    while not condn:
        for frame in pyg.event.get():
            if frame.type == pyg.QUIT:
                condn = True

        pyg.draw.rect(display_plot, (0,0,255), pyg.Rect(rect_1[0], rect_1[1], 60, 105))
        pyg.draw.rect(display_plot, (0,0,255), pyg.Rect(rect_2[0], rect_2[1], 60, 105))
        pyg.draw.polygon(display_plot, (0,0,255), ((hexagon_vertex_1),(hexagon_vertex_2),(hexagon_vertex_3),(hexagon_vertex_4),(hexagon_vertex_5),(hexagon_vertex_6)))
        pyg.draw.polygon(display_plot, (0,0,255), ((triangle_vertex_1),(triangle_vertex_2),(triangle_vertex_3), (triangle_vertex_4), (triangle_vertex_5)))

        pyg.draw.rect(display_plot, (255,0,0), pyg.Rect(100, 0, 50, 100))
        pyg.draw.rect(display_plot, (255,0,0), pyg.Rect(100, 150, 50, 100))
        pyg.draw.polygon(display_plot, (255,0,0), ((235,87.5),(300,50),(365,87.5),(365,162.5),(300,200),(235,162.5)))
        pyg.draw.polygon(display_plot, (255,0,0), ((460, 25),(460, 225),(510, 125)))
        
        ## Wall definition
        pyg.draw.rect(display_plot, (0,0,255) ,pyg.Rect(0, 0, 5, 250))
        pyg.draw.rect(display_plot, (0,0,255) ,pyg.Rect(595, 0, 5, 250))
        pyg.draw.rect(display_plot, (0,0,255) ,pyg.Rect(0, 0, 600, 5))
        pyg.draw.rect(display_plot, (0,0,255) ,pyg.Rect(0, 245, 600, 5))

        for val in closed_list:
            pyg.draw.circle(display_plot, "purple", flip_coordinates(val, 250), 1)
            pyg.display.flip()
            clk.tick(500)

        for item in backtrack_nodes:
            pyg.draw.circle(display_plot, "gray", flip_coordinates(item, 250), 1)
            pyg.display.flip()
            clk.tick(30)
        pyg.display.flip()
        pyg.time.wait(3000)
        condn = True
    pyg.quit()


def back_tracking(path, initial_state, current_node, cost_map):
    optimal_path = []
    cost_list = []
    node_path_cost = []
    optimal_path.append(current_node)
    parent_path = current_node
    while parent_path != initial_state:
        cost_list.append(cost_map[(parent_path,path[parent_path])])  
        #node_path_cost.append((path[parent_path], parent_path, cost_map[(parent_path,path[parent_path])]))
        node_path_cost.append((parent_path, cost_map[(parent_path,path[parent_path])]))
        parent_path = path[parent_path]
        optimal_path.append(parent_path)
    
    optimal_path.reverse()
    cost_list.reverse()
    node_path_cost.reverse()
    return optimal_path, len(optimal_path), cost_list, node_path_cost

def check_duplicate(Node, prev_coordinates, cost):
    for i in range(p_q.qsize()):
        if p_q.queue[i][1] == Node[1]:
            if p_q.queue[i][0] > Node[0]:
                p_q.queue[i] = Node
                return
            else:
                return
    
    p_q.put(Node)
    node_path[Node[1]] = prev_coordinates
    cost_map[(Node[1],prev_coordinates)] = np.round(cost,1)
    
                     

def ActionMoveLeft(curr_node, obstacle_map):
    (x_curr,y_curr)  = curr_node[1]
    new_coord = (x_curr-1, y_curr)

    if new_coord not in visited_nodes and new_coord not in obstacle_map:
        cost = curr_node[0]+1
        new_node = (cost, new_coord)
        check_duplicate(new_node, (x_curr,y_curr), cost) 
        


def ActionMoveRight(curr_node, obstacle_map):
    (x_curr,y_curr)  = curr_node[1]
    new_coord = (x_curr+1, y_curr)

    if new_coord not in visited_nodes and new_coord not in obstacle_map:
        cost = curr_node[0]+1
        new_node = (cost, new_coord)
        check_duplicate(new_node, (x_curr,y_curr), cost)

def ActionMoveUp(curr_node, obstacle_map):
    (x_curr,y_curr)  = curr_node[1]
    new_coord = (x_curr, y_curr+1)

    if new_coord not in visited_nodes and new_coord not in obstacle_map:
        cost = curr_node[0]+1
        new_node = (cost, new_coord)
        check_duplicate(new_node, (x_curr,y_curr),cost)

def ActionMoveDown(curr_node, obstacle_map):
    (x_curr,y_curr)  = curr_node[1]
    new_coord = (x_curr, y_curr-1)

    if new_coord not in visited_nodes and new_coord not in obstacle_map:
        cost = curr_node[0]+1
        new_node = (cost, new_coord)
        check_duplicate(new_node, (x_curr,y_curr),cost)

def ActionMoveUpLeft(curr_node, obstacle_map):
    (x_curr,y_curr)  = curr_node[1]
    new_coord = (x_curr-1, y_curr+1)

    if new_coord not in visited_nodes and new_coord not in obstacle_map:
        cost = curr_node[0]+1.4
        new_node = (cost, new_coord)
        check_duplicate(new_node, (x_curr,y_curr),cost)

def ActionMoveUpRight(curr_node, obstacle_map):
    (x_curr,y_curr)  = curr_node[1]
    new_coord = (x_curr+1, y_curr+1)

    if new_coord not in visited_nodes and new_coord not in obstacle_map:
        cost = curr_node[0]+1.4
        new_node = (cost, new_coord)
        check_duplicate(new_node, (x_curr,y_curr),cost)

def ActionMoveDownLeft(curr_node, obstacle_map):
    (x_curr,y_curr)  = curr_node[1]
    new_coord = (x_curr-1, y_curr-1)

    if new_coord not in visited_nodes and new_coord not in obstacle_map:
        cost = curr_node[0]+1.4
        new_node = (cost, new_coord)
        check_duplicate(new_node, (x_curr,y_curr), cost)

def ActionMoveDownRight(curr_node, obstacle_map):
    (x_curr,y_curr)  = curr_node[1]
    new_coord = (x_curr+1, y_curr-1)

    if new_coord not in visited_nodes and new_coord not in obstacle_map:
        cost = curr_node[0]+1.4
        new_node = (cost, new_coord)
        check_duplicate(new_node, (x_curr,y_curr), cost)

p_q = PriorityQueue()
# obstacle = map3()
# obstacleMap = []
obstacleMap = createMap()

# for i in range(obstacle.shape[1]):
#     for j in range(obstacle.shape[0]):
#         if obstacle[j][i] == 0:
#             obstacleMap.append((i,j))

#obstacleMap.append(np.where(obstacle == 0))
#obstacleMap = list(obstacleMap)
print("The obstacle map is : ")
print(obstacleMap)
sourceNode_status = False
goalNode_status = False
source_point = ()
goal_point = ()
cost_map = {}

#source_point = (183,133)
while sourceNode_status == False:

    print("Enter the x and y co-ordinate of source node in integer : ")
    x_source = int(input()) 
    y_source = int(input())
    source_point = (x_source,y_source)
    print("The source node is :")
    print(source_point)

    if source_point not in obstacleMap:
        sourceNode_status = True
        print("The entered source node co-ordinate is not an obstacle. ")
        break

    else:
        print("The entered source node co-ordinate is an obstacle. Please enter another co-ordinate ")

#goal_point = (558,135)
while goalNode_status == False:

    print("Enter the x and y co-ordinate of goal node in integer : ")
    x_goal = int(input()) 
    y_goal = int(input())
    goal_point = (x_goal,y_goal)

    if goal_point not in obstacleMap:
        goalNode_status = True
        print("The entered goal node co-ordinate is not an obstacle. ")
        break

    else:
        print("The entered goal node co-ordinate is an obstacle. Please enter another co-ordinate ")

visited_nodes = []
node_path = {}
source_node = (0,source_point)
status = False
p_q.put(source_node)

while True:
    curr_node = p_q.get()
    visited_nodes.append(curr_node[1])
    (x,y) = curr_node[1]
    if curr_node[1] != goal_point:
        if y-1 > 0:
            ActionMoveDown(curr_node, obstacleMap)
        if x-1 > 0:
            ActionMoveLeft(curr_node, obstacleMap)
        if y+1 < 250:
            ActionMoveUp(curr_node, obstacleMap)
        if x+1 < 600:
            ActionMoveRight(curr_node, obstacleMap)
        if x-1 > 0 and y+1 < 250:
            ActionMoveUpLeft(curr_node, obstacleMap)
        if x+1 < 600 and y+1 < 250:
            ActionMoveUpRight(curr_node, obstacleMap)
        if x-1 > 0 and y-1 > 0:
            ActionMoveDownLeft(curr_node, obstacleMap)
        if x+1 < 600 and y-1 > 0:
            ActionMoveDownRight(curr_node, obstacleMap)
        
    else:
        end = time.time()
        time_taken = end-start
        print("Reached x coordinate is:",x)
        print("Reached y coordinate is:",y)
        print("time taken for reaching from source to destination is ", time_taken)
        backtracking_data, length, cost_list, traversal_path_cost = back_tracking(node_path, source_point, curr_node[1], cost_map)
        print("The backtracked data from source to goal nodes are as follows: ")
        print(backtracking_data)
        print("The cost list from source to destination is : ")
        print(cost_list)
        print("The path along with cost from source to destination is : ")
        print(traversal_path_cost)

        rrt_traversal_path_cost = traversal_path_cost
        print("The RRT traversal ")

        pygame_plot(visited_nodes, backtracking_data)
        break









