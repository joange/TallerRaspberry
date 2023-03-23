# run with python2 vmf.py <realtive path of image> <frequency of noise> <kernel size(must be odd)>
# -*- coding: utf-8 -*-

# Copia d'objectes i sobretot d'objectes que copien objectes
from copy import deepcopy
import numpy as np          # Llibreria de càlcul numèric
import cv2                  # computer vision. Llibreries de imatges i videos
import random
import math
import sys
import os.path
from numpy.lib.function_base import vectorize
from numpy import Infinity


# recupera la finestra de filtrat, en la posició i,j d'una imatge amb un tamany (imparell) de filtrat
def get_window(imatge, tamany, i, j):
    desp = (tamany-1)//2
    begin_row = i-desp
    begin_col = j-desp
    # slices arr1 for size around index given by start_row and start_col
    arr = imatge[begin_row:begin_row+tamany, begin_col:begin_col+tamany]
    return(arr)

# adds salt and pepper noise to the image randomly with about frequency of freq, given as a percent


def add_sp_noise_color(image1, p, neighborhood,uniform=False):
    """
    Aquesta funció contamina els pixels de la imatge amb probabilitat p. Depenent del
    tipus de soroll fa:
    
    Ruido uniforme: Se contaminan los 3 canales con valores entre 0 y 255
    Ruido impulsivo: se contamina un sólo canal o los 3 con valores a 0 o 255


    """

    '''
    #Comprovem si existeix imatge corrupta, i si ja existeix la carrega
    # Els noms son:
        imatge_[UN|SP]_p.bmp

    '''
    name=image1[0:image1.rindex(".")]
    nameOut=name+"_"
    if uniform:
        nameOut+="UN"
    else:
        nameOut+="SP"
    
    nameOut+=("_"+str(p)+".bmp")




    if os.path.isfile(nameOut):
        noisy = cv2.imread(nameOut)
        return noisy
    


    # copy by value to avoid modification to original image
    print(image1)
    noisy = cv2.imread(image1)
    x, y, z = noisy.shape
    offset = (neighborhood-1)//2
    
    # Recorrem imatge. Les vores no es tracten
    for i in range(offset, x-offset):
        for j in range(offset, y-offset):
            if random.random() < p:   #Contaminem
                if uniform:
                    noisy[i,j,0]=random.randint(0,255)
                    noisy[i,j,1]=random.randint(0,255)
                    noisy[i,j,2]=random.randint(0,255)
                else:
                    # decidimos que canal contaminar
                    x=random.random();
                    if x<0.3: # El R
                        noisy[i,j,0]=random.randint(0,1)*255
                    elif x<0.6: # El G
                        noisy[i,j,1]=random.randint(0,1)*255
                    elif x<0.9: # El B
                        noisy[i,j,2]=random.randint(0,1)*255
                    else:
                        noisy[i,j,:]=random.randint(0,1)*255

    cv2.imwrite(nameOut, noisy)
    return(noisy)




# adds normally distributed noise for whole image with standard deviation input in range of 0-255


def noise_gauss(image1, std_dev):
    # computes a normally distrubuted array of integers the size of image1
    img2 = np.random.normal(0, std_dev, image1.shape).astype(int)
    img2 = cv2.convertScaleAbs(img2)
    img3 = image1+img2
    return img3

# applies median filter to the image


# Filtrat de mediana per una capa sol
def median_filter(image1, neighborhood):
    x, y = image1.shape
    img2 = deepcopy(image1)
    median = 0
    # using an offset so it doesn't try to get the neighborhood of an edge pixel
    offset = (neighborhood-1)//2

    for a in range(offset, x-offset):
        print(a)
        for b in range(offset, y-offset):
            median = int(np.median(get_window(img2, neighborhood, a, b)))
            img2[a, b] = median
        
    return img2


def noise_color(image1, freq):
    # copy by value to avoid modification to original image
    im2 = deepcopy(image1)
    is_high = True
    x, y, z = image1.shape
    for a in range(0, x):
        for b in range(0, y):
            if (random.random() < freq):
                for x in range(0, 3):
                    im2[a, b, x] = random.randint(0, 255)
    return(im2)


def get_minimum_dist(image1, neighborhood, a, b):
    kern = get_window(image1, neighborhood, a, b)
    # maximum distance should be around 3975 for 3 dimensional pixels from 0 to 255 for a 9 pixel neighborhood
    min_dist = np.Infinity
    sum_dist = 0
    for x in range(0, neighborhood):
        for y in range(0, neighborhood):
            sum_dist = 0
            for c in range(0, neighborhood):
                for d in range(0, neighborhood):
                    distance = np.linalg.norm((kern[x][y][:]).astype(
                        np.uint16)-kern[c][d][:].astype(np.uint16))
                    sum_dist = sum_dist+distance
            if(sum_dist < min_dist):
                min_dist = sum_dist
                min_pix = kern[x][y][:]
    return(min_pix)


# applies median filter to the image
def vector_median_filter(image1, neighborhood):
    x, y, z = image1.shape
    img2 = deepcopy(image1)
    # using an offset so it doesn't try to get the neighborhood of an edge pixel
    offset = (neighborhood-1)//2
    for a in range(offset, x-offset):
        print("v ",a)
        for b in range(offset, y-offset):
            min_pix = get_minimum_dist(image1, neighborhood, a, b)
            img2[a][b][:] = min_pix
    return img2

def L2(v1,v2):
    x=np.linalg.norm(np.array(v1)-np.array(v2))
    return x

def VMF(image,nbhd):
    x, y, z = image.shape
    filtered = deepcopy(image)

    offset = (nbhd-1)//2

    f = open('log.txt', 'w')
    # recorrem imatge. Les vores no es tracten
    for i in range(offset, x-offset):
        print("\r%2.2f%%"%(i*100/(x-2)),end="")
        for j in range(offset, y-offset):
            #Minifor per a filtrar el pixel i,j
            f.write("Filtrant el pixel "+str(i)+"-"+str(j)+" : " +str(image[i][j][:]))
            minDist=np.Infinity
            for ii in range(i-offset,i+offset):
                for jj in range(j-offset,j+offset):
                    
                    sum_dist=0
                    # Calculem la distància acumulada del pixel ii,jj  a tota la finestra

                    for iii in range(ii-offset,ii+offset+1):
                        for jjj in range(jj-offset,jj+offset+1):
                            distance = L2(image[ii][jj][:],image[iii][jjj][:])
                            sum_dist = sum_dist+distance

                    if sum_dist<minDist:
                        minDist=sum_dist
                        min_i=iii
                        min_j=jjj

            f.write(" El millor pixel per al %d-%d és el %d-%d [%d %d %d]\n"%(i,j,min_i,min_j,image[min_i][min_j][0],image[min_i][min_j][1],image[min_i][min_j][2]))
            #basura=input("seguim...")
            filtered[i][j]=image[min_i][min_j]
    f.close()
    return filtered

def main():
    print(sys.argv)

    if len(sys.argv) != 4:
        print("Error")
    else:
        image1 = str(sys.argv[1])

        if not os.path.isfile(image1):
            print("La imatge no existeix. Eixint")
            sys.exit()
        
        frequency = float(sys.argv[2])
        nbhd = int(sys.argv[3])

        # Imatge original
        im1 = cv2.imread(image1,cv2.IMREAD_COLOR)

        # im1 és una matriu altxamplex colors. Tenint el BGR (en compte de RGB)
        
        #closing all open windows  
        #cv2.destroyAllWindows()

        x, y, z = im1.shape

        print("L'imatge és %dx%d amb %d colors"%(x,y,z))

        # Imatge sorollosa
        im_noisy_sp = add_sp_noise_color(image1,frequency,nbhd,False)
#        im_noisy_imp = add_sp_noise_color(im1, frequency,True)
#        cv2.imwrite(name+"_UN.bmp", im_noisy_imp)
        #filtratge amb la correlació de canals
        #im_vmed_filtered = vector_median_filter(im_noisy_sp, nbhd)
        im_vmed_filtered = VMF(im_noisy_sp, nbhd)
        #Filtratge per canals separats
        '''
        #descomposem canals
        b_salt, g_salt, r_salt = cv2.split(im_noisy_sp)

        #Filtratge de cada canal
        b_med = median_filter(b_salt, nbhd)
        g_med = median_filter(g_salt, nbhd)
        r_med = median_filter(r_salt, nbhd)

        # unim la imatge
        im_median_filtered = cv2.merge((b_med, g_med, r_med))

        '''    
        name=image1[0:image1.rindex(".")]
        
      # cv2.imwrite(name+"_MedianFilter.bmp", im_median_filtered)
        cv2.imwrite(name+"_VectorMedianFilter.bmp", im_vmed_filtered)

        # 195075 = (255^2)*3 the range of possible vector values
        '''
        diff_img = (im1-im_median_filtered)**2
        mse_median = diff_img.sum()/(im1.size)
        psnr_median = 10*(math.log10((195075)/mse_median))
        '''
        diff_img = (im1-im_vmed_filtered)**2
        mse_vmed = diff_img.sum()/(im1.size)
        psnr_vmed = 10*(math.log10((195075)/mse_vmed))

        
        
        #fil.write("Median Filter PSNR: " + str(psnr_median) + " db")
        #fil.write("\nVector Median Filter PSNR: " + str(psnr_vmed) + " db")
        
if __name__ == '__main__':
    main()
    