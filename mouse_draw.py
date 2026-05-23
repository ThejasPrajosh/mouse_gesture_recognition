import pygame
import math

pygame.init()
running = True
drawing = False

#screen
screen_size = pygame.display.get_desktop_sizes()
screen = pygame.display.set_mode(screen_size[0],pygame.FULLSCREEN )
pygame.display.set_caption("Mouse Draw")

#storing the mouse values for detection
mouse_loc = []

#drawing the line
def acc_drawing(s1_pos,s2_pos):
    pygame.draw.aaline(screen,(255,255,255),s1_pos,s2_pos)

#shapes
circle = False

#values
tolerance = 40
threshold = 15
corner = 0
cor_list = []
cor_threshold =  40
smallestangle = 30

def checkcorner():
    cor_list.clear()
    global corner,cor_threshold,smallestangle
    corner = 0
    for i in range(5, len(mouse_loc)-5):
        p1 = mouse_loc[i-5]
        p2 = mouse_loc[i]
        p3 = mouse_loc[i+5]

        vec1 = pygame.math.Vector2(p2[0] - p1[0],p2[1] - p1[1])
        vec2 = pygame.math.Vector2(p3[0] - p2[0],p3[1] - p2[1])
        
        if vec1.length() != 0:
            vec1 = vec1.normalize()
        if vec2.length() != 0:
            vec2 = vec2.normalize()
        dot = vec1.dot(vec2)

        if dot > 1:
            dot = 1
        if dot <-1:
            dot = -1

        angle = math.degrees(math.acos(dot))
        if angle > smallestangle:
            cor_list.append((p2,angle))
        
    last_corner= None
    for i in range(0,len(cor_list)):
        current_pos =cor_list[i][0]
        if last_corner is None:
            corner +=1
            last_corner = current_pos
        else:
            dist = math.dist(current_pos,last_corner)
            if dist>cor_threshold:
                corner += 1
                last_corner = current_pos
    checkcircle()
    print(corner)

#update this in future , might cause err , usign radius
def checkcircle():
    global circle
    circle = False
    start = mouse_loc[0]
    end = mouse_loc[-1]
    end_dist = math.dist(start,end)
    if corner > 4 and end_dist < 50:
        circle = True

def detection():
    global threshold,corner
    if len(mouse_loc) < 5:
        return
    
    #all x and y values
    xs = []
    ys = []
    for point in mouse_loc:
        xs.append(point[0])
        ys.append(point[1])

    #total movement
    hor_tot = max(xs) - min(xs)
    ver_tot = max(ys) - min(ys)

    checkcorner()
    #check if the line is too small
    if hor_tot < 50 and ver_tot < 50:
        print("The line is too small")
        return
    
    #tell what shape it is
    if circle == False:
        if corner <= 1:
            if hor_tot > threshold and ver_tot < tolerance:
                print("Shape: Horizontal Line")
            elif ver_tot > threshold and hor_tot < tolerance:
                print("Shape: Vertical Line")
            else:
                print("Shape: Diagonal Line")
        if corner == 2:
            print("Shape: Triangle")
        elif corner == 3:
            print("Shape: Rectangle")
        elif corner >3:
            print("Shape: Improper Circle")
    else:
        print("Shape: Proper Circle")

#main loop
while running:
    for event in pygame.event.get():
        #quit the program
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
        #Mouse related
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_loc.clear()
            start_pos1= pygame.mouse.get_pos()
            drawing = True
            #reset shapes
            circle = False
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            detection()
        if event.type == pygame.MOUSEMOTION and drawing:
            current_pos = pygame.mouse.get_pos()
            if len(mouse_loc) == 0 or math.dist(current_pos, mouse_loc[-1]) > 5:
                mouse_loc.append(current_pos)
            acc_drawing(start_pos1,current_pos)
            start_pos1 = current_pos
    pygame.display.update()
pygame.quit()
