from PIL import Image, ImageOps


class ImageKernel:

    def __init__(self, image, matrix, kernel):
        #self.img = Image.open(str(image))
        self.img = ImageOps.grayscale(Image.open(str(image)))
        self.pixel = self.img.load()
        self.width, self.height = self.img.size
        self.kernelSection1 = kernel[0]
        self.kernelSection2 = kernel[1]
        self.kernelSection3 = kernel[2]
        self.matrix = int(matrix)

        self.Run()

    def Run(self):
        for x in range(self.width + 1):
            for y in range(self.height + 1):
                i = x * self.matrix
                k = y * self.matrix
                self.Process((i,k))



    def Process(self, data):
        self.data_x = data[0]
        self.data_y = data[1]

        self.location1 = (self.data_x - 1, self.data_y)
        self.location2 = (self.data_x - 1, self.data_y - 1)
        self.location3 = (self.data_x, self.data_y - 1)
        self.location4 = (self.data_x + 1, self.data_y - 1)
        self.location5 = (self.data_x + 1, self.data_y)
        self.location6 = (self.data_x + 1, self.data_y + 1)
        self.location7 = (self.data_x, self.data_y + 1)
        self.location8 = (self.data_x - 1, self.data_y + 1)
        self.location9 = (self.data_x, self.data_y)


        try:
            self.data_loc1 = int(self.pixel[self.location1] * int(self.kernelSection1[1]))
            self.data_loc2 = int(self.pixel[self.location2] * int(self.kernelSection1[0]))
            self.data_loc3 = int(self.pixel[self.location3] * int(self.kernelSection2[0]))
            self.data_loc4 = int(self.pixel[self.location4] * int(self.kernelSection3[0]))
            self.data_loc5 = int(self.pixel[self.location5] * int(self.kernelSection3[1]))
            self.data_loc6 = int(self.pixel[self.location6] * int(self.kernelSection3[2]))
            self.data_loc7 = int(self.pixel[self.location7] * int(self.kernelSection2[2]))
            self.data_loc8 = int(self.pixel[self.location8] * int(self.kernelSection1[2]))
            self.data_loc9 = int(self.pixel[self.location9] * int(self.kernelSection2[1]))


            count = int(self.data_loc1 + self.data_loc2 + self.data_loc3 +
                        self.data_loc4 + self.data_loc5 + self.data_loc6 +
                        self.data_loc7 + self.data_loc8 + self.data_loc9)

            self.img.putpixel(self.location1, (count))
            self.img.putpixel(self.location2, (count))
            self.img.putpixel(self.location3, (count))
            self.img.putpixel(self.location4, (count))
            self.img.putpixel(self.location5, (count))
            self.img.putpixel(self.location6, (count))
            self.img.putpixel(self.location7, (count))
            self.img.putpixel(self.location8, (count))
            self.img.putpixel(self.location9, (count))

        except:
            pass


    def show(self):
        self.img.show()



object = ImageKernel(
    "image.jpg",
    3,
    [[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
object.show()
