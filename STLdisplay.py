#!/usr/bin/env python3

import vtk
import sys, ntpath

filename = sys.argv[1]

reader = vtk.vtkSTLReader()
reader.SetFileName(filename)

mapper = vtk.vtkPolyDataMapper()
if vtk.VTK_MAJOR_VERSION <= 5:
    mapper.SetInput(reader.GetOutput())
else:
    mapper.SetInputConnection(reader.GetOutputPort())

actor = vtk.vtkActor()
actor.SetMapper(mapper)

# Create a rendering window and renderer
ren = vtk.vtkRenderer()
ren.SetBackground(.1, .2, .3)

renWin = vtk.vtkRenderWindow()

WIDTH=1024
HEIGHT=768
renWin.SetSize(WIDTH,HEIGHT)

renWin.AddRenderer(ren)

# Create a renderwindowinteractor
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

# create a text actor
txt = vtk.vtkTextActor()
txt.SetInput(ntpath.basename(filename))
txtprop=txt.GetTextProperty()
txtprop.SetFontFamilyToArial()
txtprop.SetFontSize(18)
txtprop.SetColor(1,1,1)
txt.SetDisplayPosition(20,30)

# assign actor to the renderer
ren.AddActor(txt)

# Assign actor to the renderer
ren.AddActor(actor)

# Enable user interface interactor
iren.Initialize()
renWin.Render()
iren.Start()
