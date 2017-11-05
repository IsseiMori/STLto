import math
import struct

class Vertex:
	"""docstring for ClassName"""
	x = 0
	y = 0
	z = 0

	def Convert(self):
		self.Homograph()
		self.Viewport()

	def Homograph(self):

		self.x = (camera.z * self.x) / (camera.z - self.z)
		self.y = (camera.z * self.y) / (camera.z - self.z)

	def Viewport(self):
		#original viewport size
		ViewWidth = camera.z * math.tan(math.pi / 8) * 2
		#expand vertex to file viewport size
		self.x = self.x * width / ViewWidth
		self.y = self.y * width / ViewWidth
		#move vertex from original to file viewport
		self.x = width / 2 + self.x
		self.y = width / 2 - self.y

	#a
	def GetFloat(self, s):
		#stl is z axis top
	    self.x = struct.unpack('f',data[s] + data[s+1] + data[s+2] + data[s+3])[0]
	    self.z = struct.unpack('f',data[s+4] + data[s+5] + data[s+6] + data[s+7])[0]
	    self.y = struct.unpack('f',data[s+8] + data[s+9] + data[s+10] + data[s+11])[0]
	    self.y = self.y * -1
	    self.x = self.x * -1


vert = Vertex()

camera = Vertex()
camera.z = -735

width = 500

infile = open('162.stl') #import file
out = open('162.svg', 'w') #export file

data = infile.read()

#write header
out.write('<?xml version="1.0" standalone="no"?>\n<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">\n\n')
out.write("<svg width=\"%s\" height=\"%s\" version=\"1.1\" xmlns=\"http://www.w3.org/2000/svg\">\n" % (width, width))

#count faces
number = data[80] + data[81] + data[82] + data[83] 
faces = struct.unpack('I',number)[0]

for x in range(0,faces):

    out.write("<polygon style=\"fill:none;stroke:#000000;stroke-miterlimit:10;\" points=\"")

    for y in range(0,3):
	    #data[96]~data[107] vertex1
	    vert.GetFloat(96+y*12+x*50)

	    vert.Convert()

	    out.write(str(round(vert.x,2)) + ",")
	    out.write(str(round(vert.y,2)) + ",")

    out.write("\" />\n")


out.write("</svg>")
out.close()
print "end"
