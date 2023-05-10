from utils.dijkstra import *
from utils.rrt import *
from utils.path_comparison import *
from sortedcollections import OrderedSet

coordinates = []
def draw_circle(event,x,y,flags,param):
    global coordinates
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img2,(x,y),5,(255,0,0),-1)
        coordinates.append(x)
        coordinates.append(y)

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description = 'Below are the params:')
    parser.add_argument('-p', type=str, default='input/map1.jpg',metavar='ImagePath', action='store', dest='imagePath',
                    help='Path of the image containing mazes')
    parser.add_argument('-s', type=int, default=10,metavar='Stepsize', action='store', dest='stepSize',
                    help='Step-size to be used for RRT branches')
    parser.add_argument('-start', type=int, default=[20,20], metavar='startCoord', dest='start', nargs='+',
                    help='Starting position in the maze')
    parser.add_argument('-stop', type=int, default=[450,250], metavar='stopCoord', dest='stop', nargs='+',
                    help='End position in the maze')
    parser.add_argument('-selectPoint', help='Select start and end points from figure', action='store_true')

    args = parser.parse_args()

    # remove previously stored data
    try:
      os.system("rm -rf media")
    except:
      print("Dir already clean")
    os.mkdir("media")

    img = cv2.imread(args.imagePath,0) # load grayscale maze image
    print("ORG IMAGE: ", img.shape)
    img2 = cv2.imread(args.imagePath) # load colored maze image
    start = tuple(args.start) #(20,20) # starting coordinate
    end = tuple(args.stop) #(450,250) # target coordinate
    stepSize = args.stepSize # stepsize for RRT
    node_list = [0] # list to store all the node points

    coordinates=[]
    if args.selectPoint:
        print("Select start and end points by double clicking, press 'escape' to exit")
        cv2.namedWindow('image')
        cv2.setMouseCallback('image',draw_circle)
        while(1):
            cv2.imshow('image',img2)
            k = cv2.waitKey(20) & 0xFF
            if k == 27:
                break
        # print(coordinates)

        start=(coordinates[0],coordinates[1])
        end=(coordinates[2],coordinates[3])
    
    print("The start co-ordinate is : ", start)
    print("The end co-ordinate is : ", end)

    # run the RRT algorithm 
    RRT(img, img2, start, end, stepSize)
    print("The RRT path with cost from source to destination is : ")
    print(path)

    # run the Dijkstra algorithm 
    # print("IMG: ",img)
    ret,thresh = cv2.threshold(img,70,255,0)
    # print("BINARY: ", thresh)
    obstacle_points = OrderedSet()
    for i in range(thresh.shape[1]):
        for j in range(thresh.shape[0]):            
            if thresh[j][i] == 0:
                obstacle_points.add((i,thresh.shape[0] - j))

    dstart = (start[0], img.shape[0]-start[1])
    dend = (end[0], img.shape[0]-end[1])
    backtracking_data, traversal_path_cost = dijkstra(dstart, dend, obstacle_points)
    color_img = cv2.cvtColor(img,cv2.COLOR_GRAY2RGB)
    for pts in backtracking_data:
        color_img = cv2.circle(color_img,(pts[0],color_img.shape[0]-pts[1]),1,(0,0,255),-1)
    cv2.imwrite("output/Dijkstra_output.jpg",color_img)
    cv2.imshow("Dijkstra path", color_img)
    cv2.waitKey(0)

    print("The Dijkstra path with cost from source to destination is : ")
    print(traversal_path_cost)

    compare_path(thresh, path, backtracking_data)