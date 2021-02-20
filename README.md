# Faster-RCNN-based-Object-Detection


This repository walks through the Object detection process including the custom dataset preparation, training with model congifuration setup and inference of the trained model.

# Requirements
1. Python 3.6
2. Numpy
3. Opencv
4. Pandas
5. Matplotlib
6. Tensorflow_gpu==1.15
7. Lvis

# Note
Download the pretrained model(frozen graph) and the image dataset from the following link :
https://drive.google.com/drive/folders/1ciCiNYvEpeCRIeP4QDzF5qIvnUCUj7UD?usp=sharing

# Dataset Preparation
With few data augmentation techniques such as rotate, flip, blur and translate, incereased the size of the dataset. Further details are in **data_prep_img_process.py**

**Annotation Tool** : MakeSense http://makesense.ai/ 
Annotated data is stored as a csv file and from that source csv file, the train.csv and test.csv are genearated.
With the data available on the test.csv and train.csv, the image dataset is split into test_set and train_set.

# Training
Initially Tensorflow Object Detection API module is installed with all necessary packages.(tensorflow_gpu==1.15)

ref : https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/install.html#tensorflow-object-detection-api-installation

Generate the tfrecords for the test and training set using **generate_tf_records.py**

# Model Architecture 
For quick training and better results, this object detection module was trained on Tensorflow's faster_rcnn_inception_v2 model.

# Hyper Parameters
1.num-steps = 5000
2.eval-steps=50
3.batch-size = 12
4.initial_learning_rate = 0.0002
5.num-classes = 1

# Model Performance Evaluation 
 Displayed using Tensorboard on the python notebook.




