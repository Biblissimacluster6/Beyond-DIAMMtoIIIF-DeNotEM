# Beyond-DIAMMtoIIIF-DeNotEM
BeyondDIAMMtoIIIF/DeNotEM is a project for the automatic recognition of early musical notation in manuscript sources from the Middle Ages and the Renaissance. 

## DeNotEM - Detecting Notation in Early Music

This project, carried out as part of Biblissima+ Cluster 6, is a continuation of the DIAMMtoIIIF project designed to improve the display and consultation of early musical sources using the IIIF protocol and the resources of the DIAMM (Digital Image Archive of Medieval Music) database. In order to further enrich the IIIF manifests created, Cluster 6 has developed recognition models that will eventually make it possible to generate annotation files containing the names of musical parts as well as their location and content. This project focuses on the square notations (measured or not) of late medieval music (except plainchant). 

### voxlabel.pt

To achieve this, Cluster 6 initially had to collect numerous scans (several hundred) of musical sources dating from the 13th and 14th centuries. Most of which are held at the BnF. The recovery of these images via the library's IIIF servers largely contributed to the feasibility of the project. Two YOLO detection models were initially developed in response to specific tasks or problems. The first model, 'voxlabel', aims to recognise the type of voice in monophonic and polyphonic pieces, and thus to distinguish between polyphonic and monodic notations. Its learning is based mainly on the layouts and the differences in size and density between the voices. Based on the corpus trained so far, the model has been trained to identify the five voice types most commonly used in the late Middle Ages: cantus, triplum, duplum, contratenor and tenor. 

![code](https://github.com/Biblissimacluster6/Beyond-DIAMMtoIIIF-DeNotEM/blob/main/img/Label%20model.jpg)

### earlystave.pt

The second model, 'earlystave', improves the detection of musical sections in the case of short musical passages interpolated from text-rich sources. The automatic detection of certain voices can indeed prove problematic in 13th century chansonniers. The example below shows just how difficult it can be to identify a musical part in complex layouts. Earlystave therefore focuses on finer fractions of musical notation, i.e. the staves. It can therefore signal the presence of musical notation in dense corpora and help the voxlabel model to identify a potential voice. This model is also based on fragmentary or difficult-to-read sources in order to improve its accuracy. 

![code](https://github.com/Biblissimacluster6/Beyond-DIAMMtoIIIF-DeNotEM/blob/main/img/earlystave.jpg)

### Development and use of the models

The YOLO models were trained using several hundred digitisations annotated with the LabelIMG tool. The YOLO (You Only Look Once) algorithm is a computer vision object detection algorithm based on a convolutional neural network. Unlike other approaches that segment the image into regions and then apply a classifier to each region individually, YOLO divides the image into a grid and predicts bounding boxes and object probabilities for each cell in that grid. This allows YOLO to be very fast and efficient, with a shorter inference time than other methods. 

![code](https://github.com/Biblissimacluster6/Beyond-DIAMMtoIIIF-DeNotEM/blob/main/img/Yolo%20example.jpg)

The models were trained using the ImageAI Python library. The first versions are published in this directory. New versions will be published shortly. The mAP of the first versions is not very high (0.554 for voxlabel; 0.569 for earlystave), but the models already make it possible to process numerous images of musical sources from the 13th and 14th centuries. 

A Python code (CorpusAI.py) enabling the models to be used on a large number of images and the contents of the boxes detected to be saved in a specific folder is also published above by Cluster 6. It requires the ImageAI library to be installed and needs to be completed with the paths of the files to be analysed and the target directory. Thanks to CorpusAI.py, it is now very easy for any user to run YOLO recognition models, including those published as part of DeNotEM.

## The future of DeNotEM: towards a super model for early music notation

The current advances being made by Cluster 6 as part of the DeNotEM project are aimed at improving recognition models by focusing on several future objectives. Firstly, we are currently developing post-processing algorithms to correct inaccuracies in recognition models. Some of these algorithms have already been tested and found to be very practical, but further improvements are still needed.

One major objective is to create a super model capable of exploiting a much richer context in terms of information. This will involve cross-tabulating the results of the trained models with other tools, such as Kraken OCR, to take advantage of their respective strengths. Experimental tests have so far proved successful. In addition, we wish to use more powerful YOLO models focusing on finer aspects of musical notation, ranging from the shape of the musical pieces analysed to their genre. In the long term, this system will be capable not only of recognising musical parts, but also of extracting lyrics and voice labels (where appropriate). It will also be able to create connections between different musical sources and distinguish different spellings (such as regional differences), making it easier to date or attribute certain pieces.

## Bibliography and communication

David Fiala and Kevin Roger. 2023. Connecting online early music libraries and musicological resources: Experiments in ergonomics in the Biblissima+ framework. In Proceedings of the 10th International Conference on Digital Libraries for Musicology (DLfM '23). Association for Computing Machinery, New York, NY, USA, 128–131. https://doi.org/10.1145/3625135.3625140

Kévin Roger. « Les modèles IA appliqués aux sources musicales anciennes : Constitution des corpus et premiers pas ». 2es journées du Cluster 6 Biblissima+, Paris, 4 septembre 2023. https://doi.org/10.5281/zenodo.8413599

Kévin Roger. « The French digital infrastructure for written heritage Biblissima+ and the challenges of musical heritage ». MedRen2023, Munich, 26 juillet 2023. https://doi.org/10.5281/zenodo.8414821

Alicia Fornés and Kévin Roger. « Computer Vision Methodologies applied to musical documents ». Novel approaches to Digital Codicology, Tours, 11 mai 2023.

