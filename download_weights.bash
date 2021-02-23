#!/bin/bash

echo 'Download all weights file'

./gdown.py 1JSFLvqAqq2F3LfOCrokdejTLgtfT961B large_model_x2.pt
./gdown.py 1Xeuwp0px0yUvVITx1ZAQK7jU4bajuVi8 large_model_x3.pt
./gdown.py 1zt86D-9kgLUlf-UXRJ_wvbJFxa_oQW3s large_model_x4.pt

./gdown.py 1DSa0Ba2b8GoRccfTo_XGTJr6iF_zEdmH small_model_x2.pt
./gdown.py 10zAnz5mXVBCgOoGHcNSAAk1ENdtJFt_U small_model_x3.pt
./gdown.py 1YQO71AfBtiOnFVuFJC0b8cR-zdm98Od8 small_model_x4.pt