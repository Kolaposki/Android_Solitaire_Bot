import os

class GameVals:
    cards = {}
    sliced_cards = {}
    borders = []

    # Variables related to screen size
    ScreenSize = "FullScreen"
    imageFolderName = 'Images'

    def __init__(self, width, height):
        # Original resolution the coordinates were based on
        original_width = 720
        original_height = 1600

        # Scale factor
        width_ratio = width / original_width
        height_ratio = height / original_height

        if self.ScreenSize == "FullScreen":            
            #self.imageFolderName = 'FullScreenImages'
            self.imageFolderName = 'MobileImages'

            ### For Android
            self.drawDeckArea = [
                int(410 * width_ratio), int(90 * height_ratio),
                int(715 * width_ratio), int(250 * height_ratio)
            ]
            self.deckArea = [
                int(7 * width_ratio), int(90 * height_ratio),
                int(410 * width_ratio), int(250 * height_ratio)
            ]
            self.columnsStart = int(5 * width_ratio)
            self.columnsStartH = int(250 * height_ratio)
            self.columnsEndH = int(1000 * height_ratio)
            self.columnWidth = int(108 * width_ratio)
            self.columnOffset = int(100 * width_ratio)
            self.cardcenterXoffset = int(25 * width_ratio)
            self.cardcenterYoffset = int(25 * height_ratio)

            ### For desktop
            # self.drawDeckArea = [330, 70, 750, 300]
            # self.deckArea = [850, 70, 1600, 300]
            # self.columnsStart = 325
            # self.columnsStartH = 325
            # self.columnsEndH = 1050
            # self.columnWidth = 175
            # self.columnOffset = 182
            # self.cardcenterXoffset = 25
            # self.cardcenterYoffset = 25

        for i in range(1,5):
            borderName = 'border' + str(i) + '.png'
            self.borders.append(borderName)
        
        for i in range(1,14):
            for ch in ['c','d','h','s']:
                card = ch+str(i) 
                cardpath = os.path.join(os.getcwd(), self.imageFolderName, card + '.png') 
                sliceCardPath = os.path.join(os.getcwd(), self.imageFolderName, 'Slices', card + '.png') 
                self.cards[card] = cardpath     
                self.sliced_cards[card] = sliceCardPath
