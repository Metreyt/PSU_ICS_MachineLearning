# Machine Learning using Python and Tensorflow
## Chris Blanton (cjb47@psu.edu)
## The Pennsylvania State University
## Institute for CyberScience and Materials Research Institute

Slides <https://goo.gl/5qNftz>

This workshop is an introduction to using the TensorFlow framework 
with Python. 

# Objectives of this workshop
The objectives of this introductive workshop are to give a 
brief understanding of what machine learning is as well
as some hands-on instruction using the TensorFlow framework
and associated libraries to get started. 


## Preparing a local environment for completing the workshop

### Linux

Here are the steps for creating the workshop environment:

```bash
$ conda create -n psu_tf_workshop_py36 python=3.6 jupyter spyder numpy pandas scikit-learn matplotlib seaborn 
$ conda activate psy_tf_workshop_py36
$ pip install --upgrade tensorflow
$ python
Python 3.6.8 |Anaconda, Inc.| (default, Dec 30 2018, 01:22:34) 
[GCC 7.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import tensorflow as tf
>>> hello = tf.constant('Hello, Tensorflow')
>>> sess = tf.Session()
2019-01-18 06:05:22.078114: I tensorflow/core/platform/cpu_feature_guard.cc:141] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2
>>> print(sess.run(hello))
b'Hello, Tensorflow'
>>> exit()
```



### Windows

```
c:\ > conda create -n psu_tf_workshop_py36 python=3.6 jupyter spyder numpy pandas scikit-learn matplotlib seaborn
c:\ > conda activate psu_tf_workshop_py36
c:\ > pip install --upgrade tensorflow
```

### Mac OSX
```bash
$ conda create -n psu_tf_workshop_py36 python=3.6 jupyter spyder numpy pandas scikit-learn matplotlib seaborn 
$ conda activate psy_tf_workshop_py36
$ pip install --upgrade tensorflow
$ python
Python 3.6.8 |Anaconda, Inc.| (default, Dec 30 2018, 01:22:34) 
[GCC 7.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import tensorflow as tf
>>> hello = tf.constant('Hello, Tensorflow')
>>> sess = tf.Session()
2019-01-18 06:05:22.078114: I tensorflow/core/platform/cpu_feature_guard.cc:141] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2
>>> print(sess.run(hello))
b'Hello, Tensorflow'
>>> exit()
```



## Using a cloud Python environment for completing the workshop

Using Google Colab <https://colab.research.google.com> is a good way to have a working 
environment that has TensorFlow available without installing on a local computer. 

On Colab, you can directly interface with the GitHub repo.



