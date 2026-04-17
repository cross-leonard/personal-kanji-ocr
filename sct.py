from mss import mss, tools


def sct():
    """ Take sc based on parameters given """
    with mss() as sct:

        # The screen part to capture
        monitor = {"top": 300, "left": 0, "width": 920, "height": 600}
        output = "screenshot.png".format(**monitor)

        # Grab the data
        sct_img = sct.grab(monitor)

        # Save to the picture file
        tools.to_png(sct_img.rgb, sct_img.size, output=output)
        print(output)

sct()


#this take a sc of a specific section of screen so far
# TODO 
# use tkinter to create a transparent box and grab coords to use for sc of said box