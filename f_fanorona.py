import pygame
import Tkinter

class Blank:    #Render nothing
	def __init__(self, screen, posx, posy):     #constructor   
		self.selfpx=posx
		self.selfpy=posy
		self.pos =  (posx, posy)

	def Render(self, screen):
		ren=True

class LightDisk: #Light Coins

	def __init__(self, screen, posx, posy):       #constructor 
		self.selfpx=posx
		self.selfpy=posy
		self.pos =  (posx, posy)

	def Render(self, screen):
		lightcoin = pygame.image.load("light.png")
		lightcoin = pygame.transform.scale(lightcoin, (60,60))
		screen.blit(lightcoin, (self.pos[0]-30, self.pos[1]-30))

boardconfig = [[2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 1, 2, 1, 0, 2, 1, 2, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1]]
move_list_length=0
player=1
move_list_length_withdraw=0
move_list_x =[0, 0, 0, 0, 0, 0, 0, 0]
move_list_y =[0, 0, 0, 0, 0, 0, 0, 0]
move_list_x_withdraw =[0, 0, 0, 0, 0, 0, 0, 0]
move_list_y_withdraw =[0, 0, 0, 0, 0, 0, 0, 0]
move=[0,0,0,0,0]
RenderList=[] # list of objects
check = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
capture = 0
apwd=0
checkbatao=0
MouseReleased=False

class DarkDisk:     #Dark Coins

	def __init__(self, screen, posx, posy):     #constructor
		self.selfpx=posx
		self.selfpy=posy
		self.pos =  (posx, posy)

	def Render(self, screen):
		lightcoin = pygame.image.load("dark.png")
		lightcoin = pygame.transform.scale(lightcoin, (60,60))
		screen.blit(lightcoin, (self.pos[0]-30, self.pos[1]-30))

def coins_to_kill(x_current,y_current,x_new,y_new, player): # check is 1 for toward-capture and 2 for withdraw capture
	global boardconfig
	global check
	if check[x_new][y_new] == 1:
		if x_new > x_current and y_new == y_current:
			x_new += 1
			while ( x_new <= 4 and (boardconfig[x_new][y_new] != player and boardconfig[x_new][y_new] != 0) ):
				boardconfig[x_new][y_new] = 0
				x_new += 1
		
		if x_new < x_current and y_new == y_current:
			x_new -= 1
			while (x_new >= 0 and (boardconfig[x_new][y_new] != player and boardconfig[x_new][y_new] != 0) ):
				boardconfig[x_new][y_new] = 0
				x_new -= 1

		if x_new == x_current and y_new > y_current:
			y_new += 1
			while ( y_new<= 8 and (boardconfig[x_new][y_new] != player and boardconfig[x_new][y_new] != 0) ):
				boardconfig[x_new][y_new] = 0
				y_new += 1

		if x_new == x_current and y_new < y_current:
			y_new -= 1
			while ( y_new>= 0 and (boardconfig[x_new][y_new] != player and boardconfig[x_new][y_new] != 0)):
				boardconfig[x_new][y_new] = 0
				y_new -= 1

		if x_new > x_current and y_new > y_current:
			x_new += 1
			y_new += 1
			while ( x_new<= 4 and  y_new<= 8 and (boardconfig[x_new][y_new] != player and boardconfig[x_new][y_new] != 0)  ):
				boardconfig[x_new][y_new] = 0
				x_new += 1
				y_new += 1

		if x_new < x_current and y_new > y_current:
			x_new -= 1
			y_new += 1
			while (x_new>= 0 and  y_new<= 8 and (boardconfig[x_new][y_new] != player and boardconfig[x_new][y_new] != 0)  ):
				boardconfig[x_new][y_new] = 0
				x_new -= 1
				y_new += 1

		if x_new < x_current and y_new < y_current:
			x_new -= 1
			y_new-= 1
			while ( x_new>= 0 and  y_new>= 0 and (boardconfig[x_new][y_new] != player and boardconfig[x_new][y_new] != 0)  ):
				boardconfig[x_new][y_new] = 0
				x_new -= 1
				y_new -= 1

		if x_new > x_current and y_new < y_current:
			x_new += 1
			y_new -= 1
			while ( x_new<= 4 and  y_new>= 0 and (boardconfig[x_new][y_new] != player and boardconfig[x_new][y_new] != 0) ):
				boardconfig[x_new][y_new] = 0
				x_new += 1
				y_new -= 1

	elif check[x_new][y_new] == 2:
		if x_new > x_current and y_new == y_current:
			x_current -= 1
			while (x_current>= 0 and (boardconfig[x_current][y_current] != player and boardconfig[x_current][y_current] != 0) ):
				boardconfig[x_current][y_current] = 0
				x_current -= 1
		
		if x_new < x_current and y_new == y_current:
			x_current += 1
			while (x_current<= 4 and (boardconfig[x_current][y_current] != player and boardconfig[x_current][y_current] != 0) ):
				boardconfig[x_current][y_current] = 0
				x_current += 1

		if x_new == x_current and y_new > y_current:
			y_current -= 1
			while (y_current>= 0 and (boardconfig[x_current][y_current] != player and boardconfig[x_current][y_current] != 0) ):
				boardconfig[x_current][y_current] = 0
				y_current -= 1

		if x_new == x_current and y_new < y_current:
			y_current += 1
			while (y_current<= 8 and (boardconfig[x_current][y_current] != player and boardconfig[x_current][y_current] != 0) ):
				boardconfig[x_current][y_current] = 0
				y_current += 1

		if x_new > x_current and y_new > y_current:
			x_current -= 1
			y_current -= 1
			while ( x_current>= 0 and  y_current>= 0 and (boardconfig[x_current][y_current] != player and boardconfig[x_current][y_current] != 0)  ):
				boardconfig[x_current][y_current] = 0
				x_current -= 1
				y_current -= 1

		if x_new < x_current and y_new > y_current:
			x_current += 1
			y_current -= 1
			while ( x_current<= 4 and  y_current>= 0  and (boardconfig[x_current][y_current] != player and boardconfig[x_current][y_current] != 0) ):
				boardconfig[x_current][y_current] = 0
				x_current += 1
				y_current -= 1

		if x_new < x_current and y_new < y_current:
			x_current += 1
			y_current += 1
			while (x_current<= 4 and  y_current<= 8 and (boardconfig[x_current][y_current] != player and boardconfig[x_current][y_current] != 0)  ):
				boardconfig[x_current][y_current] = 0
				x_current += 1
				y_current += 1

		if x_new > x_current and y_new < y_current:
			x_current -= 1
			y_current += 1
			while ( x_current>= 0 and  y_new<= 8 and (boardconfig[x_current][y_current] != player and boardconfig[x_current][y_current] != 0)  ):
				boardconfig[x_current][y_current] = 0
				x_current -= 1
				y_current += 1


def capture_possible(x, y, player): # (x,y) are coordinates
	local_capture=0
	if x>=1:
		if boardconfig[x-1][y] == 0: 
			if x>=2  and (boardconfig[x-2][y] != player and boardconfig[x-2][y] != 0):
				local_capture = 1
			if x<=3:
				if boardconfig[x+1][y] != player and boardconfig[x+1][y] != 0:
					local_capture = 1
	if x<=3:
		if boardconfig[x+1][y] == 0: 
			if x<=2 and (boardconfig[x+2][y] != player and boardconfig[x+2][y] != 0):
				local_capture = 1 
			if x>=1: 
				if boardconfig[x-1][y] != player and boardconfig[x-1][y] != 0:
					local_capture = 1 
	if y>=1:
		if boardconfig[x][y-1] == 0: 
			if y>=2 and (boardconfig[x][y-2] != player and boardconfig[x][y-2] != 0):
				local_capture = 1
			if y<=7:
				if boardconfig[x][y+1] != player and boardconfig[x][y+1] != 0:
					local_capture = 1 
	if y<=7:
		if boardconfig[x][y+1] == 0: 
			if y<=6 and (boardconfig[x][y+2] != player and boardconfig[x][y+2] != 0):
				local_capture = 1
			if y>=1:
				if boardconfig[x][y-1] != player and boardconfig[x][y-1] != 0:
					local_capture = 1 
	if (x+y)%2 == 0:
		if x>=1 and y>=1:
			if boardconfig[x-1][y-1] == 0: 
				if x>=2  and  y>=2  and (boardconfig[x-2][y-2] != player and boardconfig[x-2][y-2] != 0):
					local_capture = 1 
				if x<=3  and  y<=7:
					if boardconfig[x+1][y+1] != player and boardconfig[x+1][y+1] != 0:
						local_capture = 1 
		if x>=1 and y<=7:
			if boardconfig[x-1][y+1] == 0: 
				if x>=2  and  y<=6  and (boardconfig[x-2][y+2] != player and boardconfig[x-2][y+2] != 0):
					local_capture = 1 
				if x<=3  and  y>=1:
					if boardconfig[x+1][y-1] != player and boardconfig[x+1][y-1] != 0:
						local_capture = 1 
		if x<=3 and y<=7:
			if boardconfig[x+1][y+1] == 0: 
				if x<=2  and  y<=6  and (boardconfig[x+2][y+2] != player and boardconfig[x+2][y+2] != 0):
					local_capture = 1 
				if x>=1  and  y>=1:
					if boardconfig[x-1][y-1] != player and boardconfig[x-1][y-1] != 0:
						local_capture = 1 
		if x<=3 and y>=1:
			if boardconfig[x+1][y-1] == 0: 
				if x<=2  and  y>=2  and (boardconfig[x+2][y-2] != player and boardconfig[x+2][y-2] != 0):
					local_capture = 1 
				if x>=1  and  y<=7:
					if boardconfig[x-1][y+1] != player and boardconfig[x-1][y+1] != 0:
						local_capture = 1
	return local_capture
	
def valid_moves(x, y, player): # (x,y) are coordinates
	global move_list_length
	global move_list_length_withdraw
	move_list_length = 0
	move_list_length_withdraw =0
	global capture
	capture = 0
	global move_list_x
	global move_list_y
	global move_list_x_withdraw
	global move_list_y_withdraw
	global check
	check = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
	move_list_x =[0, 0, 0, 0, 0, 0, 0, 0]
	move_list_y =[0, 0, 0, 0, 0, 0, 0, 0]
	move_list_x_withdraw =[0, 0, 0, 0, 0, 0, 0, 0]
	move_list_y_withdraw =[0, 0, 0, 0, 0, 0, 0, 0]
	if x>=1:
		if boardconfig[x-1][y] == 0: 
			if x>=2  and (boardconfig[x-2][y] != player and boardconfig[x-2][y] != 0):
				capture = 1 
				move_list_x[move_list_length] = x-1
				move_list_y[move_list_length] = y
				move_list_length+=1
			if x<=3:
				if boardconfig[x+1][y] != player and boardconfig[x+1][y] != 0:
					capture = 1 
					move_list_x_withdraw[move_list_length_withdraw] = x-1
					move_list_y_withdraw[move_list_length_withdraw] = y   
					move_list_length_withdraw+=1

	if x<=3:
		if boardconfig[x+1][y] == 0: 
			if x<=2 and (boardconfig[x+2][y] != player and boardconfig[x+2][y] != 0):
				capture = 1 
				move_list_x[move_list_length] = x+1
				move_list_y[move_list_length] = y
				move_list_length+=1
			if x>=1: 
				if boardconfig[x-1][y] != player and boardconfig[x-1][y] != 0:
					capture = 1 
					move_list_x_withdraw[move_list_length_withdraw] = x+1
					move_list_y_withdraw[move_list_length_withdraw] = y
					move_list_length_withdraw+=1
			
	if y>=1:
		if boardconfig[x][y-1] == 0: 
			if y>=2 and (boardconfig[x][y-2] != player and boardconfig[x][y-2] != 0):
				capture = 1
				move_list_x[move_list_length] = x
				move_list_y[move_list_length] = y-1
				move_list_length+=1
			if y<=7:
				if boardconfig[x][y+1] != player and boardconfig[x][y+1] != 0:
					capture = 1 
					move_list_x_withdraw[move_list_length_withdraw] = x
					move_list_y_withdraw[move_list_length_withdraw] = y-1
					move_list_length_withdraw+=1
	if y<=7:
		if boardconfig[x][y+1] == 0: 
			if y<=6 and (boardconfig[x][y+2] != player and boardconfig[x][y+2] != 0):
				capture = 1
				move_list_x[move_list_length] = x
				move_list_y[move_list_length] = y+1
				move_list_length+=1
			if y>=1:
				if boardconfig[x][y-1] != player and boardconfig[x][y-1] != 0:
					capture = 1 
					move_list_x_withdraw[move_list_length_withdraw] = x
					move_list_y_withdraw[move_list_length_withdraw] = y+1
					move_list_length_withdraw+=1

	if (x+y)%2 == 0:
		if x>=1 and y>=1:
			if boardconfig[x-1][y-1] == 0: 
				if x>=2  and  y>=2  and (boardconfig[x-2][y-2] != player and boardconfig[x-2][y-2] != 0):
					capture = 1 
					move_list_x[move_list_length] = x-1
					move_list_y[move_list_length] = y-1
					move_list_length+=1
				if x<=3  and  y<=7:
					if boardconfig[x+1][y+1] != player and boardconfig[x+1][y+1] != 0:
						capture = 1 
						move_list_x_withdraw[move_list_length_withdraw] = x-1
						move_list_y_withdraw[move_list_length_withdraw] = y-1
						move_list_length_withdraw+=1
		
		if x>=1 and y<=7:
			if boardconfig[x-1][y+1] == 0: 
				if x>=2  and  y<=6  and (boardconfig[x-2][y+2] != player and boardconfig[x-2][y+2] != 0):
					capture = 1 
					move_list_x[move_list_length] = x-1
					move_list_y[move_list_length] = y+1
					move_list_length+=1
				if x<=3  and  y>=1:
					if boardconfig[x+1][y-1] != player and boardconfig[x+1][y-1] != 0:
						capture = 1 
						move_list_x_withdraw[move_list_length_withdraw] = x-1
						move_list_y_withdraw[move_list_length_withdraw] = y+1
						move_list_length_withdraw+=1
		
		if x<=3 and y<=7:
			if boardconfig[x+1][y+1] == 0: 
				if x<=2  and  y<=6  and (boardconfig[x+2][y+2] != player and boardconfig[x+2][y+2] != 0):
					capture = 1 
					move_list_x[move_list_length] = x+1
					move_list_y[move_list_length] = y+1
					move_list_length+=1
				if x>=1  and  y>=1:
					if boardconfig[x-1][y-1] != player and boardconfig[x-1][y-1] != 0:
						capture = 1 
						move_list_x_withdraw[move_list_length_withdraw] = x+1
						move_list_y_withdraw[move_list_length_withdraw] = y+1
						move_list_length_withdraw+=1
		
		if x<=3 and y>=1:
			if boardconfig[x+1][y-1] == 0: 
				if x<=2  and  y>=2  and (boardconfig[x+2][y-2] != player and boardconfig[x+2][y-2] != 0):
					capture = 1 
					move_list_x[move_list_length] = x+1
					move_list_y[move_list_length] = y-1
					move_list_length+=1
				if x>=1  and  y<=7:
					if boardconfig[x-1][y+1] != player and boardconfig[x-1][y+1] != 0:
						capture = 1 
						move_list_x_withdraw[move_list_length_withdraw] = x+1
						move_list_y_withdraw[move_list_length_withdraw] = y-1
						move_list_length_withdraw+=1
	
	cappos=0

	for i in range(0, 5):
		for j in range(0, 9):
			if boardconfig[i][j]==player:
				if capture_possible(i, j, player)==1:
					cappos=1
					break

	if cappos == 0:
		if x>=1:
			if boardconfig[x-1][y] == 0: 
				move_list_x[move_list_length] = x-1
				move_list_y[move_list_length] = y
				move_list_length+=1

		if x<=3:
			if boardconfig[x+1][y] == 0: 
				move_list_x[move_list_length] = x+1
				move_list_y[move_list_length] = y
				move_list_length+=1
				
		if y>=1:
			if boardconfig[x][y-1] == 0: 
				move_list_x[move_list_length] = x
				move_list_y[move_list_length] = y-1
				move_list_length+=1
		if y<=6:
			if boardconfig[x][y+1] == 0: 
				move_list_x[move_list_length] = x
				move_list_y[move_list_length] = y+1
				move_list_length+=1

		if (x+y)%2 == 0:
			if x>=1 and y>=1:
				if boardconfig[x-1][y-1] == 0:  
					move_list_x[move_list_length] = x-1
					move_list_y[move_list_length] = y-1           
					move_list_length+=1
			if x>=1 and y<=7:
				if boardconfig[x-1][y+1] == 0: 
					move_list_x[move_list_length] = x-1
					move_list_y[move_list_length] = y+1
					move_list_length+=1
			
			if x<=3 and y<=7:
				if boardconfig[x+1][y+1] == 0: 
					move_list_x[move_list_length] = x+1
					move_list_y[move_list_length] = y+1
					move_list_length+=1
			if x<=3 and y>=1:
				if boardconfig[x+1][y-1] == 0:  
					move_list_x[move_list_length] = x+1
					move_list_y[move_list_length] = y-1
					move_list_length+=1
	return


def getscore(x_current,y_current,x_new,y_new, player): # check is 1 for toward-capture and 2 for withdraw capture
	global boardconfig
	global check
	score=0
	if check[x_new][y_new] == 1:
		if x_new > x_current and y_new == y_current:
			x_new += 1
			while ( x_new <= 4 and (boardconfig[x_new][y_new] != player and boardconfig[x_new][y_new] != 0) ):
				score+=1
				x_new += 1
		
		if x_new < x_current and y_new == y_current:
			x_new -= 1
			while (x_new >= 0 and (boardconfig[x_new][y_new] != player and boardconfig[x_new][y_new] != 0) ):
				score+=1
				x_new -= 1

		if x_new == x_current and y_new > y_current:
			y_new += 1
			while ( y_new<= 8 and (boardconfig[x_new][y_new] != player and boardconfig[x_new][y_new] != 0) ):
				score+=1
				y_new += 1

		if x_new == x_current and y_new < y_current:
			y_new -= 1
			while ( y_new>= 0 and (boardconfig[x_new][y_new] != player and boardconfig[x_new][y_new] != 0)):
				score+=1
				y_new -= 1

		if x_new > x_current and y_new > y_current:
			x_new += 1
			y_new += 1
			while ( x_new<= 4 and  y_new<= 8 and (boardconfig[x_new][y_new] != player and boardconfig[x_new][y_new] != 0)  ):
				score+=1
				x_new += 1
				y_new += 1

		if x_new < x_current and y_new > y_current:
			x_new -= 1
			y_new += 1
			while (x_new>= 0 and  y_new<= 8 and (boardconfig[x_new][y_new] != player and boardconfig[x_new][y_new] != 0)  ):
				score+=1
				x_new -= 1
				y_new += 1

		if x_new < x_current and y_new < y_current:
			x_new -= 1
			y_new-= 1
			while ( x_new>= 0 and  y_new>= 0 and (boardconfig[x_new][y_new] != player and boardconfig[x_new][y_new] != 0)  ):
				score+=1
				x_new -= 1
				y_new -= 1

		if x_new > x_current and y_new < y_current:
			x_new += 1
			y_new -= 1
			while ( x_new<= 4 and  y_new>= 0 and (boardconfig[x_new][y_new] != player and boardconfig[x_new][y_new] != 0) ):
				score+=1
				x_new += 1
				y_new -= 1

	elif check[x_new][y_new] == 2:
		if x_new > x_current and y_new == y_current:
			x_current -= 1
			while (x_current>= 0 and (boardconfig[x_current][y_current] != player and boardconfig[x_current][y_current] != 0) ):
				score+=1
				x_current -= 1
		
		if x_new < x_current and y_new == y_current:
			x_current += 1
			while (x_current<= 4 and (boardconfig[x_current][y_current] != player and boardconfig[x_current][y_current] != 0) ):
				score+=1
				x_current += 1

		if x_new == x_current and y_new > y_current:
			y_current -= 1
			while (y_current>= 0 and (boardconfig[x_current][y_current] != player and boardconfig[x_current][y_current] != 0) ):
				score+=1
				y_current -= 1

		if x_new == x_current and y_new < y_current:
			y_current += 1
			while (y_current<= 8 and (boardconfig[x_current][y_current] != player and boardconfig[x_current][y_current] != 0) ):
				score+=1
				y_current += 1

		if x_new > x_current and y_new > y_current:
			x_current -= 1
			y_current -= 1
			while ( x_current>= 0 and  y_current>= 0 and (boardconfig[x_current][y_current] != player and boardconfig[x_current][y_current] != 0)  ):
				score+=1
				x_current -= 1
				y_current -= 1

		if x_new < x_current and y_new > y_current:
			x_current += 1
			y_current -= 1
			while ( x_current<= 4 and  y_current>= 0  and (boardconfig[x_current][y_current] != player and boardconfig[x_current][y_current] != 0) ):
				score+=1
				x_current += 1
				y_current -= 1

		if x_new < x_current and y_new < y_current:
			x_current += 1
			y_current += 1
			while (x_current<= 4 and  y_current<= 8 and (boardconfig[x_current][y_current] != player and boardconfig[x_current][y_current] != 0)  ):
				score+=1
				x_current += 1
				y_current += 1

		if x_new > x_current and y_new < y_current:
			x_current -= 1
			y_current += 1
			while ( x_current>= 0 and  y_new<= 8 and (boardconfig[x_current][y_current] != player and boardconfig[x_current][y_current] != 0)  ):
				score+=1
				x_current -= 1
				y_current += 1
	return score


def temp_valid_moves(x, y, player): # (x,y) are coordinates
	global boardconfig
	global MouseReleased
	global check
	global capture
	check = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
	mlist = 0
	mlist_wd =0
	capture = 0
	movx =[0, 0, 0, 0, 0, 0, 0, 0]
	movy =[0, 0, 0, 0, 0, 0, 0, 0]
	movx_wd =[0, 0, 0, 0, 0, 0, 0, 0]
	movy_wd =[0, 0, 0, 0, 0, 0, 0, 0]
	if x>=1:
		if boardconfig[x-1][y] == 0:
			if x>=2  and (boardconfig[x-2][y] != player and boardconfig[x-2][y] != 0):
				capture = 1
				movx[mlist] = x-1
				movy[mlist] = y
				mlist+=1
			if x<=3:
				if (boardconfig[x+1][y] != player) and (boardconfig[x+1][y] != 0):
					capture = 1 
					movx_wd[mlist_wd] = x-1
					movy_wd[mlist_wd] = y   
					mlist_wd+=1

	if x<=3:
		if boardconfig[x+1][y] == 0: 
			if x<=2 and (boardconfig[x+2][y] != player and boardconfig[x+2][y] != 0):
				capture = 1 
				movx[mlist] = x+1
				movy[mlist] = y
				mlist+=1
			if x>=1: 
				if boardconfig[x-1][y] != player and boardconfig[x-1][y] != 0:
					capture = 1 
					movx_wd[mlist_wd] = x+1
					movy_wd[mlist_wd] = y
					mlist_wd+=1
			
	if y>=1:
		if boardconfig[x][y-1] == 0: 
			if y>=2 and (boardconfig[x][y-2] != player and boardconfig[x][y-2] != 0):
				capture = 1
				movx[mlist] = x
				movy[mlist] = y-1
				mlist+=1
			if y<=7:
				if boardconfig[x][y+1] != player and boardconfig[x][y+1] != 0:
					capture = 1 
					movx_wd[mlist_wd] = x
					movy_wd[mlist_wd] = y-1
					mlist_wd+=1
	if y<=7:
		if boardconfig[x][y+1] == 0: 
			if y<=6 and (boardconfig[x][y+2] != player and boardconfig[x][y+2] != 0):
				capture = 1
				movx[mlist] = x
				movy[mlist] = y+1
				mlist+=1
			if y>=1:
				if boardconfig[x][y-1] != player and boardconfig[x][y-1] != 0:
					capture = 1 
					movx_wd[mlist_wd] = x
					movy_wd[mlist_wd] = y+1
					mlist_wd+=1

	if (x+y)%2 == 0:
		if x>=1 and y>=1:
			if boardconfig[x-1][y-1] == 0: 
				if x>=2  and  y>=2  and (boardconfig[x-2][y-2] != player and boardconfig[x-2][y-2] != 0):
					capture = 1 
					movx[mlist] = x-1
					movy[mlist] = y-1
					mlist+=1
				if x<=3  and  y<=7:
					if boardconfig[x+1][y+1] != player and boardconfig[x+1][y+1] != 0:
						capture = 1 
						movx_wd[mlist_wd] = x-1
						movy_wd[mlist_wd] = y-1
						mlist_wd+=1
		
		if x>=1 and y<=7:
			if boardconfig[x-1][y+1] == 0: 
				if x>=2  and  y<=6  and (boardconfig[x-2][y+2] != player and boardconfig[x-2][y+2] != 0):
					capture = 1 
					movx[mlist] = x-1
					movy[mlist] = y+1
					mlist+=1
				if x<=3  and  y>=1:
					if boardconfig[x+1][y-1] != player and boardconfig[x+1][y-1] != 0:
						capture = 1 
						movx_wd[mlist_wd] = x-1
						movy_wd[mlist_wd] = y+1
						mlist_wd+=1
		
		if x<=3 and y<=7:
			if boardconfig[x+1][y+1] == 0: 
				if x<=2  and  y<=6  and (boardconfig[x+2][y+2] != player and boardconfig[x+2][y+2] != 0):
					capture = 1 
					movx[mlist] = x+1
					movy[mlist] = y+1
					mlist+=1
				if x>=1  and  y>=1:
					if boardconfig[x-1][y-1] != player and boardconfig[x-1][y-1] != 0:
						capture = 1 
						movx_wd[mlist_wd] = x+1
						movy_wd[mlist_wd] = y+1
						mlist_wd+=1
		
		if x<=3 and y>=1:
			if boardconfig[x+1][y-1] == 0: 
				if x<=2  and  y>=2  and (boardconfig[x+2][y-2] != player and boardconfig[x+2][y-2] != 0):
					capture = 1 
					movx[mlist] = x+1
					movy[mlist] = y-1
					mlist+=1
				if x>=1  and  y<=7:
					if boardconfig[x-1][y+1] != player and boardconfig[x-1][y+1] != 0:
						capture = 1 
						movx_wd[mlist_wd] = x+1
						movy_wd[mlist_wd] = y-1
						mlist_wd+=1
	
	cappos=0

	for i in range(0, 5):
		for j in range(0, 9):
			if boardconfig[i][j]==player:
				if capture_possible(i, j, player)==1:
					cappos=1
					break

	if cappos == 0:
		if x>=1:
			if boardconfig[x-1][y] == 0: 
				movx[mlist] = x-1
				movy[mlist] = y
				mlist+=1

		if x<=3:
			if boardconfig[x+1][y] == 0: 
				movx[mlist] = x+1
				movy[mlist] = y
				mlist+=1
				
		if y>=1:
			if boardconfig[x][y-1] == 0: 
				movx[mlist] = x
				movy[mlist] = y-1
				mlist+=1
		if y<=6:
			if boardconfig[x][y+1] == 0: 
				movx[mlist] = x
				movy[mlist] = y+1
				mlist+=1

		if (x+y)%2 == 0:
			if x>=1 and y>=1:
				if boardconfig[x-1][y-1] == 0:  
					movx[mlist] = x-1
					movy[mlist] = y-1           
					mlist+=1
			if x>=1 and y<=7:
				if boardconfig[x-1][y+1] == 0: 
					movx[mlist] = x-1
					movy[mlist] = y+1
					mlist+=1
			
			if x<=3 and y<=7:
				if boardconfig[x+1][y+1] == 0: 
					movx[mlist] = x+1
					movy[mlist] = y+1
					mlist+=1
			if x<=3 and y>=1:
				if boardconfig[x+1][y-1] == 0:  
					movx[mlist] = x+1
					movy[mlist] = y-1
					mlist+=1

	max_score=0
	new_x=0
	new_y=0
	

	for i in range(0, mlist):
		check[movx[i]][movy[i]]=1
	for i in range(0, mlist_wd):
		check[movx_wd[i]][movy_wd[i]]=2

	for i in range(0, mlist):
		if getscore(x, y, movx[i], movy[i], player) >= max_score:
			max_score=getscore(x, y, movx[i], movy[i], player)
			new_x=movx[i]
			new_y=movy[i]
	for i in range(0, mlist_wd):
		if getscore(x, y, movx_wd[i], movy_wd[i], player) > max_score:
			max_score=getscore(x, y, movx_wd[i], movy_wd[i], player)
			new_x=movx[i]
			new_y=movy[i]

	a=[]
	a.append(max_score)
	a.append(x)
	a.append(y)
	a.append(new_x)
	a.append(new_y)
	return a

def best_move(player):
	global RenderList
	global move
	move=[0,0,0,0,0]
	for i in range(0, 5):
		for j in range(0, 9):
			if boardconfig[i][j]==player:
				tmove=temp_valid_moves(i, j, player)
				if tmove[0]>=move[0]:
					move[0]=tmove[0]
					move[1]=tmove[1]
					move[2]=tmove[2]
					move[3]=tmove[3]
					move[4]=tmove[4]


background_image = pygame.image.load("board.jpg")
background_image = pygame.transform.scale(background_image, (1366,768))
backgroundRect = background_image.get_rect()
screen=pygame.display.set_mode((1366,768))
screen.blit(background_image, backgroundRect)
pc = pygame.image.load("PC.png")
human = pygame.image.load("Human.png")
Fanorona = pygame.image.load("Fanorona.png")
WhoPlays = 0

while WhoPlays==0:
	MouseReleased=False
	pos=pygame.mouse.get_pos()
	for Event in pygame.event.get():
		if Event.type == pygame.QUIT:
			exit()
		if Event.type == pygame.MOUSEBUTTONUP:
			MouseReleased=True
			MouseDown=False
	
	if MouseReleased==True:
		if pos[0]>=382 and pos[0]<=678 and pos[1]>=100 and pos[1]<=358:
			WhoPlays=1
		if pos[0]>=382 and pos[0]<=678 and pos[1]>=398 and pos[1]<=556:
			WhoPlays=2

	screen.blit(background_image, backgroundRect)
	screen.blit(Fanorona, (555, 20))
	screen.blit(pc, (530, 200))
	screen.blit(human, (530, 400))
	pygame.display.flip()

def main():
	global player
	global capture
	global check
	global checkbatao
	global apwd
	global MouseReleased
	global RenderList
	background_image = pygame.image.load("board (copy)1.png")
	background_image = pygame.transform.scale(background_image, (1366,768))
	backgroundRect = background_image.get_rect()
	screen=pygame.display.set_mode((1366,768))
	screen.blit(background_image, backgroundRect)
	running=True
	MousePressed=False # Pressed down THIS FRAME
	MouseDown=False # mouse is held down
	MouseReleased=False # Released THIS FRAME

	############################         INITIAL CONFIG        ###############################
	
	#ROW 1
	
	RenderList.append(DarkDisk(screen, 179, 128))
	RenderList.append(DarkDisk(screen, 304, 128))
	RenderList.append(DarkDisk(screen, 428, 128))
	RenderList.append(DarkDisk(screen, 551, 128))
	RenderList.append(DarkDisk(screen, 675, 128))
	RenderList.append(DarkDisk(screen, 800, 128))
	RenderList.append(DarkDisk(screen, 924, 128))
	RenderList.append(DarkDisk(screen, 1048, 128))
	RenderList.append(DarkDisk(screen, 1172, 128))

	#ROW 2

	RenderList.append(DarkDisk(screen, 179, 253))
	RenderList.append(DarkDisk(screen, 304, 253))
	RenderList.append(DarkDisk(screen, 428, 253))
	RenderList.append(DarkDisk(screen, 551, 253))
	RenderList.append(DarkDisk(screen, 675, 253))
	RenderList.append(DarkDisk(screen, 800, 253))
	RenderList.append(DarkDisk(screen, 924, 253))
	RenderList.append(DarkDisk(screen, 1048, 253))
	RenderList.append(DarkDisk(screen, 1172, 253))

	#ROW 3
	
	RenderList.append(DarkDisk(screen, 179, 382))
	RenderList.append(LightDisk(screen, 304, 382))
	RenderList.append(DarkDisk(screen, 428, 382))
	RenderList.append(LightDisk(screen, 551, 382))
	RenderList.append(Blank(screen, 675, 382))
	RenderList.append(DarkDisk(screen, 800, 382))
	RenderList.append(LightDisk(screen, 924, 382))
	RenderList.append(DarkDisk(screen, 1048, 382))
	RenderList.append(LightDisk(screen, 1172, 382))

	#ROW 4

	RenderList.append(LightDisk(screen, 179, 512))
	RenderList.append(LightDisk(screen, 304, 512))
	RenderList.append(LightDisk(screen, 428, 512))
	RenderList.append(LightDisk(screen, 551, 512))
	RenderList.append(LightDisk(screen, 675, 512))
	RenderList.append(LightDisk(screen, 800, 512))
	RenderList.append(LightDisk(screen, 924, 512))
	RenderList.append(LightDisk(screen, 1048, 512))
	RenderList.append(LightDisk(screen, 1172, 512))

	#ROW 5

	RenderList.append(LightDisk(screen, 179, 640))
	RenderList.append(LightDisk(screen, 304, 640))
	RenderList.append(LightDisk(screen, 428, 640))
	RenderList.append(LightDisk(screen, 551, 640))
	RenderList.append(LightDisk(screen, 675, 640))
	RenderList.append(LightDisk(screen, 800, 640))
	RenderList.append(LightDisk(screen, 924, 640))
	RenderList.append(LightDisk(screen, 1048, 640))
	RenderList.append(LightDisk(screen, 1172, 640))


	Target=None
	Selected=False
	############################         GAME LOOP        ###############################
	while running:
		screen.fill((0,0,0)) # clear screen
		pos=pygame.mouse.get_pos()

		LightCount = 0
		DarkCount = 0
		Winner = 0

		for i in range(0, 5):
			for j in range(0,9):
				if boardconfig[i][j]==1:
					LightCount+=1
		for i in range(0, 5):
			for j in range(0,9):
				if boardconfig[i][j]==2:
					DarkCount+=1

		if LightCount==0:
			player=3
			Winner=2
		elif DarkCount==0:
			player=3
			Winner=1

		for i in range(0, 5):
			for j in range(0,9):
				if boardconfig[i][j]==0:
					temp=RenderList[(i*9)+j]
					RenderList=list(RenderList)
					RenderList[(i*9)+j]=Blank(screen, temp.pos[0], temp.pos[1])

		for Event in pygame.event.get():
			if Event.type == pygame.QUIT:
				running=False
				break
			
			if Event.type == pygame.MOUSEBUTTONDOWN:
				MousePressed=True 
				MouseDown=True 
			   
			if Event.type == pygame.MOUSEBUTTONUP:
				MouseReleased=True
				MouseDown=False

		if WhoPlays==1 and player==2:
			best_move(player)
			coins_to_kill((move[1]), (move[2]), (move[3]), (move[4]), player)
			boardconfig[move[3]][move[4]] = boardconfig[move[1]][move[2]]
			boardconfig[move[1]][move[2]]=0
			RenderList[(move[3]*9)+move[4]].pos, RenderList[(move[1]*9)+move[2]].pos = RenderList[(move[1]*9)+move[2]].pos, RenderList[(move[3]*9)+move[4]].pos
			RenderList[(move[3]*9)+move[4]], RenderList[(move[1]*9)+move[2]] = RenderList[(move[1]*9)+move[2]], RenderList[(move[3]*9)+move[4]]
			Selected=False
			MouseReleased=False
			if capture==0:
				if player==1:
					player=2
				else:
					player=1
		i+=1

		if MouseReleased==True and Selected==True:
			i=0
			for item in RenderList: # search all items on board
				zabardasticheck=0
				if (i/9) in move_list_x:
					if (i%9) in move_list_y:
						zabardasticheck=1
				if (i/9) in move_list_x_withdraw:
					if (i%9) in move_list_y_withdraw:
						zabardasticheck=1

				if pos[0]>=(item.pos[0]-30) and pos[0]<=(item.pos[0]+30) and pos[1]>=(item.pos[1]-30) and pos[1]<=(item.pos[1]+30) and boardconfig[i/9][i%9]==0 and zabardasticheck==1: # window for mouse movement
					temp=0
					for it in RenderList:
						if it==Target:
							break
						temp+=1
					if check[i/9][i%9]==3:
						checkbatao = 0
						while(checkbatao==0):
							
							apwd = 0
							choice = Tkinter.Tk()
							def approach():
								global apwd
								global checkbatao
								apwd+=1
								checkbatao+=1
								choice.destroy()
							def withdraw():
								global apwd
								global checkbatao
								apwd+=2
								checkbatao+=1
								choice.destroy()
							ap = Tkinter.Button (choice, text = "Approach Capture", command = approach)
							wd = Tkinter.Button (choice, text = "Withdraw Capture", command = withdraw)
							ap.pack()
							wd.pack()
							choice.mainloop()
						check[i/9][i%9]=apwd

					coins_to_kill((temp/9), (temp%9), (i/9), (i%9), player)
					boardconfig[i/9][i%9] = boardconfig[temp/9][temp%9]
					boardconfig[temp/9][temp%9]=0
					Target.pos, item.pos = item.pos, Target.pos
					RenderList[i], RenderList[temp] = RenderList[temp], RenderList[i]
					Selected=False
					MouseReleased=False
					if capture==0:
						if player==1:
							player=2
						else:
							player=1
					break
				i+=1


		if MouseReleased==True:
			i=0
			for item in RenderList: # search all items on board
				if (pos[0]>=(item.pos[0]-30) and pos[0]<=(item.pos[0]+30) and pos[1]>=(item.pos[1]-30) and pos[1]<=(item.pos[1]+30) and boardconfig[i/9][i%9]==player): # window for mouse movement
					check = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
					Target=item
					Selected=True
					valid_moves((i/9), (i%9), player)
					for i in range(0, move_list_length):
						check[(move_list_x[i])][(move_list_y[i])]+=1
					for i in range(0, move_list_length_withdraw):
						check[(move_list_x_withdraw[i])][(move_list_y_withdraw[i])]+=2
					break
				i+=1

		screen.blit(background_image, backgroundRect)

		for item in RenderList:
			item.Render(screen) # Draw all items

		if Selected==True:
			ring = pygame.image.load("green_ring.png")
			ring = pygame.transform.scale(ring, (73,73))
			aring = pygame.image.load("appr_move.png")
			aring = pygame.transform.scale(aring, (73,73))
			wring = pygame.image.load("with_move.png")
			wring = pygame.transform.scale(wring, (73,73))
			awring = pygame.image.load("withappr.png")
			awring = pygame.transform.scale(awring, (73,73))
			screen.blit(ring, (Target.pos[0]-37, Target.pos[1]-37))
			for i in range(0, 5):
				for j in range(0,9):
					if check[i][j]==1:
						screen.blit(aring, (RenderList[(i*9)+j].pos[0]-37, RenderList[(i*9)+j].pos[1]-37))
			for i in range(0, 5):
				for j in range(0,9):
					if check[i][j]==2:
						screen.blit(wring, (RenderList[(i*9)+j].pos[0]-37, RenderList[(i*9)+j].pos[1]-37))
			for i in range(0, 5):
				for j in range(0,9):
					if check[i][j]==3:
						screen.blit(awring, (RenderList[(i*9)+j].pos[0]-37, RenderList[(i*9)+j].pos[1]-37))

		if Winner==1:
			pwin = pygame.image.load("pwin.png")
			screen.blit(pwin, (550, 10))
		if Winner==2:
			pwin = pygame.image.load("2pwin.png")
			screen.blit(pwin, (550, 10))

		if player==1:
			play = pygame.image.load("p1.png")
			screen.blit(play, (550, 10))
		elif player==2:
			play = pygame.image.load("p2.png")
			screen.blit(play, (550, 10))

		MousePressed=False # Reset these to False
		MouseReleased=False
		pygame.display.flip()
	return
	
if __name__ == '__main__':
	main()