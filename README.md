# c2wy3dm
Model converter for Wineyard3d (wy3dm)

This Python script <b>c2wy3dm.py</b> converts Wavefront .obj file to Wineyard3d model .wy3dm file.


The following geometry options should be used when exporting .obj file (using Blender, for example):

Check:
- Triangulate faces
- Write normals
- Include UVs

Uncheck:
- Write materials

<b>Usage</b>: <code class="language-plaintext highlighter-rouge">python3 ./c2wy3dm.py inputFile.obj [outputWy3dmFile]</code>

If argument <i>outputWy3dmFile</i> is not provided, then the output file is set to "<i>inputFile.obj.wy3dm</i>"
