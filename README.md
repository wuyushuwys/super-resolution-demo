## Super Resolution Inference Demo

Based on [WDSR](https://github.com/ychfan/wdsr)

Just for fun :P

1. Download weight file: `./download_weights.bash`
2. Install dependencies:
  - Create conda environment: `conda create -n SR`
  - Activate conda environment: `conda activate SR`
  - Install packages: 
    - `conda install pytorch torchvision cudatoolkit=10.2 -c pytorch`
    - `python3 -m pip install tqdm opencv-python --no-cache-dir`
  - (Optional) Clean Conda cache: `conda clean -a`
3. Put images in `inputs` folder
4. Run script: `python main.py`
5. Outputs will be saved in `outputs` folder
- For more details: 'python main.py -h'