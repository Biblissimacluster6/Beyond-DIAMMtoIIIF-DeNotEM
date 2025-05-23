# DeNotEM - Detecting Notation in Early Music

<img src="https://github.com/Biblissimacluster6/DIAMMtoIIIF/blob/main/img/biblissima-baseline-sombre-france2030.png" width="300"><img src="https://github.com/Biblissimacluster6/DIAMMtoIIIF/blob/main/img/Icon.jpg" width="300">

"Ce travail a bénéficié́ d'une aide de l’État gérée par l'Agence Nationale de la Recherche au titre du programme d’Investissements d’avenir portant la référence ANR-21-ESRE-0005 (Biblissima+)"

"This work has received government funding administered by the French National Research Agency under the "Investissements d’avenir" program, reference ANR-21-ESRE-0005 (Biblissima+)."

## Overview

DeNotEM is a project for the automatic recognition of early musical notation in manuscript sources from the Middle Ages and the Renaissance. This project, carried out as part of Biblissima+ Cluster 6, is a continuation of the DIAMMtoIIIF project designed to improve the display and consultation of early musical sources using the IIIF protocol and the resources of the DIAMM (Digital Image Archive of Medieval Music) database. In order to further enrich the IIIF manifests created, Cluster 6 has developed recognition models that will make it possible to generate annotation files containing the names of musical parts as well as their location and content. Eventually, the tools developed will also serve to provide metadata on the types of notations used, the dating of the sources, layout schemes, and more.

## DeNotEM Architecture 

The DeNotEM project develops and applies tools to automatically detect and analyse musical notations in digitised medieval and Renaissance manuscripts. It focuses on enabling high-quality digital musicology workflows through:

- Deep learning-based detection of musical parts
- Classification of polyphonic and monophonic musical parts
- Various metadata inferences about the nature of sources, annotations, dating, etc.
- IIIF-compatible semantic annotation of source images
- Creation of a web interface for musicological paleography

<img src="https://github.com/Biblissimacluster6/Beyond-DIAMMtoIIIF-DeNotEM/blob/main/img/DeNotEM_architecture.jpg" width="400">

All models use the YOLO algorithm. HTR Kraken models are also used in the framework of the project to automatically transcribe text. The architecture is entirely developed in Python.

## DeNotEM Data

To begin with, Cluster 6 focused on square notation from the 13th to the 15th century (excluding monophonic liturgical music). This was the most widespread notational form in the West at the end of the Middle Ages. To optimize the generalization of the detection models, it is indeed necessary to concentrate on corpora whose notational styles are similar. In total, we identified and retrieved the contents of around thirty manuscripts produced between 1250 and 1500. Over 2,000 images were manually annotated as part of the project, which currently amounts to 7,500 annotations. The images were annotated using LabelIMG, an open-source tool that allows for manual labeling of objects within images. This annotation process enables the generation of bounding boxes stored in XML or YOLO format, which are essential for training computer vision models.

## Last model versions

### Detection Models CantusScope (YOLOv8 and YOLOv10)

We have developed two generations of object detection models targeting musical areas in medieval manuscripts (out of notation in score), from 1250 to 1500:

- **CantusScopeV1-YOLOv8-based model**: Initial robust detector (mAP=0.87)
- **CantusScopeV2-YOLOv10-based model**: Optimised with better recall and greater versability (mAP=0.87)

<img src="https://github.com/Biblissimacluster6/Beyond-DIAMMtoIIIF-DeNotEM/blob/main/img/Training_Metrics.png" width="550">

The diagram illustrates the progressive improvement in the V2 model’s performance of CantusScope over the training epochs. The mean Average Precision at 50% IoU (mAP@50) reaches approximately 0.58, while the stricter mAP@50-95 rises to around 0.42. These metrics demonstrate that the model is increasingly capable of detecting musical zones with both spatial accuracy and consistency across diverse manuscript layouts. The precision and recall curves also improve steadily throughout training, converging near 0.59 and 0.58 respectively. This balance suggests the model not only avoids false positives but also captures a large proportion of relevant regions, indicating a robust understanding of musical content in complex manuscript images.

The smooth and consistent evolution of all metrics suggests a stable training process without overfitting. It confirms that the dataset is well-structured and that the model generalizes effectively. These results make the current YOLOv10-based detector suitable for downstream tasks such as voice classification, IIIF annotation, or real-time interaction via a web application.

### Voice Classification Models CantusSort (YOLOv8 and YOLOv10)

Two classification models are also available for identifying distinct musical voices in monodic and polyphonic contexts:

- **CantusSortV1-YOLOv8** - 7 classification labels: Cantusxiii; Tenorxiii; Supxiv; Infxiv; Supxv; Infxv; Empty (average accuracy = 0.93)
- **CantusSortV2-YOLOv10** - 8 classification labels: xiiiend_cantus_m; xiiiend_cantus_nm; xiiiend_tenor_m; xiv_inf_m; xiv_sup_m; xv_inf_m; xv_sup_m; empty (average accuracy = 0.97)

<img src="https://github.com/Biblissimacluster6/Beyond-DIAMMtoIIIF-DeNotEM/blob/main/img/val_batch2_pred.jpg" width="300"><img src="https://github.com/Biblissimacluster6/Beyond-DIAMMtoIIIF-DeNotEM/blob/main/img/output_metrics_class.png" width="550">

The training curve reveals an efficient and stable learning process for the voice classification model. The Top-1 accuracy steadily increases and stabilizes around 96–97%, while the Top-5 accuracy quickly reaches 100% after only a few epochs. This indicates that the model consistently ranks the correct voice class among its top predictions, reflecting both high precision and low ambiguity.

The training loss shows a sharp decline during the first 10 epochs, then flattens progressively, suggesting rapid initial learning followed by fine-tuning of class boundaries. The validation loss also decreases, albeit with minor fluctuations — likely due to limited sample diversity or class imbalance in the validation set. However, no sign of overfitting is observed, as both loss curves converge harmoniously.

Overall, the model demonstrates excellent generalization capacity and consistent classification performance across the corpus. These results suggest that the voice classifier is ready for deployment in real-world manuscript analysis scenarios and could serve as a robust component in a larger MEI or IIIF annotation workflow.

## DeNotEM Team 

- Kévin Roger (leader, developer, annotator) - University of Lorraine
- David Fiala (leader) - University of Tours
- Benjamin Foret (annotator, developer) - University of Lorraine

## Deprecated parts of the projet

The repository has evolved significantly since its early experimental models. The following models (YOLOv3) are considered deprecated in the framework of DeNotEM, but still functional:

### voxlabel.pt (deprecated - YOLOv3 - mAP = 0.554)

Cluster 6 initially had to collect numerous scans (several hundred) of musical sources dating from the 13th and 14th centuries. Most of which are held at the BnF. The recovery of these images via the library's IIIF servers largely contributed to the feasibility of the project. Two YOLO detection models were initially developed in response to specific tasks or problems. The first model, 'voxlabel', aims to recognise the type of voice in monophonic and polyphonic pieces, and thus to distinguish between polyphonic and monodic notations. Its learning is based mainly on the layouts and the differences in size and density between the voices. Based on the corpus trained so far, the model has been trained to identify the five voice types most commonly used in the late Middle Ages: cantus, triplum, duplum, contratenor and tenor. 

### earlystave.pt (deprecated - YOLOv3 - mAP= 0.569)

The second model, 'earlystave', improves the detection of musical sections in the case of short musical passages interpolated from text-rich sources. The automatic detection of certain voices can indeed prove problematic in 13th century chansonniers. The example below shows just how difficult it can be to identify a musical part in complex layouts. Earlystave therefore focuses on finer fractions of musical notation, i.e. the staves. It can therefore signal the presence of musical notation in dense corpora and help the voxlabel model to identify a potential voice. This model is also based on fragmentary or difficult-to-read sources in order to improve its accuracy. 

<img src="https://github.com/Biblissimacluster6/Beyond-DIAMMtoIIIF-DeNotEM/blob/main/img/earlystave.jpg" width="500">

## The future of DeNotEM: towards a global and powerful recognition system for early music notation

![code](https://github.com/Biblissimacluster6/Beyond-DIAMMtoIIIF-DeNotEM/blob/main/img/Yolo%20example.jpg)

The current advances being made by Cluster 6 as part of the DeNotEM project are aimed at improving recognition models by focusing on several future objectives. Firstly, we are currently developing post-processing algorithms to correct inaccuracies in recognition models. Some of these algorithms have already been tested and found to be very practical, but further improvements are still needed.

One major objective is to create a set of  models capable of exploiting a much richer context in terms of information. This will involve cross-tabulating the results of the trained models with other tools, such as Kraken OCR, to take advantage of their respective strengths. Experimental tests have so far proved successful. In addition, we wish to use more powerful YOLO models focusing on finer aspects of musical notation, ranging from the shape of the musical pieces analysed to their genre. In the long term, this system will be capable not only of recognising musical parts, but also of extracting lyrics and voice labels (where appropriate). It will also be able to create connections between different musical sources and distinguish different spellings (such as regional differences), making it easier to date or attribute certain pieces.

## Bibliography and communication

Kévin Roger. 2025. « Les musiques anciennes sous le regard de l’IA : les promesses de DeNotEM ». 2e journée d’étude du département de musicologie de Metz, Metz, 07 mai 2025.

Kévin Roger. 2025. « Le numérique et l’intelligence artificielle appliqués aux répertoires musicaux du Moyen Âge occidental ». Séminaire Cenhtor, Nancy, 25 février 2025.

David Fiala and Kevin Roger. 2023. Connecting online early music libraries and musicological resources: Experiments in ergonomics in the Biblissima+ framework. In Proceedings of the 10th International Conference on Digital Libraries for Musicology (DLfM '23). Association for Computing Machinery, New York, NY, USA, 128–131. https://doi.org/10.1145/3625135.3625140

Kévin Roger. « Les modèles IA appliqués aux sources musicales anciennes : Constitution des corpus et premiers pas ». 2es journées du Cluster 6 Biblissima+, Paris, 4 octobre 2023. https://doi.org/10.5281/zenodo.8413599

Kévin Roger. « The French digital infrastructure for written heritage Biblissima+ and the challenges of musical heritage ». MedRen2023, Munich, 26 juillet 2023. https://doi.org/10.5281/zenodo.8414821

Alicia Fornés and Kévin Roger. « Computer Vision Methodologies applied to musical documents ». Novel approaches to Digital Codicology, Tours, 11 mai 2023.

