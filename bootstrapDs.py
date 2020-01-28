import os
import shutil
import numpy as np

# Split the provided training set into train, validation and test set
largeTrainDestPath = 'DataSet/ModelTrainingDataset/Train/Large'
smallTrainDestPath = 'DataSet/ModelTrainingDataset/Train/Small'
largeValidationDestPath = 'DataSet/ModelTrainingDataset/Validation/Large'
smallValidationDestPath = 'DataSet/ModelTrainingDataset/Validation/Small'
originLargesFilesPath = 'DataSet/TrainImages/Large'
originSmallsFilesPath = 'DataSet/TrainImages/Small'

largesFiles = os.listdir(originLargesFilesPath)
smallsFiles = os.listdir(originSmallsFilesPath)

seed = 18
indexes = np.arange(0, len(largesFiles))
np.random.seed(seed)
np.random.shuffle(indexes)
validationSize = int(len(largesFiles) * 0.2)

def moveTo(basePath, files, dest):
    for f in files:
        shutil.move(os.path.join(basePath, f), dest)

moveTo(originLargesFilesPath, largesFiles[0:validationSize], largeValidationDestPath)
moveTo(originLargesFilesPath, largesFiles[validationSize:len(largesFiles)], largeTrainDestPath)

moveTo(originSmallsFilesPath, smallsFiles[0:validationSize], smallValidationDestPath)
moveTo(originSmallsFilesPath, smallsFiles[validationSize:len(largesFiles)], smallTrainDestPath)

def printDirectoryStructure(startpath):
    for root, _, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        print('{}{} files'.format(subindent, len(files)))

printDirectoryStructure('DataSet/ModelTrainingDataset')