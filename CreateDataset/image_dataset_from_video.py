# Save sreenshots from a video as image 
# Good if you need random images as dataset in your projects 

import matplotlib.pyplot as plt 
import imageio
import os

imageio.plugins.ffmpeg.download() # download ffmpeg plugin if not already present
filename = raw_input(" Enter path to video : ") # path to video
assert os.path.exists(filename), "I did not find the file at, "+str(filename)
vid = imageio.get_reader(filename,  'ffmpeg')

frame_interval = input("Enter frame interval : ")

len = vid.get_length()
print len

for i in range(0, len):
	if(i%frame_interval == 0):
		image = vid.get_data(i)
		fig = plt.figure()
		fig.suptitle('image #{}'.format(i), fontsize=10)
		plt.axis('off')
		plt.imshow(image)
		plt.savefig('img_' +str(i)+'.png')
	else:
		continue;
# pylab.show()
