width, height = (300, 300)
centerX, centerY = (width//2, height//2)
zoomFactor = 1/2
scale = 0
if(width > height):
    scale = height * zoomFactor
else:
    scale = width * zoomFactor