from Blit import *
photo = Bitmap('IMG_2467.JPG')
hackcolor = Color(54, 36, 135)

def soft_light(bottom_chan, top_chan):
    """ Hard light blend function.

        Math from http://illusions.hu/effectwiki/doku.php?id=hard_light_blending
    """
    # different pixel subsets for dark and light parts of overlay
    dk, lt = top_chan < .5, top_chan >= .5

    output_chan = numpy.empty(bottom_chan.shape, bottom_chan.dtype)
    output_chan[dk] = 2 * bottom_chan[dk] * top_chan[dk] + bottom_chan[dk]**2 * (1 - 2*top_chan[dk])
    output_chan[lt] = 2 * bottom_chan[lt] * (1 - top_chan[lt]) + bottom_chan[lt]**0.5 * (2*top_chan[lt] - 1)

    return output_chan

coloroverlay = photo.blend(hackcolor, blendfunc=hard_light)
coloroverlay.image().save("abc.png")
