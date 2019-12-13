# Synthesizing Normalized Faces From Facial Identity Features (Additional Results B.3 Section Implementation Only)

This repository provides a Python implementation of the CVPR 2017 Paper - Synthesizing Normalized Faces From Facial Identity Features (Additional Results B.3 Implementation Only). Only Fitting Texture part is implemented which is mentioned in Additional Results Section B.3 of the paper.
Note that it is not production ready yet. If you encounter any issues, feel free to post.

# Paper
[Synthesizing Normalized Faces From Facial Identity Features](https://arxiv.org/pdf/1701.04851.pdf)

# Dependencies
* [Python 3.5](https://www.python.org/downloads/release/python-352/)
  - [Numpy](https://pypi.org/project/numpy/) -> ```pip install numpy```
  - [Scipy](https://pypi.org/project/scipy/) -> ```pip install scipy```
  
## Usage
### 1. Cloning the repository
```
git clone https://github.com/nabeel3133/3D-texture-fitting.git
```
### 2. Downloading the model
- [BFM09: Basel Face Model 2009](https://faces.dmi.unibas.ch/bfm/index.php?nav=1-1-0&id=details)
  - After you have acquired BFM, extract the BaselFaceModel.tgz and go to`PublicMM1` folder, copy `01_MorphableModel.mat` and paste it in `3D-texture-fitting` folder.
  
### 3. Running the code


## Citation
If this work is useful for your research or if you use this implementation in your academic projects, please cite the following papers:
- [Synthesizing Normalized Faces From Facial Identity Features](https://arxiv.org/pdf/1701.04851.pdf)
```bibtex
@misc{cole2017synthesizing,
    title={Synthesizing Normalized Faces from Facial Identity Features},
    author={Forrester Cole and David Belanger and Dilip Krishnan and Aaron Sarna and Inbar Mosseri and William T. Freeman},
    year={2017},
    eprint={1701.04851},
    archivePrefix={arXiv},
    primaryClass={cs.CV}
}
```
