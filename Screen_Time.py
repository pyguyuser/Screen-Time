import pygame,time
pygame.init()
W,H,fps,x_coord,y_coord,step_x,step_y,R,G,B,control,nconst_1,nconst_2 = 1600,900,120,0,0,1,1,50,0,0,0,255,5
clock = pygame.time.Clock()
display = pygame.display.set_mode((W,H))
# surface = pygame.Surface((212,50))
text_vid = pygame.font.SysFont('Times New Roman', 60)
def colormix():
    global R,G,B,control,nconst_1,nconst_2
    if R!=nconst_1:R+=nconst_2
    else:
        if G!=nconst_1:G+=nconst_2
        else:
            if B!=nconst_1:B+=nconst_2
            else:control+=3
    if control==3:nconst_1,nconst_2=50,-5
    if control==6:control,R,G,B,nconst_1,nconst_2=0,50,0,0,255,5
pygame.mouse.set_visible(False)
run = True
while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
    display.fill('black')
    colormix()
    par_text = text_vid.render(time.asctime().split(" ")[3], 1,(R,G,B))
    display.blit(par_text,(x_coord,y_coord-8))
    # display.blit(surface,(x_coord,y_coord))
    x_coord += step_x
    y_coord += step_y
    if x_coord + 212 == W or x_coord == 0:
        step_x *= -1
    if y_coord + 50 == H or y_coord == 0:
        step_y *= -1
    pygame.display.update()
    clock.tick(fps)
pygame.quit()