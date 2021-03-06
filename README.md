# K-means-Clustering-Image-Compression
In this exercise, we will use k-means clustering to compress an image. When an image is stored in the PNG format, for each pixel, the red, blue and green components are stored as 8 bit numbers each. Thus, we need 24 bits per pixel 4 . The idea for compressing is the following. We think of each pixel with components (r, g, b) as a point in three dimensions. Thus there are as many points as there are pixels in the image. Then, using k-means clustering, we compute k cluster centers. Each cluster center is a point in three dimensions and thus represents a color. If a point p belongs to a cluster with center c, we will change the color of the pixel corresponding to p to the color represented by c. We expect the error caused by this change to be small. Let us take k = 64 so that each cluster number is encoded by 6 bits. Thus, we will only use 64 distinct colors corresponding to the 64 cluster centers. Each pixel can now store 6 bits of information indicating which of the 64 colors it uses. Thus, apart from the overhead of storing the 64 colors using 64 × 3 bytes, we only use 6 bits per pixel, leading to a reduction in space by a factor of about 4.

1. We use the above idea to convert the image Neuschwanstein small.png into an image that uses only 64 distinct colors.

2. If you try to use the same idea for a larger image like Neuschwanstein large.png, you will find that k-Means takes a long time since the image has over a million pixels. Use
MiniBatchKMeans instead of KMeans from Scikit-learn. Skim this short paper to learn how MiniBatchKMeans works.

See detailed description in the pdf file, problem 5.
