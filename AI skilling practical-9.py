def hillclimbing (ini_goal,final_goal):
    max1,max2='D','A'
    print("%c \t %c"%(ini_goal,final_goal))
    if final_goal is max1:
        hillclimbing(chr(68),chr(ord('D')-1))
    if final_goal is chr(67):
        hillclimbing(chr(67),chr(ord('C')-1))
    if final_goal is chr(66):
        hillclimbing(chr(66),chr(ord('B')-1))
    hillclimbing('A','D')
