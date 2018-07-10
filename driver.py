#neeraj varshney (2014A7PS0103P)
from final_program import *
import time
import copy
a=(int)(input("\nOption 1: Display the room environment\nOption 2: Find the path (action sequence) and path cost using T1\nOption 3: Find the path (action sequence) and path cost using T2\nOption 4: Show all results and graphs in the GUI.\n"))
if(a>4 or a<0):
	print("invalid input")
	exit();
p=(int)(input("Enter the dirt percentage: "))
if(p>100 or p<0):
	print("invalid dirty cell percentage")
	exit();
if(a==1):
	
	initialize()
	new_grid=dirt_generator(p)
	new_grid2=copy.deepcopy(new_grid)
	draw_grid(new_grid)
	
	initialize_informed(new_grid2)
	draw_grid(new_grid2)
	
	turtle.exitonclick()
if(a==2):
	initialize()
	new_grid=dirt_generator(p)
	new_grid2=copy.deepcopy(new_grid)
	draw_grid(new_grid)
	
	initial_time=time.time()
	answer2=uninformed(0,0,0,p,1)
	final_time=time.time()
	no_of_calls=give_no_of_calls_uninformed()
	node_size=give_size_of_node(0)
	write_analysis(2*answer2+p,final_time-initial_time,no_of_calls,node_size,1)
	
	turtle.exitonclick()

if(a==3):
	initialize()
	new_grid=dirt_generator(p)
	new_grid2=copy.deepcopy(new_grid)
	
	initialize_informed(new_grid2)
	draw_grid(new_grid2)
	initial_time=time.time()
	
	answer2=func(p,new_grid2,1)
	final_time=time.time()
	no_of_calls=give_no_of_calls()
	node_size=give_size_of_node(1)
	
	write_analysis(2*answer2+p,final_time-initial_time,no_of_calls,node_size,0)
	
	turtle.exitonclick()

if(a==4):
	initialize()
	new_grid=dirt_generator(p)
	new_grid2=copy.deepcopy(new_grid)
	draw_grid(new_grid)
	
	initial_time=time.time()
	answer2=uninformed(0,0,0,p,1)
	final_time=time.time()
	no_of_calls=give_no_of_calls_uninformed()
	node_size=give_size_of_node(0)
	memory_un=node_size*no_of_calls
	write_analysis(2*answer2+p,final_time-initial_time,no_of_calls,node_size,1)
	
	
	initialize_informed(new_grid2)
	draw_grid(new_grid2)
	initial_time=time.time()
	
	answer2=func(p,new_grid2,1)
	final_time=time.time()
	no_of_calls=give_no_of_calls()
	node_size=give_size_of_node(1)
	memory_in=node_size*no_of_calls
	write_analysis(2*answer2+p,final_time-initial_time,no_of_calls,node_size,0)
	write_analysis(0,0,0,0,2)
	comparision_module(memory_un,memory_in)
	
	turtle.exitonclick()