import cv2
import math
points = []
def get_integer_points(x1, y1, x2, y2):
    global points
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    x = x1
    y = y1
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1

    if dx > dy:
        err = dx / 2
        while x != x2:
            points.append((x, y))
            err -= dy
            if err < 0:
                y += sy
                err += dx
            x += sx
    else:
        err = dy / 2
        while y != y2:
            points.append((x, y))
            err -= dx
            if err < 0:
                x += sx
                err += dy
            y += sy

    points.append((x, y))  # Include the second point
    # return points

# obs_map = cv2.imread("space.jpg")
# rrt_path = [(15, 50), (21, 51), (28, 49), (35, 49), (42, 51), (42, 58), (46, 64), (53, 63), (60, 64), (67, 67), (67, 74), (64, 80), (62, 87), (55, 90), (56, 97), (60, 102), (61, 109), (61, 116), (66, 121), (71, 125), (76, 130), (82, 132), (89, 134), (96, 135), (102, 138), (109, 140), (116, 141), (123, 139), (129, 140), (136, 139), (143, 136), (235, 235)]
# dijkstra_path = [(15, 50), (16, 50), (17, 50), (18, 51), (19, 52), (20, 52), (21, 53), (22, 54), (23, 55), (24, 56), (25, 57), (26, 58), (27, 59), (28, 60), (29, 61), (30, 62), (31, 63), (32, 64), (33, 65), (34, 66), (35, 67), (36, 68), (37, 69), (38, 70), (39, 71), (40, 72), (41, 73), (42, 74), (43, 75), (44, 76), (45, 77), (46, 78), (47, 79), (48, 80), (49, 81), (50, 82), (51, 83), (52, 84), (53, 85), (54, 86), (55, 87), (56, 88), (57, 89), (58, 90), (59, 91), (60, 92), (61, 93), (62, 94), (63, 94), (64, 94), (65, 94), (66, 94), (67, 94), (68, 94), (69, 94), (70, 94), (71, 94), (72, 94), (73, 94), (74, 94), (75, 94), (76, 94), (77, 94), (78, 94), (79, 94), (80, 94), (81, 94), (82, 94), (83, 94), (84, 94), (85, 95), (86, 96), (87, 97), (88, 98), (89, 99), (90, 100), (91, 101), (92, 102), (93, 103), (94, 104), (95, 105), (96, 105), (97, 105), (98, 105), (99, 105), (100, 106), (101, 106), (102, 106), (103, 106), (104, 106), (105, 106), (106, 106), (107, 106), (108, 106), (109, 106), (110, 106), (111, 106), (112, 106), (113, 106), (114, 106), (115, 106), (116, 106), (117, 106), (118, 107), (119, 108), (120, 109), (121, 110), (122, 111), (123, 112), (124, 113), (125, 114), (126, 115), (127, 116), (128, 117), (129, 118), (130, 119), (131, 120), (132, 121), (133, 122), (134, 123), (135, 124), (136, 125), (137, 126), (138, 127), (139, 128), (140, 129), (141, 130), (142, 131), (143, 132), (144, 133), (145, 134), (146, 135), (147, 136), (148, 137), (149, 138), (150, 139), (151, 140), (152, 141), (153, 142), (154, 143), (155, 144), (156, 145), (156, 146), (156, 147), (156, 148), (156, 149), (156, 150), (156, 151), (156, 152), (156, 153), (156, 154), (156, 155), (156, 156), (157, 157), (158, 158), (159, 159), (160, 160), (161, 161), (162, 162), (163, 163), (164, 164), (165, 165), (166, 166), (167, 167), (168, 168), (169, 169), (170, 170), (171, 171), (172, 172), (173, 173), (174, 174), (175, 175), (176, 176), (177, 177), (178, 178), (179, 179), (180, 180), (181, 181), (182, 182), (183, 183), (184, 184), (185, 185), (186, 186), (187, 187), (188, 188), (189, 189), (190, 190), (191, 191), (192, 192), (193, 193), (194, 194), (195, 195), (196, 196), (197, 197), (198, 198), (199, 199), (200, 200), (201, 201), (202, 202), (203, 203), (204, 204), (205, 205), (206, 206), (207, 207), (208, 208), (209, 209), (210, 210), (211, 211), (212, 212), (213, 213), (214, 214), (215, 215), (216, 216), (217, 217), (218, 218), (219, 219), (220, 220), (221, 221), (222, 222), (223, 223), (224, 224), (225, 225), (226, 226), (227, 227), (228, 228), (229, 229), (230, 230), (231, 231), (232, 232), (233, 233), (234, 234), (235, 235)]
# print("Length of RRT path: ", len(rrt_path))
# print("Length of Dijkstra path: ", len(dijkstra_path))
def euclidean_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    # print("POINTS: ", point1, point2)
    # print("DIST: ", distance)
    return distance

def compare_path(obs_map, rrt_path, dijkstra_path, dijkstra_path_with_cost):
    
    print("Comparing path........")
    h,l = obs_map.shape
    obs_map = cv2.cvtColor(obs_map,cv2.COLOR_GRAY2RGB)
    optimal_map = obs_map.copy()
    R_PATH = []
    D_PATH = []
    for i in range(len(rrt_path)-1):
        # print("XX: ",rrt_path[i][0], rrt_path[i][1], rrt_path[i+1][0], rrt_path[i+1][1])
        get_integer_points(rrt_path[i][0], rrt_path[i][1], rrt_path[i+1][0], rrt_path[i+1][1])
        # R_PATH.append(pt)

    R_PATH = points

    R_PATH = [i for n, i in enumerate(R_PATH) if i not in R_PATH[:n]]

    R_PATH_WITH_COST = [(R_PATH[0], 0)]
    
    for i in range(len(R_PATH[1:])):
        # print(R_PATH_WITH_COST[-1][1])
        R_PATH_WITH_COST.append((R_PATH[i+1], R_PATH_WITH_COST[-1][1] + euclidean_distance(R_PATH[i+1],R_PATH[i])))
    # points = []
    # for i in range(len(dijkstra_path)-1):
    #     get_integer_points(dijkstra_path[i][0], dijkstra_path[i][1], dijkstra_path[i+1][0], dijkstra_path[i+1][1])

    # D_PATH = points
    # print("RRT WITH COST: ", R_PATH_WITH_COST)
    # print("Length of RRT path after expanding: ", len(R_PATH))
    # print("Length of Dijkstra path after expanding: ", len(D_PATH))
    for i in range(len(rrt_path)-1):
        cv2.line(obs_map, (rrt_path[i][0], h - rrt_path[i][1]), (rrt_path[i+1][0], h - rrt_path[i+1][1]), (255,0,0), thickness=1, lineType=8)
    # print("3")
    for i in range(len(dijkstra_path)-1):
        cv2.line(obs_map, (dijkstra_path[i][0], h - dijkstra_path[i][1]), (dijkstra_path[i+1][0], h - dijkstra_path[i+1][1]), (0,255,0), thickness=1, lineType=8)
    # print("4")
    match_points = []
    for d_path in dijkstra_path:
        for r_path in R_PATH:
            if d_path == r_path:
                if d_path not in match_points:
                    match_points.append(d_path)

                cv2.circle(obs_map, (d_path[0], obs_map.shape[0] - d_path[1]), 1, (0,0,255), -1)

    opti_path = []
    opti_path_with_cost = []
    for i in range(len(match_points)-1):
        # print("E DIST: ", euclidean_distance(match_points[i], match_points[i+1]))
        if euclidean_distance(match_points[i], match_points[i+1]) > 10:
            r_idx_n = R_PATH.index(match_points[i+1])
            d_idx_n = dijkstra_path.index(match_points[i+1])
            print("Next idx: ", r_idx_n, d_idx_n)
            r_idx = R_PATH.index(match_points[i])
            d_idx = dijkstra_path.index(match_points[i])
            print("Curr idx: ", r_idx, d_idx)
            # rrt_cost = R_PATH_WITH_COST[r_idx][1]
            # dij_cost = dijkstra_path_with_cost[d_idx][1]
            rrt_cost = R_PATH_WITH_COST[r_idx_n][1] - R_PATH_WITH_COST[r_idx][1]
            dij_cost = dijkstra_path_with_cost[d_idx_n][1] - dijkstra_path_with_cost[d_idx][1]
            print("R cost at Match point "+str(i+1)+": ", rrt_cost)
            print("D cost at Match point "+str(i+1)+": ", dij_cost)
            if abs(rrt_cost - dij_cost) < 5:
                print("Adding R Path")
                sliced_path = R_PATH[r_idx:r_idx_n+1]
                opti_path.extend(sliced_path)
            else:
                print("Adding D Path")
                sliced_path = dijkstra_path[d_idx:d_idx_n+1]
                opti_path.extend(sliced_path)

        else:
            print("Adding R Path")
            r_idx = R_PATH.index(match_points[i])
            r_idx_n = R_PATH.index(match_points[i+1])
            sliced_path = R_PATH[r_idx:r_idx_n+1]
            opti_path.extend(sliced_path)

    opti_path = [i for n, i in enumerate(opti_path) if i not in opti_path[:n]]

    print("Opti path: ", opti_path)

    for i in range(len(opti_path)-1):
        cv2.line(optimal_map, (opti_path[i][0], h - opti_path[i][1]), (opti_path[i+1][0], h - opti_path[i+1][1]), (255,0,0), thickness=1, lineType=8)
    print("Matching points: ",match_points)

    print("Num of nodes in RRT: ", len(rrt_path))
    print("Num of nodes in RRT+Dijkstra: ", len(optimal_map))

    print("Cost of RRT: ", R_PATH_WITH_COST[-1][1])
    print("Cost of RRT+Dijkstra: ")

    combime_map = cv2.hconcat([obs_map, optimal_map])
    # cv2.imshow("Final", combime_map)
    # cv2.imwrite("output/output_matching.jpg", obs_map)
    cv2.imwrite("output/optimal.jpg", combime_map)
    cv2.waitKey(0)

