class Screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value
    @property
    def resolution(self):
        return self._width * self._height

if __name__ =='__main__':
    s = Screen()
    s.width = 750
    print(s.width)
    s.height = 320
    print(s.height)
    print(s.resolution)

