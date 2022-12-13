import maya.cmds as cmds


def renameObject(*args):
    count = 1
    selsList = cmds.ls(sl=True)


    if len(selsList)<1:
        print("Choose Object To Rename")
    else:
        for sels in selsList:
            name = (cmds.textField(name_field, q=True, tx=True))
            number = (str(count))
            object = (cmds.textField(object_field, q=True, tx=True))

            newName = (name + "_0" + number + "_" + object)
            print = (newName)

            cmds.rename(sels, newName)
            count += 1


cmds.window(title='Rename Object')
cmds.columnLayout(adj=3)
cmds.text(label='Insert Name', w=300, h=30)
cmds.separator()
name_field = cmds.textField('newName')
cmds.text(label='Insert Object Type', w=300, h=30)
cmds.separator()
object_field = cmds.textField('newObject')
cmds.button(label='Rename', width=300, c=renameObject)

cmds.showWindow()