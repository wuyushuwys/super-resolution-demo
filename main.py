import torch
from PIL import Image
import numpy as np
from glob import glob
from torchvision import transforms
from torchvision.utils import save_image
import os
import cv2
from tqdm import tqdm
from utils import *
import argparse


def main(args):
    device = torch.device('cuda') if args.gpu and torch.cuda.is_available() else torch.device('cpu')
    
    model_weight = get_weight_name(args)
    
    model = torch.load(model_weight)
    model = model.to(device)
    
    files = get_inputs_name()

    for f in files:
        print('{0:*^80}'.format(f'Run Super Resolution on {f}'))
        img = transforms.functional.to_tensor(np.array(Image.open(f)))


        val = img.shape[2]
        num = int(np.sqrt(val))
        for i in range(1, num+1):
            if val % i == 0:
                slices = i
        print(f'Crop {f} to {slices} slices')
        milestone = [int(val/slices*i) for i in range(1, slices+1)]
        milestone.insert(0,0)
        imgs = [img[:,:,milestone[i]:milestone[i+1]].unsqueeze(0) for i in range(len(milestone)-1)]
        width = 0
        for im in imgs:
            width += im.shape[-1]
        assert width==val, 'incorrect slice'


        file_name = os.path.split(os.path.splitext(f)[0])[-1]
        folder_init('/tmp', file_name)

        model.eval()
        for i, im in enumerate(tqdm(imgs)):
            img = im.to(device)
            output = model(img).to('cpu').squeeze()
            save_image(output, f'/tmp/{file_name}/{i:02d}.jpg')
            del img, output

        slices_files = glob(f'/tmp/{file_name}/*.jpg')
        slices_files.sort()
        slices_imgs = [cv2.imread(slices_file) for slices_file in slices_files]
        whole_image = cv2.hconcat([slices_imgs[0]])
        for i in range(1, len(slices_imgs)):
            whole_image = cv2.hconcat([whole_image, slices_imgs[i]])

        output_name = f'outputs/{file_name}_x{args.scale}_{args.model_size}.jpg'
        cv2.imwrite(output_name, whole_image)
        folder_remove('tmp', file_name)
        print(f"Finish {f}, save in {output_name}")



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--model-size', default='small', type=str, help='Model size: large/small')
    parser.add_argument('-s', '--scale', default=2, type=int, help='Scale size: 2/3/4')
    parser.add_argument('--gpu', action='store_true', help='Using GPU')
    args, _ = parser.parse_known_args()

    main(args)