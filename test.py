def valid_moves(x, y, player): # (x,y) are coordinates
	mlen = 0
	mlen_wd =0
	capture = 0
	global check
	check = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
	movx =[0, 0, 0, 0, 0, 0, 0, 0]
	movy =[0, 0, 0, 0, 0, 0, 0, 0]
	movx_wd =[0, 0, 0, 0, 0, 0, 0, 0]
	movy_wd =[0, 0, 0, 0, 0, 0, 0, 0]
	if x>=1:
		if boardconfig[x-1][y] == 0: 
			if x>=2  and (boardconfig[x-2][y] != player and boardconfig[x-2][y] != 0):
				capture = 1 
				movx[mlen] = x-1
				movy[mlen] = y
				mlen+=1
			if x<=3:
				if boardconfig[x+1][y] != player and boardconfig[x+1][y] != 0:
					capture = 1 
					movx_wd[mlen_wd] = x-1
					movy_wd[mlen_wd] = y   
					mlen_wd+=1

	if x<=3:
		if boardconfig[x+1][y] == 0: 
			if x<=2 and (boardconfig[x+2][y] != player and boardconfig[x+2][y] != 0):
				capture = 1 
				movx[mlen] = x+1
				movy[mlen] = y
				mlen+=1
			if x>=1: 
				if boardconfig[x-1][y] != player and boardconfig[x-1][y] != 0:
					capture = 1 
					movx_wd[mlen_wd] = x+1
					movy_wd[mlen_wd] = y
					mlen_wd+=1
			
	if y>=1:
		if boardconfig[x][y-1] == 0: 
			if y>=2 and (boardconfig[x][y-2] != player and boardconfig[x][y-2] != 0):
				capture = 1
				movx[mlen] = x
				movy[mlen] = y-1
				mlen+=1
			if y<=7:
				if boardconfig[x][y+1] != player and boardconfig[x][y+1] != 0:
					capture = 1 
					movx_wd[mlen_wd] = x
					movy_wd[mlen_wd] = y-1
					mlen_wd+=1
	if y<=7:
		if boardconfig[x][y+1] == 0: 
			if y<=6 and (boardconfig[x][y+2] != player and boardconfig[x][y+2] != 0):
				capture = 1
				movx[mlen] = x
				movy[mlen] = y+1
				mlen+=1
			if y>=1:
				if boardconfig[x][y-1] != player and boardconfig[x][y-1] != 0:
					capture = 1 
					movx_wd[mlen_wd] = x
					movy_wd[mlen_wd] = y+1
					mlen_wd+=1

	if (x+y)%2 == 0:
		if x>=1 and y>=1:
			if boardconfig[x-1][y-1] == 0: 
				if x>=2  and  y>=2  and (boardconfig[x-2][y-2] != player and boardconfig[x-2][y-2] != 0):
					capture = 1 
					movx[mlen] = x-1
					movy[mlen] = y-1
					mlen+=1
				if x<=3  and  y<=7:
					if boardconfig[x+1][y+1] != player and boardconfig[x+1][y+1] != 0:
						capture = 1 
						movx_wd[mlen_wd] = x-1
						movy_wd[mlen_wd] = y-1
						mlen_wd+=1
		
		if x>=1 and y<=7:
			if boardconfig[x-1][y+1] == 0: 
				if x>=2  and  y<=6  and (boardconfig[x-2][y+2] != player and boardconfig[x-2][y+2] != 0):
					capture = 1 
					movx[mlen] = x-1
					movy[mlen] = y+1
					mlen+=1
				if x<=3  and  y>=1:
					if boardconfig[x+1][y-1] != player and boardconfig[x+1][y-1] != 0:
						capture = 1 
						movx_wd[mlen_wd] = x-1
						movy_wd[mlen_wd] = y+1
						mlen_wd+=1
		
		if x<=3 and y<=7:
			if boardconfig[x+1][y+1] == 0: 
				if x<=2  and  y<=6  and (boardconfig[x+2][y+2] != player and boardconfig[x+2][y+2] != 0):
					capture = 1 
					movx[mlen] = x+1
					movy[mlen] = y+1
					mlen+=1
				if x>=1  and  y>=1:
					if boardconfig[x-1][y-1] != player and boardconfig[x-1][y-1] != 0:
						capture = 1 
						movx_wd[mlen_wd] = x+1
						movy_wd[mlen_wd] = y+1
						mlen_wd+=1
		
		if x<=3 and y>=1:
			if boardconfig[x+1][y-1] == 0: 
				if x<=2  and  y>=2  and (boardconfig[x+2][y-2] != player and boardconfig[x+2][y-2] != 0):
					capture = 1 
					movx[mlen] = x+1
					movy[mlen] = y-1
					mlen+=1
				if x>=1  and  y<=7:
					if boardconfig[x-1][y+1] != player and boardconfig[x-1][y+1] != 0:
						capture = 1 
						movx_wd[mlen_wd] = x+1
						movy_wd[mlen_wd] = y-1
						mlen_wd+=1
	
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
				movx[mlen] = x-1
				movy[mlen] = y
				mlen+=1

		if x<=3:
			if boardconfig[x+1][y] == 0: 
				movx[mlen] = x+1
				movy[mlen] = y
				mlen+=1
				
		if y>=1:
			if boardconfig[x][y-1] == 0: 
				movx[mlen] = x
				movy[mlen] = y-1
				mlen+=1
		if y<=6:
			if boardconfig[x][y+1] == 0: 
				movx[mlen] = x
				movy[mlen] = y+1
				mlen+=1

		if (x+y)%2 == 0:
			if x>=1 and y>=1:
				if boardconfig[x-1][y-1] == 0:  
					movx[mlen] = x-1
					movy[mlen] = y-1           
					mlen+=1
			if x>=1 and y<=7:
				if boardconfig[x-1][y+1] == 0: 
					movx[mlen] = x-1
					movy[mlen] = y+1
					mlen+=1
			
			if x<=3 and y<=7:
				if boardconfig[x+1][y+1] == 0: 
					movx[mlen] = x+1
					movy[mlen] = y+1
					mlen+=1
			if x<=3 and y>=1:
				if boardconfig[x+1][y-1] == 0:  
					movx[mlen] = x+1
					movy[mlen] = y-1
					mlen+=1
	return