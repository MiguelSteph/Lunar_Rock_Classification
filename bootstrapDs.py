import os
import shutil
import numpy as np

# Split the provided training set into train, validation and test set
largeTrainDestPath = 'DataSet/ModelTrainingDataset/Train/Large'
smallTrainDestPath = 'DataSet/ModelTrainingDataset/Train/Small'
largeValidationDestPath = 'DataSet/ModelTrainingDataset/Validation/Large'
smallValidationDestPath = 'DataSet/ModelTrainingDataset/Validation/Small'
largeTestDestPath = 'DataSet/ModelTrainingDataset/Test/Large'
smallTestDestPath = 'DataSet/ModelTrainingDataset/Test/Small'
originLargesFilesPath = 'DataSet/TrainImages/Large'
originSmallsFilesPath = 'DataSet/TrainImages/Small'

largesFiles = os.listdir(originLargesFilesPath)
smallsFiles = os.listdir(originSmallsFilesPath)

seed = 18
indexes = np.arange(0, len(largesFiles))
np.random.seed(seed)
np.random.shuffle(indexes)
testSize = int(len(largesFiles) * 0.1)

def moveTo(basePath, files, dest):
    for f in files:
        shutil.move(os.path.join(basePath, f), dest)

moveTo(originLargesFilesPath, largesFiles[0:testSize], largeTestDestPath)
moveTo(originLargesFilesPath, largesFiles[testSize:2*testSize], largeValidationDestPath)
moveTo(originLargesFilesPath, largesFiles[2*testSize:len(largesFiles)], largeTrainDestPath)

moveTo(originSmallsFilesPath, smallsFiles[0:testSize], smallTestDestPath)
moveTo(originSmallsFilesPath, smallsFiles[testSize:2*testSize], smallValidationDestPath)
moveTo(originSmallsFilesPath, smallsFiles[2*testSize:len(largesFiles)], smallTrainDestPath)

def printDirectoryStructure(startpath):
    for root, _, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        print('{}{} files'.format(subindent, len(files)))

printDirectoryStructure('DataSet/ModelTrainingDataset')