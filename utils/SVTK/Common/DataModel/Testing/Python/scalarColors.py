#!/usr/bin/env python
import svtk
from svtk.util.misc import svtkGetDataRoot
SVTK_DATA_ROOT = svtkGetDataRoot()

# Color points with scalars
# get the interactor ui
ren1 = svtk.svtkRenderer()
renWin = svtk.svtkRenderWindow()
renWin.AddRenderer(ren1)
iren = svtk.svtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)
# create some points with scalars
colors = svtk.svtkUnsignedCharArray()
colors.SetName("Colors")
colors.SetNumberOfComponents(3)
colors.SetNumberOfTuples(3)
colors.InsertComponent(0,0,255)
colors.InsertComponent(0,1,99)
colors.InsertComponent(0,2,71)
colors.InsertComponent(1,0,125)
colors.InsertComponent(1,1,255)
colors.InsertComponent(1,2,0)
colors.InsertComponent(2,0,226)
colors.InsertComponent(2,1,207)
colors.InsertComponent(2,2,87)
sizes = svtk.svtkUnsignedCharArray()
sizes.SetName("Sizes")
sizes.SetNumberOfComponents(1)
sizes.SetNumberOfTuples(3)
sizes.SetValue(0,1)
sizes.SetValue(1,2)
sizes.SetValue(2,3)
polyVertexPoints = svtk.svtkPoints()
polyVertexPoints.SetNumberOfPoints(3)
polyVertexPoints.InsertPoint(0,0.0,0.0,0.0)
polyVertexPoints.InsertPoint(1,2.5,0.0,0.0)
polyVertexPoints.InsertPoint(2,5.0,0.0,0.0)
aPolyVertex = svtk.svtkPolyVertex()
aPolyVertex.GetPointIds().SetNumberOfIds(3)
aPolyVertex.GetPointIds().SetId(0,0)
aPolyVertex.GetPointIds().SetId(1,1)
aPolyVertex.GetPointIds().SetId(2,2)
aPolyVertexGrid = svtk.svtkUnstructuredGrid()
aPolyVertexGrid.Allocate(1,1)
aPolyVertexGrid.InsertNextCell(aPolyVertex.GetCellType(),aPolyVertex.GetPointIds())
aPolyVertexGrid.SetPoints(polyVertexPoints)
aPolyVertexGrid.GetPointData().SetScalars(sizes)
aPolyVertexGrid.GetPointData().AddArray(colors)
sphere = svtk.svtkSphereSource()
sphere.SetRadius(1.0)
sphere.Update()
glyphs = svtk.svtkGlyph3D()
glyphs.ScalingOn()
glyphs.SetColorModeToColorByScalar()
glyphs.SetScaleModeToScaleByScalar()
glyphs.SetScaleFactor(1)
glyphs.SetInputData(aPolyVertexGrid)
glyphs.SetSourceConnection(sphere.GetOutputPort())
glyphs.SetInputArrayToProcess(0,0,0,0,"Sizes")
glyphs.SetInputArrayToProcess(3,0,0,0,"Colors")
#puts [ glyphs GetScaleModeAsString]
glyphsMapper = svtk.svtkDataSetMapper()
glyphsMapper.SetInputConnection(glyphs.GetOutputPort())
glyphsActor = svtk.svtkActor()
glyphsActor.SetMapper(glyphsMapper)
glyphsActor.GetProperty().BackfaceCullingOn()
ren1.SetBackground(.1,.2,.4)
ren1.AddActor(glyphsActor)
glyphsActor.GetProperty().SetDiffuseColor(1,1,1)
ren1.ResetCamera()
ren1.GetActiveCamera().Azimuth(30)
ren1.GetActiveCamera().Elevation(20)
ren1.GetActiveCamera().Dolly(1.25)
ren1.ResetCameraClippingRange()
renWin.Render()
# render the image
#
iren.Initialize()
# --- end of script --