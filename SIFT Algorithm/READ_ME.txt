To run Raw Image Classifier and Sift Classifier - do the following
Step 1. install image-classification-env-requirements.txt to your desired environment and then activate that environment
Step 2. run Scripts/Sift Classifier.py, when prompted - enter 1 for svg resized files or 2 for the interpolation resized files
Step 3. run Scripts/Raw Image Classifier.py, when prompted - enter 1 for svg resized files or 2 for the interpolation resized files

optionally, if you would like to see how the resize was done from the original data - do the following
THIS MAY ALSO REQUIRE SOME ADDITIONAL JVM CONFIGURATION ON YOUR LOCAL MACHINE
Step 1. install conversion-env-requirements.txt to your desired environment and then activate that environment
Step 2. FOR TESTING, you can delete leaf-classification-jpg-resized, leaf-classification-svg
***PLEASE DO NOT DELETE ANYTHING INSIDE leaf-classification***
Step 3. run Scripts/Resize-Zoom-JPGviaSVG (for some reason this worked from my IDE but not from the comman line for me)

feel free to look through my report summarizing my findings at the following location
Results & Report/Sift vs Raw Image for MLP Classifers.docx