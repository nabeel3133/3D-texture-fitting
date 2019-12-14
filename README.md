# Synthesizing Normalized Faces From Facial Identity Features (Additional Results B.3 Section Implementation Only)
<p align="center"> 
<img style="display:inline;" src="/images/test_input.gif">
<img style="display:inline;" src="/images/test_output.gif">
</p>

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
cd 3d-texture-fitting
```
### 2. Downloading the model
- [BFM09: Basel Face Model 2009](https://faces.dmi.unibas.ch/bfm/index.php?nav=1-1-0&id=details)
  - After you have acquired BFM, extract the BaselFaceModel.tgz and go to`PublicMM1` folder, copy `01_MorphableModel.mat`, `BFM_exp_idx.mat` and paste it in `./3D-texture-fitting/configs` folder.
  
### 3. Running the code
Run the `main.py` with obj output from ddfa as input
```
python main.py -o ./samples/test.obj
```
If you can see the following output log in terminal, you ran it successfully.
```
BFM Mapping for Texture Prediction Started...
BFM Mapping for Texture Prediction Completed
Predicting Ear and Neck Texture...
Predicting Ear and Neck Texture Completed
Dump to ./samples/output.obj
Dump to ./samples/output.ply
```
Two output files (obj and ply) will be saved in `3D-texture-fitting/samples` folder with the name `output.obj` and `output.ply` which can be redered by Meshlab or Microsoft 3D Builder.

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
## References
- [Face Alignment in Full Pose: A 3D Total Solution](https://arxiv.org/abs/1804.01005) [(Github)](https://github.com/cleardusk/3DDFA)
```bibtex
  @misc{3ddfa_cleardusk,
  author =       {Jianzhu Guo, Xiangyu Zhu and Zhen Lei},
  title =        {3DDFA},
  howpublished = {\url{https://github.com/cleardusk/3DDFA}},
  year =         {2018}
}
```
