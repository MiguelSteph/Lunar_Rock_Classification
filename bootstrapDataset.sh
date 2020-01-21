#!/usr/bin/env bash

# STEPS TO CHANGE OUR DATASET IN THE RIGHT FORMAT
#   1- Download the DataSet
#   2- Unzip the DataSet 
#   3- Delete the DataSet zip file
#   4- Unzip the Train and Test set 
#   5- Delete the Train and test Set zip file
#   6- Create the folders that my Structure
#   7- Rename the test set to OnlineTestSet
#   8- Run the Python code to move datata around creating the train, test and validation set

wget http://hck.re/kkBIfM -O DataSet.zip
unzip DataSet.zip
rm -f DataSet.zip

unzip -q DataSet/Test\ Images.zip -d DataSet
unzip -q DataSet/Train\ Images.zip -d DataSet
mv DataSet/Test\ Images DataSet/TestImages
mv DataSet/Train\ Images DataSet/TrainImages
rm -rf DataSet/Test\ Images.zip DataSet/Train\ Images.zip

mkdir -p DataSet/ModelTrainingDataset/Test/Large DataSet/ModelTrainingDataset/Test/Small \
    DataSet/ModelTrainingDataset/Validation/Large DataSet/ModelTrainingDataset/Validation/Small \
    DataSet/ModelTrainingDataset/Train/Large DataSet/ModelTrainingDataset/Train/Small DataSet/OnlineTestDataset

mv DataSet/TestImages DataSet/OnlineTestDataset

python bootstrapDs.py

rm -rf DataSet/TrainImages

echo 'End of the Dataset Bootstrapping'







