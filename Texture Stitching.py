# 演算法分析機測
# 學號: 11127115 / 11127127 / 11127148
# 姓名: 陳姿安 / 陳沛君 / 劉梓萱
# 中原大學資訊工程系

import numpy as np
import cv2

# ========== read_input ==========
def read_input():
    image_name = input("請輸入影像檔：")
    direction = int( input("請輸入拼貼方向 (1)水平、(2)垂直：") )
    overlap_ratio = int( input("請輸入重疊比例 (%)：") )

    return image_name, direction, overlap_ratio

# ========== get_overlap_area ==========
def get_overlap_area( image_name, direction, overlap_ratio ):
    image = cv2.imread(image_name, -1)
    overlap_length = round( image.shape[direction-1] * overlap_ratio / 100 )

    if direction == 1:
        # Cut the overlap and rotate
        # The reason for the rotation is that the difference between the calculated vertical rectangles is too large
        # so the merged image is almost the same as the original image.
        overlap_image1 = cv2.rotate(image[0:image.shape[1], image.shape[0]-overlap_length:image.shape[0]].copy(), cv2.ROTATE_90_CLOCKWISE )
        overlap_image2 = cv2.rotate(image[0:image.shape[1], 0:overlap_length].copy(), cv2.ROTATE_90_CLOCKWISE )
    else:
        # Cut the overlap
        overlap_image1 = image[image.shape[1] - overlap_length:image.shape[1], 0:image.shape[0]].copy()
        overlap_image2 = image[0:overlap_length, 0:image.shape[0]].copy()

    height = overlap_length
    width = image.shape[0]

    return image, overlap_image1, overlap_image2, height, width

# ========== get_seam ==========
def get_seam( record, previous_node, width, height ):
    minimum = np.inf
    seam = [0]

    # find the path which have smallest difference
    for i in range(height):
        if minimum > record[i][width-1]:
            seam[0] = i
            minimum = record[i][width-1]

    # get the seam (smallest difference path )
    j = width-1
    while j >= 1:
        seam.insert(0, previous_node[seam[0]][j])
        j = j - 1
        
    return seam

# ========== process_overlap_area ==========
def process_overlap_area( image1, image2, height, width ):
    similarity = calculate_similarity( image1, image2 )
    record = np.zeros((height, width), dtype=np.float32)        # Record cumulative similarity
    previous_node = np.zeros((height, width), dtype=np.int32)   # Record the previous point of this path

    record[:,0] = similarity[:,0]

    for i in range(1, width):
        for j in range(height):
            # Get the path with the smallest difference among the paths to the current node
            if j == 0:
                min_similarity = min( record[j][i-1], record[j+1][i-1] )
            elif j == height-1:
                min_similarity = min( record[j-1][i-1], record[j][i-1] ) 
            else:
                min_similarity = min( record[j-1][i-1], record[j][i-1], record[j+1][i-1] ) 

            # record the previous node from smallest difference path
            if j != 0 and min_similarity == record[j-1][i-1]:
                previous_node[j][i] = j-1
            elif j != height-1 and min_similarity == record[j+1][i-1]:
                previous_node[j][i] = j+1
            else:
                previous_node[j][i] = j

            # calculate the similarity of current node
            record[j][i] = similarity[j][i] + min_similarity

    # print(record[:,255])
    seam = get_seam(record, previous_node, width, height )
    # print(seam)
    return seam

# ========== calculate_similarity ==========
def calculate_similarity( image1, image2 ):
    # calculate the difference of two image
    similarity = np.linalg.norm( image1.astype(np.float32) - image2.astype(np.float32), axis=2 )

    return similarity

# ========== get_merge ==========
def get_merge( width, height, image1, image2, seam ):
    merge_image = image1.copy()

    # Overlapping parts of blended images
    for i in range( width ):
        # merge_image[seam[i],i] = [0,0,255]
        for j in range( seam[i]+1, height ):
            merge_image[j,i] = image2[j,i]

    return merge_image

# ========== collage ==========
def collage( direction, width, height, image, merge_image ):

    # print(width, height)
    
    # Collage direction is horizontal
    if direction == 1:
        # Return to original direction
        merge_image = cv2.rotate(merge_image, cv2.ROTATE_90_COUNTERCLOCKWISE )
        temp = height
        height = width
        width = temp

        # Crop images for collage
        image1 = image[0:image.shape[1], 0:image.shape[0]-width]
        image2 = image[0:image.shape[1], width:image.shape[0]]

        # Collage Image
        collage_image = cv2.hconcat([image1, merge_image, image2])

    # Collage direction is vertical
    else:
        # Crop images for collage
        image1 = image[0:image.shape[1]-height, 0:image.shape[0]]
        image2 = image[height:image.shape[1], 0:image.shape[0]]

        # Collage Image
        collage_image = cv2.vconcat([image1, merge_image, image2])

    return collage_image

# ========== main ==========
def main():
    image_name, direction, overlap_ratio = read_input()
    image, image1, image2, height, width = get_overlap_area( image_name, direction, overlap_ratio )
    seam = process_overlap_area( image1, image2, height, width )
    merge_image = get_merge( width, height, image1, image2, seam )
    collage_image = collage( direction, width, height, image, merge_image)

    # Output image
    cv2.imwrite( image_name.split(".")[0] + "_result.bmp", collage_image)
    
    print()
    print("輸出影像檔", image_name.split(".")[0] + "_result.bmp")

main()