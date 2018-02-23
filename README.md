# cahw2018_hydrophone


Keep all files into data folder.

Notebooks in notebook folder.

### Data Access

- many files of different size
- we store them locally in to files of equal size
- about 2GB for 2hours around eclipse

### Data processing 
- we need to efficiently calculate spectrograms of many files: maybe we parallelize this step
- should we downsample/throw out frequencies at this step?


### Visualization

#### clustering points with a thumbnail 

- static scikit learn

http://bebi103.caltech.edu.s3-website-us-east-1.amazonaws.com/2016/tutorials/aux8_tsne.html

- javascript tsne

https://github.com/scienceai/tsne-js

- D3.js tsne 

https://github.com/karpathy/tsnejs

#### sliding histograms

-  save spectrograms for different starting points: visualize as a video or with a slider after that
-  see if we can make a widget with computing the spectrogram on the fly


