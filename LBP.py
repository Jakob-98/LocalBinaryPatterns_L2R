# https://link.springer.com/article/10.1007/s11042-020-09698-5
def lbp_l2r(img, x, y):
    ylen = img.shape[1]
    pc = img[x, y,1]
    res = str()
    coords = [(-1, 1), (-1, 2), (0, 2), (1, 2), (1, 1), (1, 0), (0, 0), (-1, 0)]
    for coord in coords: 
        yoffset, layer = coord
        # skip top and bottom pixels. 
        if y + yoffset == ylen or y + yoffset == 0: 
            pi = -1
        else: 
            pi = img[x, y + yoffset, layer]
        res += (str(1 * (pi >= pc)))
    return int(res, 2)
  
  
  def get_lbp(img):
    fin = np.ndarray((img.shape[0], img.shape[1]))
    for xi in range(img.shape[0]):
        for yi in range(img.shape[1]):
            fin[xi, yi] = lbp_l2r(img, xi, yi)
    return fin
  
