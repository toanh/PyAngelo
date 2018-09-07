from PyAngelo import *

#allowing randomization
import random

#Setting title, fps, and border
jmss = Graphics(width = 1300, height = 650, title ="Poképong", fps = 60)

#Setting variables
    #of ball
ball_ypos = 239
ball_xpos = 554
ball_yspeed = -9
ball_xspeed = 9

    #Rigt paddle
paddleR_ypos = 232
paddleR_xpos = 1160

    #Left paddle
paddleL_ypos = 232
paddleL_xpos = 20
    #paddle lives
paddleL_lives = 3
paddleR_lives = 3

game_state = 0 # 0 = Title, 1 = Game, 2 = Win

#Pre-loading image into RAM
ball_img = jmss.loadImage("ball.gif") #116 x 116
paddle_L = jmss.loadImage("paddle.L.gif") #27 x 191
paddle_R = jmss.loadImage("paddle.R.gif") #27 x 191
background_img = jmss.loadImage("background.gif")#1300 x 650
title_img = jmss.loadImage("title screen.gif")
win_img = jmss.loadImage("winscreen.gif")


@jmss.mainloop
def game():
    #allowing indented code to access variables
    global ball_ypos, ball_xpos, ball_yspeed, ball_xspeed, ball_img,\
           paddle_L, paddle_R, paddleR_ypos, paddleL_ypos, game_state, paddleL_lives,\
           paddleR_lives

    #Title Screen
    if game_state == 0:
        #Check to see if D is pressed, if yes continue to game (game state 1), if no show title screen
        if jmss.isKeyDown (KEY_D):
            game_state = 1
        #crearing screen
        jmss.clear ()
        #drawing title image
        jmss.drawImage (title_img, 0, 0)

    #game
    elif game_state == 1:
        # check if any player has lost
        if paddleL_lives <= 0 or paddleR_lives <= 0:
            #if yes, continue to win screen
            game_state = 2
        #if no, continue with game
        else:

            #making ball go diagonal
            ball_ypos = ball_ypos + ball_yspeed
            ball_xpos = ball_xpos + ball_xspeed
            
            #makingg ball variables random
            if jmss.isKeyDown(KEY_SPACE):
                ball_yspeed = random_num = random.randint (-7, 7)
                ball_xspeed = random_num = random.randint (-7, 7)

            
            #keys for right paddle
            if jmss.isKeyDown (KEY_DOWN):
                paddleR_ypos = paddleR_ypos -15

            if jmss.isKeyDown (KEY_UP):
                paddleR_ypos = paddleR_ypos +15
                
            #keys for left paddle
            if jmss.isKeyDown (KEY_W):
                paddleL_ypos = paddleL_ypos +15
                
            if jmss.isKeyDown (KEY_S):
                paddleL_ypos = paddleL_ypos -15

            #setting ball's borders
            if ball_ypos <= 0:
                ball_ypos = 0
                #reversing ball direction
                ball_yspeed = -ball_yspeed

            if ball_ypos >= 534:
                ball_ypos = 534
                #reversing ball direction
                ball_yspeed = -ball_yspeed

            #Checking for the ball going off screen
                #Right side
            if ball_xpos > 1380:
                ball_xpos = 554
                ball_ypos = 239
                #decreasing left paddle's lives by 1
                paddleR_lives -= 1
                #reseting ball speed after loosing health
                ball_xspeed = 9
                
                #Left side
            if ball_xpos < -80:
                ball_xpos = 554
                ball_ypos = 239
                #decreasing right paddle's lives by 1
                paddleL_lives -= 1
                #reseting ball speed after loosing health
                ball_xspeed = 9

                
            #setting paddles' borders + snapping it back
            if paddleR_ypos <= -15:
                paddleR_ypos = -15
            
            if paddleR_ypos >= 446:
                paddleR_ypos = 446
                
            if paddleL_ypos <= -15:
                paddleL_ypos = -15
            
            if paddleL_ypos >= 446:
                paddleL_ypos = 446

            #Left paddle Collision
            #If the ball is to the right of the left paddle's x pos, and the ball goes beyond the left paddle's right edge
            if ball_xpos > paddleL_xpos and ball_xpos < paddleL_xpos + 81 and ball_ypos > paddleL_ypos and ball_ypos < paddleL_ypos + 191: #<- Paddle height
                #reverse direction
                ball_xspeed = -ball_xspeed
                #increasing ball speed every time ball hits the paddle
                ball_xspeed *= 1.1
                #Causing ball to bounce off paddle's right edge
                ball_xpos = paddleL_xpos + 81

            #Right paddle Collision
            if ball_xpos + 76 > paddleR_xpos and ball_xpos < paddleR_xpos and ball_ypos > paddleR_ypos and ball_ypos < paddleR_ypos + 191: #<- Paddle height
                #reverse direction
                ball_xspeed = -ball_xspeed
                #increasing ball speed every time ball hits the paddle
                ball_xspeed *= 1.1
                #Causing ball to bounce off paddle's left edge
                ball_xpos = paddleR_xpos - 76
                

            #clearing each frame
            jmss.clear ()
            #drawing ball, background, paddles
            jmss.drawImage(background_img, x = 0, y = 0)
            jmss.drawImage(ball_img, x = ball_xpos, y = ball_ypos)
            jmss.drawImage(paddle_L, x = paddleL_xpos, y = paddleL_ypos)
            jmss.drawImage(paddle_R, x = paddleR_xpos, y = paddleR_ypos)


            #50,550
            '''
            jmss.drawText ("Lives:\n\
                           asdfsssssssssssssssssssssssssssssssssssssss\n \
                           aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n \
                           aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n \
                           aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n \
                           aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n \
                           aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n \
                           aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n \
                           aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n \
                           aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n \
                           aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n \
                           aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n \
                           ssssssssssssssssssssssss" + str(paddleL_lives), 0, 0, fontSize=30)
                           '''
            #jmss.drawText ("Lives:" + str(paddleR_lives), 1140, 550, fontSize=30) 


            #Shows lives

    #Win screen
    elif game_state == 2:
        if paddleL_lives <= 0:
            winner = 2
        else:
            winner = 1
        #If D key is down reset game
        if jmss.isKeyDown (KEY_D):
            game_state = 1
            #Resetting variables 
            ball_ypos = 239
            ball_xpos = 554
            ball_yspeed = -9
            ball_xspeed = 9

            paddleL_lives = 3
            paddleR_lives = 3

        #Showing winner
        jmss.clear()
        #printing win screen background
        jmss.drawImage(win_img, 0, 0)
        #drawing winner and directions
        jmss.drawText("PLAYER " + str(winner) + " WINS!", 375, 290, fontSize = 50)
        jmss.drawText("PRESS D TO RESTART", 400, 230, fontSize = 30)
            
        
    
#Run game
jmss.run()
