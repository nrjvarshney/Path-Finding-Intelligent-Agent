#neeraj varshney (2014A7PS0103P)
from random import randint
import copy
import sys
import turtle
import time
# grid 10 X 10
# grid=np.zeros((10,10),dtype=int)
grid = [[0 for i in range(10)] for j in range(10)]
# visited=np.zeros((10,10),dtype=int)
visited = [[0 for i in range(10)] for j in range(10)]

# this function randomly distributes p dirt
def dirt_generator(p):
	for i in range(p):
		flag=1
		while(flag==1):
			row=randint(0, 9)
			col=randint(0, 9)
			if(grid[row][col]==0):
				flag=0;
			grid[row][col]=1
	return grid
# this function prints grid on console
def print_grid(grid):
	# (rows,cols)=grid.shape
	rows=10
	cols=10
	for row in range(rows):
		for col in range(cols):
			if(grid[row][col]==1):
				sys.stdout.write('#')
			else:
				sys.stdout.write('_')
		print("")

# this function initializes grid GUI for uninformed
def initialize():
	global screen
	global my_turtle	
	global window_width,window_height
	
	screen = turtle.Screen()
	window_width=screen.window_width()
	window_height=screen.window_height()
	turtle.setup(1.0, 1.0, startx=window_width/2, starty=window_height/2)
	window_width=screen.window_width()
	window_height=screen.window_height()
	
	turtle.bgcolor("white")
	turtle.title("AUTOMATED Vacuum Cleaner")
	my_turtle = turtle.Turtle()
	my_turtle.shape("turtle")
	my_turtle.speed(0)
	my_turtle.penup()
	my_turtle.backward(window_width/4)
	my_turtle.pendown()
	my_turtle.right(90)
	my_turtle.forward(window_height/2)
	my_turtle.backward(window_height)
	
	my_turtle.left(90)
	my_turtle.penup()
	my_turtle.goto(-1*window_width/4+10,window_height/2-20)
	my_turtle.pendown()
# this function initializes grid GUI for informed
def initialize_informed(new_grid):
	grid=new_grid
	# visited=np.zeros((10,10),dtype=int)
	visited = [[0 for i in range(10)] for j in range(10)]
	my_turtle.penup()
	my_turtle.goto(window_width/6-50,window_height/2-20)
	my_turtle.pendown()
# this function draws grid GUI
def draw_grid(grid):
	
	# my_turtle.color("red")
	
	dot_distance = 50
	width = 10
	height = 10
	for y in range(height):
	    for i in range(width):
	        for i in range(4):
    			
    			my_turtle.forward(dot_distance)
    			my_turtle.right(90)
	        my_turtle.forward(dot_distance)
	    my_turtle.backward(dot_distance * width)
	    my_turtle.right(90)
	    my_turtle.forward(dot_distance)
	    my_turtle.left(90)
	    
	my_turtle.left(90)
	my_turtle.forward(dot_distance*height)
	my_turtle.right(90)
	
	(rows,cols)=(10,10)
	
	for row in range(rows):
		for col in range(cols):
			if(grid[row][col]==1):
				my_turtle.penup()
				my_turtle.color("grey")
				my_turtle.forward(9)
				my_turtle.right(90)
				my_turtle.forward(25)
				my_turtle.pendown()
				my_turtle.begin_fill()
				my_turtle.circle(15)
				my_turtle.end_fill()
				my_turtle.penup()
				my_turtle.backward(25)
				my_turtle.left(90)
				my_turtle.backward(9)
				
			my_turtle.forward(dot_distance)
		my_turtle.backward(dot_distance * width)
		my_turtle.right(90)
		my_turtle.forward(dot_distance)
		my_turtle.left(90)
	        	
	my_turtle.left(90)
	my_turtle.forward(dot_distance*height)
	my_turtle.right(90)
	
	my_turtle.forward(dot_distance/2)
	my_turtle.right(90)
	
	my_turtle.forward(dot_distance/2)
	my_turtle.left(90)
	my_turtle.color("black")
	
	my_turtle.pendown()

def check_goal_state(count,initial):
	if(count==1):
		return 1;
	return 0;
def distance(row1,col1,row2,col2):
	downd=row2-row1;
	rightd=col2-col1;
	return abs(row1-row2)+abs(col1-col2)
def cal_distance(row1,col1,row2,col2):
	downd=row2-row1;
	rightd=col2-col1;
	return downd,rightd;
def draw_circle():
	my_turtle.color("blue")
	my_turtle.backward(16)
	my_turtle.right(90)
	my_turtle.pendown()
	my_turtle.begin_fill()
	my_turtle.circle(15)
	my_turtle.end_fill()
	my_turtle.penup()
	my_turtle.left(90)
	my_turtle.forward(16)

def move_turtle(prevrow,prevcol,newrow,newcol):
	if(newcol==prevcol):
		if(newrow>prevrow):
			my_turtle.right(90)
			my_turtle.forward((newrow-prevrow)*50)
			# my_turtle.dot()
			
			my_turtle.penup()
			if(grid[newrow][newcol]==1):
				draw_circle()
				# my_turtle.color("red")
			my_turtle.pendown()
			my_turtle.left(90)
		else:
			my_turtle.left(90)
			my_turtle.forward((prevrow-newrow)*50)
			# my_turtle.dot()
			
			my_turtle.penup()
			if(grid[newrow][newcol]==1):
				draw_circle()
				# my_turtle.color("red")
			my_turtle.pendown()		
			my_turtle.right(90)
		return;
	if(newcol>prevcol):
		my_turtle.forward((newcol-prevcol)*50)
		if(newrow==prevrow):
			# my_turtle.dot()

			my_turtle.penup()
			if(grid[newrow][newcol]==1):
				draw_circle()
				# my_turtle.color("red")
			my_turtle.pendown()		
			return;
		if(newrow>prevrow):
			my_turtle.right(90)
			my_turtle.forward((newrow-prevrow)*50)
			# my_turtle.dot()

			my_turtle.penup()
			if(grid[newrow][newcol]==1):
				draw_circle()
				# my_turtle.color("red")
			my_turtle.pendown()		
			my_turtle.left(90)
		else:
			my_turtle.left(90)
			my_turtle.forward((prevrow-newrow)*50)
			# my_turtle.dot()

			my_turtle.penup()
			if(grid[newrow][newcol]==1):
				draw_circle()
				# my_turtle.color("red")
			my_turtle.pendown()		
			my_turtle.right(90)
	else:
		my_turtle.backward((prevcol-newcol)*50)
		if(newrow==prevrow):
			# my_turtle.dot()

			my_turtle.penup()
			if(grid[newrow][newcol]==1):
				draw_circle()
				# my_turtle.color("red")
			my_turtle.pendown()		
		
			return;
		if(newrow>prevrow):
			my_turtle.right(90)
			my_turtle.forward((newrow-prevrow)*50)
			# my_turtle.dot()

			my_turtle.penup()
			if(grid[newrow][newcol]==1):
				draw_circle()
				# my_turtle.color("red")
			my_turtle.pendown()		
		
			my_turtle.left(90)
		else:
			my_turtle.left(90)
			my_turtle.forward((prevrow-newrow)*50)
			# my_turtle.dot()

			my_turtle.penup()
			if(grid[newrow][newcol]==1):
				draw_circle()
			my_turtle.pendown()
			my_turtle.right(90)

def to_be_added_to_goal_state(startx,starty,move):
	answer_temp=0;
	if(10-startx<=5):# go down else go up
		if(10-starty<=5):
			answer_temp+=9-startx+9-starty;# BR
			if(move==1):
				move_turtle(startx,starty,9,9)
		else:
			answer_temp+=9-startx+starty #DL
			if(move==1):
				move_turtle(startx,starty,9,0)
	else:
		if(10-starty<=5):
			answer_temp+=startx+9-starty;# TR
			if(move==1):
				move_turtle(startx,starty,0,9)
		else:
			answer_temp+=startx+starty #TL
			if(move==1):
				move_turtle(startx,starty,0,0)
	
	return answer_temp;
def check_validity(curr_row,curr_col):
	if(curr_col>=0 and curr_col<=9 and curr_row>=0 and curr_row<=9 and visited[curr_row][curr_col]==0):
		return 1;
	return 0;

answer=0

no_of_recursive_calls=0
no_of_recursive_calls_uninformed=0
startx=0
starty=0
node_size_uninformed=0
node_size_informed=0
def node_at_depth(curr_row,curr_col,d,move):
	global answer
	global no_of_recursive_calls
	global node_size_informed
	node_size_informed=sys.getsizeof(curr_row)+sys.getsizeof(curr_col)+sys.getsizeof(d)
	no_of_recursive_calls+=1
	if(d==0):
		if(grid[curr_row][curr_col]==1):
			global startx
			global starty
			answer+=distance(startx,starty,curr_row,curr_col)
			if(move==1):
				my_turtle.color("green")
				move_turtle(startx,starty,curr_row,curr_col)
			startx=curr_row
			starty=curr_col
			grid[startx][starty]=0;
			return 1;
		return 0;
	else:

		if(check_validity(curr_row,curr_col-1)==1):
			if(node_at_depth(curr_row,curr_col-1,d-1,move)==1):
				return 1;
		if(check_validity(curr_row,curr_col+1)==1):
			if(node_at_depth(curr_row,curr_col+1,d-1,move)==1):
				return 1;
		if(check_validity(curr_row-1,curr_col)==1):
			if(node_at_depth(curr_row-1,curr_col,d-1,move)==1):
				return 1;
		if(check_validity(curr_row+1,curr_col)==1):
			if(node_at_depth(curr_row+1,curr_col,d-1,move)==1):
				return 1;
		
		return 0;

def func(initial,new_grid,move):
	global grid,visited
	grid=new_grid
	# visited=np.zeros((10,10),dtype=int)
	visited = [[0 for i in range(10)] for j in range(10)]
	count=0;
	global startx
	global starty
	global answer
	answer=0
	my_turtle.color("green")
	while(count!=initial):
		
		print(startx,starty)
		depth=0
		found=0
		while(found==0):
			if(node_at_depth(startx,starty,depth,move)==1):
				found=1
				count+=1
			else:
				depth+=1
	print(startx,starty)
	answer+=to_be_added_to_goal_state(startx,starty,move)
	my_turtle.color("black")
	
	return answer;

def move_turtle_on_analysis():
	my_turtle.penup()
	my_turtle.right(90)
	my_turtle.forward(30)
	my_turtle.left(90)
	my_turtle.pendown()

def write_analysis(answer2,time_taken,no_of_calls,node_size,uninformed):
	my_turtle.penup()
	my_turtle.color("black")
	if(uninformed==1):
		my_turtle.goto(-1*window_width/2+10,window_height/2-50)
		my_turtle.pendown()
		my_turtle.write("ANALYSIS MODULE for T1", move=False, align="left", font=("Arial", 10, "normal"))
	
		move_turtle_on_analysis()
		my_turtle.write("number of nodes generated = "+str(no_of_calls), move=False, align="left", font=("Arial", 8, "normal"))
		move_turtle_on_analysis()
		my_turtle.write("memory allocated to 1 node = "+str(node_size), move=False, align="left", font=("Arial", 8, "normal"))
		move_turtle_on_analysis()

		my_turtle.write("max growth of stack = "+str(no_of_calls*node_size), move=False, align="left", font=("Arial", 8, "normal"))
		move_turtle_on_analysis()
		my_turtle.write("cost to clean  = "+str(answer2), move=False, align="left", font=("Arial", 8, "normal"))
		
		move_turtle_on_analysis()
		my_turtle.write("time to complete path = "+str(time_taken), move=False, align="left", font=("Arial", 8, "normal"))
		my_turtle.penup()
	
	if(uninformed==0):
		my_turtle.goto(-1*window_width/2+10,window_height/4-60)
		my_turtle.pendown()
		my_turtle.write("ANALYSIS MODULE for T2", move=False, align="left", font=("Arial", 8, "normal"))
	
		move_turtle_on_analysis()
		my_turtle.write("number of nodes generated = "+str(no_of_calls), move=False, align="left", font=("Arial", 8, "normal"))
		
		move_turtle_on_analysis()
		my_turtle.write("memory allocated to 1 node = "+str(node_size), move=False, align="left", font=("Arial", 8, "normal"))
		move_turtle_on_analysis()
		my_turtle.write("max growth of stack = "+str(no_of_calls*node_size), move=False, align="left", font=("Arial", 8, "normal"))
		move_turtle_on_analysis()
		my_turtle.write("cost to clean  = "+str(answer2), move=False, align="left", font=("Arial", 8, "normal"))
		
		move_turtle_on_analysis()
		my_turtle.write("time to complete path = "+str(time_taken), move=False, align="left", font=("Arial", 8, "normal"))
		my_turtle.penup()

	if(uninformed==2):# comparision
		my_turtle.goto(-1*window_width/2+10,-150)
		my_turtle.pendown()
		my_turtle.write("COMPARITIVE ANALYSIS(uninformed : informed)", move=False, align="left", font=("Arial", 10, "normal"))
	
		move_turtle_on_analysis()
		my_turtle.write("memory used = "+str(no_of_calls), move=False, align="left", font=("Arial", 10, "normal"))
	
def comparision_module(memory_unin,memory_in):
	my_turtle.write("memory used = "+str(memory_unin)+" : "+str(memory_in), move=False, align="left", font=("Arial", 10, "normal"))
	move_turtle_on_analysis()
	my_turtle.write("computing...", move=False, align="left", font=("Arial", 10, "normal"))
	move_turtle_on_analysis()
	(a,b,dirts)=average_path_cost()
	my_turtle.write("average path cost on dirt percentage "+str(dirts), move=False, align="left", font=("Arial", 10, "normal"))
	move_turtle_on_analysis()
	my_turtle.write(""+str(sum(a)/float(len(a))-83)+" : "+str(sum(b)/float(len(b))), move=False, align="left", font=("Arial", 10, "normal"))
	move_turtle_on_analysis()

def average_path_cost():
	cost_uninformed=[];
	cost_informed=[];
	num=10
	dirts=[]
	for i in range(num):
		p=randint(70, 99)
		dirts.append(p)
		new_grid=dirt_generator(p)
		new_grid2=copy.deepcopy(new_grid)
		cost_uninformed.append(2*uninformed(0,0,0,p,0)+p)
		cost_informed.append(2*func(p,new_grid2,0)+p)
	return cost_uninformed,cost_informed,dirts

def give_no_of_calls():
	return no_of_recursive_calls

old_x=0;
old_y=0;
dfs_cost=0;

def dfs(curr_row,curr_col,curr_cost,no_of_dirt_left,move):
	global node_size_uninformed
	node_size_uninformed=sys.getsizeof(curr_row)+sys.getsizeof(curr_col)+sys.getsizeof(curr_cost)+sys.getsizeof(no_of_dirt_left)
	global no_of_recursive_calls_uninformed
	no_of_recursive_calls_uninformed+=1
	global old_x,old_y,dfs_cost
	if(move==1):
		my_turtle.color("red")
		move_turtle(old_x,old_y,curr_row,curr_col);
	old_x=curr_row
	old_y=curr_col
	visited[curr_row][curr_col]=1
	if(no_of_dirt_left==1):
		if(check_validity(curr_row+1,curr_col)==1 and grid[curr_row+1][curr_col]==1):
			if(dfs(curr_row+1,curr_col,curr_cost+1,no_of_dirt_left,move)==1):
				return 1;
	if(grid[curr_row][curr_col]==1):
		grid[curr_row][curr_col]=0
		no_of_dirt_left-=1
		
		if(no_of_dirt_left==0):
			# print(curr_cost,curr_row,curr_col)
			dfs_cost=curr_cost
			dfs_cost+=to_be_added_to_goal_state(old_x,old_y,move)
			return 1;
	if(no_of_dirt_left>0):
		if(check_validity(curr_row,curr_col-1)==1):
			if(dfs(curr_row,curr_col-1,curr_cost+1,no_of_dirt_left,move)==1):
				return 1;
		if(check_validity(curr_row-1,curr_col)==1):
			if(dfs(curr_row-1,curr_col,curr_cost+1,no_of_dirt_left,move)==1):
				return 1;
		if(check_validity(curr_row,curr_col+1)==1):
			if(dfs(curr_row,curr_col+1,curr_cost+1,no_of_dirt_left,move)==1):
				return 1;
		if(check_validity(curr_row+1,curr_col)==1):
			if(dfs(curr_row+1,curr_col,curr_cost+1,no_of_dirt_left,move)==1):
				return 1;
	return 0;
def uninformed(curr_row,curr_col,curr_cost,no_of_dirt_left,move):
	my_turtle.color("red")
	if(no_of_dirt_left==0):
		return 0;
	global dfs_cost
	dfs_cost=0
	if(dfs(curr_row,curr_col,curr_cost,no_of_dirt_left,move)==1):
		return dfs_cost	
	my_turtle.color("black")
	return dfs_cost;
def give_no_of_calls_uninformed():
	return no_of_recursive_calls_uninformed
def give_size_of_node(var):
	global node_size_uninformed,node_size_informed
	if(var==0):
		return node_size_uninformed;
	else:
		return node_size_informed