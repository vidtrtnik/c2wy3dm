import sys
#print ('Number of arguments:', len(sys.argv), 'arguments.')
#print ('Argument List:', str(sys.argv))

if len(sys.argv) < 2:
	print("Usage: python3 c2wy3dm.py [ObjFile] [OutputFile]")
	sys.exit(1)
	
IN=sys.argv[1]

if len(sys.argv) < 3:
	OUT=IN+".wy3dm"
else:
	OUT=sys.argv[2]

print("**Wineyard3D** OBJ to WY3DM converter\n")
print("Input file: " + IN)
print("Output file: " + OUT + "\n")

v = []
vn = []
vt = []
f = []

mx = 0
my = 0
mz = 0

with open(IN, 'r') as file:

	for line in file:
		line = line.replace("\n", "")
		id = line[0:2]
		#print(id)
		
		spl = line[2:].split(" ")
		for s in spl:
			if s:
				if id == "v ":
					v.append(s)
				if id == "vn":
					vn.append(s)
				if id == "vt":
					vt.append(s)
				if id == "f ":
					f.append([s.split("/")[0], s.split("/")[1], s.split("/")[2]])

unpV = []
unpT = []
unpN = []
unpI = []

for i in range(0, len(f), 3):
	print("\rConverting: " + str(int(i*100/len(f))) + "%", end="")
	f1 = f[i]
	f2 = f[i+1]
	f3 = f[i+2]
	
	tmpv = []
	tmpt = []
	tmpn = []
	
	for i in range(0, 3):
		tmpv.append(v[int(int(f1[0])-1)*3+i])
		
	for i in range(0, 3):
		tmpv.append(v[int(int(f2[0])-1)*3+i])
		
	for i in range(0, 3):
		tmpv.append(v[int(int(f3[0])-1)*3+i])
	
	
	
	for i in range(0, 2):
		tmpt.append(vt[int(int(f1[1])-1)*2+i])
		
	for i in range(0, 2):
		tmpt.append(vt[int(int(f2[1])-1)*2+i])
		
	for i in range(0, 2):
		tmpt.append(vt[int(int(f3[1])-1)*2+i])
	
	
	
	
	for i in range(0, 3):
		tmpn.append(vn[int(int(f1[2])-1)*3+i])
		
	for i in range(0, 3):
		tmpn.append(vn[int(int(f2[2])-1)*3+i])
		
	for i in range(0, 3):
		tmpn.append(vn[int(int(f3[2])-1)*3+i])
	
	
	for i in range(0, len(tmpv)):
		unpV.append(tmpv[i])
	
	for i in range(0, len(tmpt)):
		unpT.append(tmpt[i])
	
	for i in range(0, len(tmpn)):
		unpN.append(tmpn[i])
	
	unpI.append(len(unpI))
	unpI.append(len(unpI))
	unpI.append(len(unpI))

print("\rConverting: 100%")

minx = unpV[0]
maxx = unpV[0]
miny = unpV[0]
maxy = unpV[0]
minz = unpV[0]
maxz = unpV[0]
for i in range(0, len(unpV), 3):
    print("\rCalculating bounding box: " + str(int(i*100/len(unpV))) + "%", end="")
    ix = unpV[i+0]
    iy = unpV[i+1]
    iz = unpV[i+2]
    
    if ix > maxx:
        maxx = ix
    if ix < minx:
        minx = ix
    if iy > maxy:
        maxy = iy
    if iy < miny:
        miny = iy
    if iz > maxz:
        maxz = iz
    if iz < minz:
        minz = iz
    
mdx = abs(float(maxx) - float(minx))
mdy = abs(float(maxy) - float(miny))
mdz = abs(float(maxz) - float(minz))
print("\rCalculating bounding box: 100%")

fout = open(OUT, "w")
fout.write("Wineyard3D Model 0.0.1")

print("\rWriting: " + "0%", end="")
fout.write("\n\nv\n")
for i in range(0, len(unpV)):
	fout.write(unpV[i])
	if i < len(unpV)-1:
		fout.write(",")
		
print("\rWriting: " + "25%", end="")
fout.write("\n\ni\n")
for i in range(0, len(unpI)):
	fout.write(str(unpI[i]))
	if i < len(unpI)-1:
		fout.write(",")
		
print("\rWriting: " + "50%", end="")
fout.write("\n\nn\n")
for i in range(0, len(unpN)):
	fout.write(unpN[i])
	if i < len(unpN)-1:
		fout.write(",")

print("\rWriting: " + "75%", end="")		
fout.write("\n\nt\n")
for i in range(0, len(unpT)):
	fout.write(unpT[i])
	if i < len(unpT)-1:
		fout.write(",")

fout.write("\n\nb\n")
fout.write(str(mdx) + "," + str(mdy) + "," + str(mdz));
print("\rWriting: " + "100%\n")		
fout.close()

print("Conversion to WY3DM complete.")
sys.exit(0)