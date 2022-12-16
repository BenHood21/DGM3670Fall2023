import maya.cmds as cmds
"BLACK = 1, GREY = 3, DARK RED = 4, DARK BLUE = 5 \n"
"BLUE = 6, DARK GREEN = 7, DARK PURPLE = 8 \n"
"HOT PINK = 9, BROWN = 10, DARK BROWN = 11 \n"
"BRIGHT RED = 13, NEON GREEN = 14, NAVY BLUE = 15 \n"
"WHITE = 16, YELLOW = 17, LIGHT BLUE = 18, TURQUOISE = 19 \n"
"LIGHT BROWN =  21, PURPLE = 30"

sels = cmds.ls(type='nurbsCurve')

color = int(input())

for sel in sels:
    cmds.setAttr(sel + ".overrideEnabled ", 1)
    cmds.setAttr(sel + ".overrideColor", color)