import maya.cmds as cmds


cmds.polySphere(sx=20, sy=20, r=2, n='Head')
cmds.move (0,20,0)
cmds.polySphere(sx=20, sy=20, r=4, n='Chest')
cmds.move (0,15.43,-2.88)
cmds.polySphere(sx=20, sy=20, r=3, n='Pelvis')
cmds.move (0,10.229,-3.314)
cmds.polySphere(sx=20, sy=20, r=2, n='R_Clavical')
cmds.move (-3.406, 17.024, -3.293)
cmds.polySphere(sx=20, sy=20, r=2, n='L_Clavical')
cmds.move (3.406, 17.024, -3.293)
cmds.polySphere(sx=20, sy=20, r=1.75, n='R_Shoulder')
cmds.move (-6.617, 17.621, -4.474)
cmds.polySphere(sx=20, sy=20, r=1.75, n='L_Shoulder')
cmds.move (6.617, 17.621, -4.474)
cmds.polySphere(sx=20, sy=20, r=1.75, n='R_Elbow')
cmds.move (-8.408, 15.413, -2.921)
cmds.polySphere(sx=20, sy=20, r=1.75, n='L_Elbow')
cmds.move (8.408, 15.413, -2.921)
cmds.polySphere(sx=20, sy=20, r=1.75, n='R_Wrist')
cmds.move (-8.663, 13.972, -0.483)
cmds.polySphere(sx=20, sy=20, r=1.75, n='L_Wrist')
cmds.move (8.663, 13.972, -0.483)
cmds.polySphere(sx=20, sy=20, r=1.75, n='R_Hand')
cmds.move (-8.663, 13.972, 3.247)
cmds.polySphere(sx=20, sy=20, r=1.75, n='L_Hand')
cmds.move (8.663, 13.972, 3.247)
cmds.polySphere(sx=20, sy=20, r=2, n='R_Thigh')
cmds.move (-2.912,7.992,-1.994)
cmds.polySphere(sx=20, sy=20, r=2, n='L_Thigh')
cmds.move (2.912,7.992,-1.994)
cmds.polySphere(sx=20, sy=20, r=1.75, n='R_Knee')
cmds.move (-4.71,5.74,0.666)
cmds.polySphere(sx=20, sy=20, r=1.75, n='L_Knee')
cmds.move (4.71,5.74,0.666)
cmds.polySphere(sx=20, sy=20, r=1.25, n='R_Calf')
cmds.move (-3.844,3.277,-0.966)
cmds.polySphere(sx=20, sy=20, r=1.25, n='L_Calf')
cmds.move (3.844,3.277,-0.966)
cmds.polySphere(sx=20, sy=20, r=1, n='R_Ankle')
cmds.move (-3.844,1.724,-1.46)
cmds.polySphere(sx=20, sy=20, r=1, n='L_Ankle')
cmds.move (3.844,1.724,-1.46)
cmds.polySphere(sx=20, sy=20, r=.75, n='R_Heel')
cmds.move (-3.844,0.262,-1.46)
cmds.polySphere(sx=20, sy=20, r=.75, n='L_Heel')
cmds.move (3.844,0.262,-1.46)
cmds.polySphere(sx=20, sy=20, r=.75, n='R_Foot')
cmds.move (-4.096, 0.262, 0.102)
cmds.polySphere(sx=20, sy=20, r=.75, n='L_Foot')
cmds.move (4.096, 0.262, 0.102)
cmds.polySphere(sx=20, sy=20, r=.75, n='R_Toe')
cmds.move (-4.459, 0.262, 1.744)
cmds.polySphere(sx=20, sy=20, r=.75, n='L_Toe')
cmds.move (4.459, 0.262, 1.744)
cmds.polyExtrudeFacet ('Chest.f[80:99]', kft=False, ltz=6, ls=(.5, .5, 0) )
cmds.polyTorus( sx=12, sy=16, r=.5, sr=.1, n='Eye')
cmds.move (-1.4,21,1.5)
cmds.rotate( '90deg', 0, 0, r=True )
cmds.polyMirrorFace( 'Eye', direction=0, mergeMode=1 )
cmds.polyCube( sx=1, sy=1, sz=1, d=5, h=5, w=5)
cmds.move (0,18.6,3.8)
cmds.rotate ('-30deg',0,0, r=True)
cmds.polyBoolOp( 'Head','pCube1', op=2, n='HeadMouth' )
cmds.polyCone( sx=4, sy=1, sz=1, r=.5, h=1, n='Nose')
cmds.move (0,20.96,1.6)
cmds.rotate ('-23deg',0,0, r=True)
cmds.group(' R_Hand','L_Heel','R_Heel','R_Calf','L_Knee','L_Toe','L_Elbow',
          'Pelvis','L_Clavical','L_Foot','L_Thigh','L_Shoulder','R_Clavical',
          'L_Wrist','R_Knee','L_Hand','R_Ankle','Head','R_Shoulder','Chest','R_Elbow',
          'L_Ankle','L_Calf','R_Thigh','R_Wrist','R_Foot','R_Toe','Nose','HeadMouth','Eye', n='SnowmanBody')
cmds.delete(ch=True)
