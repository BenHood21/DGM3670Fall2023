import maya.cmds as cmds


def changeColor(*args):
    for sel in sels:
        cmds.setAttr(sel + ".overrideEnabled ", 1)
        cmds.setAttr(sel + ".overrideColor", color)

window = cmds.window(title='Change Color of NURBS')

cmds.rowColumnLayout(numberOfColumns=2,  columnWidth=[(10, 100), (10, 250)])
cmds.text(    label="BLACK = 1, GREY = 3, DARK RED = 4, DARK BLUE = 5 \n"
          "BLUE = 6, DARK GREEN = 7, DARK PURPLE = 8 \n"
          "HOT PINK = 9, BROWN = 10, DARK BROWN = 11 \n"
          "BRIGHT RED = 13, NEON GREEN = 14, NAVY BLUE = 15 \n"
          "WHITE = 16, YELLOW = 17, LIGHT BLUE = 18, TURQUOISE = 19 \n"
          "LIGHT BROWN =  21, PURPLE = 30")
cmds.separator()
color = cmds.textField()
cmds.separator()

cmds.button(label='Apply', c=changeColor)

cmds.showWindow()

sels = cmds.ls(type='nurbsCurve')