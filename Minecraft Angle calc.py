import math


#Set the angle and length to what you want
LENGTH = 100
ANGLE = 30

#returns a coordinate list of blocks in the angle/length requested
def generate_Blocklist():
    blocklist = []
    angle = ANGLE
    length = LENGTH
    blockWidth = int(round(round((math.cos( math.radians(angle)) * length),2)))
    blockHeight = int(round(round((math.sin( math.radians(angle)) * length),2)))
    #print(blockWidth)
    #print(blockHeight)

    for xpos in range(0,blockWidth):
        ypos = int(give_Line_YPos(xpos,blockWidth,blockHeight))
        blocklist.append([xpos,ypos])
    #print(blocklist)
    return blocklist

#returns a list of the number of blocks (for each y level) you need to place
def generate_Placement_list(blocklist):
        placementlist = []
        blocklevel = blocklist[0][1]
        blockcounter = 0
        for i in blocklist:
            
            if(i[1] == blocklevel):
                blockcounter +=1
            else:
                placementlist.append(blockcounter) 
                blocklevel = i[1]
                blockcounter = 1
        print(placementlist)
        print(len(placementlist))

def give_Line_YPos(xpos,blockWidth,blockHeight):
        slope = blockHeight/blockWidth

        ypos = xpos * slope

        return ypos
    


generate_Placement_list(generate_Blocklist())
