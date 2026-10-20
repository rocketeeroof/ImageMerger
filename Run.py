'''
The premise:
* Take any two images and merge them into one, with arbitrary settings.
'''
from PIL import Image
import numpy as np
import copy
from CustomMerge import mergeFunc
import sys

class image():
    def __init__(self, ref):
        # Initialize the image based on parameters
        img = Image.open(ref)
        width, height = img.size
        self.resolution = [width, height]
        ref = np.asarray(img)
        self.resolution = [ref.shape[1], ref.shape[0]]
        self.pixels = ref.tolist()

    def merge(self, otherImg, func):
        for y in range(self.resolution[1]):
            for x in range(self.resolution[0]):
                new_px = mergeFunc(x, y, self.pixels[y][x], otherImg.pixels[y][x])
                self.pixels[y][x] = new_px
    
    def save_image(self, name):
        '''
        Saves the result, always uses 3 channels.

        If there are fewer than 3 channels, it adds new empty ones until there are 3.

        If there are more than 3 channels, it removes the 4th one and those after.
        '''
        to_save = copy.deepcopy(self.pixels)
        # Add extra channels to make the image "saveable"
        channel_length = len(self.pixels[0][0])
        if channel_length < 3:
            for i in range(3 - channel_length):
                for y in range(self.resolution[1]):
                    for x in range(self.resolution[0]):
                        to_save[y][x].append(0)
        # Reduce to 3 channels to make the image "saveable"
        for y in range(self.resolution[1]):
            for x in range(self.resolution[0]):
                to_save[y][x] = to_save[y][x][:3]
        # Save the image
        array_np = np.array(to_save, dtype=np.uint8)
        Image.fromarray(array_np).save(name + ".png")

def merge(ref1, ref2):
    img1 = image(ref1)
    img2 = image(ref2)
    if img1.resolution[0] == img2.resolution[0] and img1.resolution[1] == img2.resolution[1]:
        # Merging
        img1.merge(img2, mergeFunc)
        img1.save_image("Results/result.png")
    else:
        raise IndexError("Both images have different resolutions!")
# Run
usedArgs = sys.argv[1:]
for i in range(2 - len(usedArgs)):
    usedArgs.append(input("Add another image to complete the merge: "))
merge(usedArgs[0], usedArgs[1])