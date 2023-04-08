% Load sample image
I = imread('testpattern512.tif');

% Compute Sobel kernels
h = fspecial('sobel');
h1 = h';
h2 = -h;

% Apply Sobel kernels to image using imfilter
gx = imfilter(double(I), h1, 'replicate');
gy = imfilter(double(I), h2, 'replicate');
mag1 = sqrt(gx.^2 + gy.^2);

% Compute gradient magnitude image using edge function
mag2 = edge(I, 'Sobel', [], 'both');

% Scale the pixel values of the edge image to [0, 255]
mag2 = uint8(255 * mag2);

% Display results in three large figures
figure('Position', [100 100 800 600]);
subplot(1,3,1); imshow(I); title('Input image');
subplot(1,3,2); imshow(mag1, []); title('Gradient magnitude using imfilter');
subplot(1,3,3); imshow(mag2); title('Gradient magnitude using edge');

% Save the gradient magnitude images as files
imwrite(uint8(mag1), 'Sobel Magnitude Imfilter.tif');
imwrite(uint8(mag2), 'Sobel Magnitude Edge.tif');
