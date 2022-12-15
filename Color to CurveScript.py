import maya.cmds as cmds

cmds.colorEditor()
if cmds.colorEditor(query=True, result=True):
    rGBValues = cmds.colorEditor(query=True, rgb=True)
    # print ('RGB = ' + str(values))
    hSVValues = cmds.colorEditor(query=True, hsv=True)
    # print ('HSV = ' + str(values))
    alpha = cmds.colorEditor(query=True, alpha=True)
# print ('Alpha = ' + str(alpha))
else:
    print('Editor was dismissed')




def colorChanger(values, alpha):
    newColorObj = cmds.ls(sl=True)
    rGBValues = values

    cmds.color(newColorObj, ud=1)
    cmds.color(newColorObj, rgb=(values))
    print(values)
    print(newColorObj)

colorChanger(rGBValues, alpha)


