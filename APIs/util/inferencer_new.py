import torch 
import numpy as np
from PIL import Image
import cv2
from matplotlib import pyplot as plt
from torch import nn
import os
from torchvision import transforms,datasets
import PIL
from tqdm import tqdm
import random
from timm.data.constants import IMAGENET_DEFAULT_MEAN, IMAGENET_DEFAULT_STD


class Inferencer(object): 
    
    def __init__(self, model:nn.Module,path:str, cat_info:dict, mode:str='single',label=None, transform=None, 
                 device:str="cuda:0", custom_dataset=None): 
        """_summary_
        Args:
            model (nn.Module): 
            path (str): 이미지 경로 / 테스트 데이터셋 root 경로
            cat_info (dict): categories' information {name: idx} when training data
            mode (str, optional): _description_. Defaults to 'single'.
            label (_type_, optional): for single mode. Defaults to None.
            transform (Compose, optional): augmentation transform. it's depend on model's evaluation setting. 
            Defaults is resizing (224,224) and normalize imagenet's gaussian value.
            device (str, optional): gpu type. Defaults to "cuda:0".
            custom_dataset (_type_, optional): dataset if it's different from ImageFolder class or etc. Defaults to None.
        """
        self.model=model
        self.cat_info=cat_info
        self.mode=mode
        self.device=device
        self.path=path
        
        if transform:
            self.transform=transform
        else:
            self.transform=self._default_transform()

        if mode=='single':
            self.img_tensor=self._path2tensor(path)
            self._visualize(path)
            if label!=None: #해당 사진에 대한 라벨정보 따로 주면 그 라벨이라고 표시
                self.label=label
            else:
                self.label=path.split('/')[-2] #수정해야함
             
        else:
            if custom_dataset:
                self.dataset=custom_dataset
            else:
                self.dataset=self._test_dataset(path)
            
    
    def _default_transform(self, size:int=224):
        mean = IMAGENET_DEFAULT_MEAN
        std = IMAGENET_DEFAULT_STD
        data_transforms = transforms.Compose([
        transforms.Resize(size, interpolation=PIL.Image.BICUBIC),
        transforms.CenterCrop(size),
        transforms.ToTensor(),
        transforms.Normalize(mean, std)
        ])
        return data_transforms
    
    def _path2tensor(self, path): #when single mode
        image = Image.open(path)
        transform=self.transform
        image = transform(image)
        image = image.unsqueeze(0)
        
        return image #default (1,3,224,224) size
    
    def _test_dataset(self, path): #when test mode
        transform=self.transform
        dataset = datasets.ImageFolder(path, transform=transform)
    
        return dataset
    
    def _visualize(self,path, shape:tuple=(224,224)):
        img = np.array(Image.open(path))
        img = cv2.resize(img, shape)
        img = np.float32(img) / 255
        plt.imshow(img)
        return

    def __call__(self,k:int=1, infer_per_num=5, batch_size=32): 
        #single mode
        self.model.eval()
        if self.mode=='single':    
            with torch.no_grad():
                pred=self.model(self.img_tensor.to(self.device))
                prob=nn.Softmax(dim=1)
                pred=prob(pred)
                pred_topk=torch.topk(pred,k)    #한 배치의 topk정보 지님, 형태는 [value= batch size*5 형태, indices=b size*5 형태]
                batch_scores=pred_topk[0]
                batch_indices=pred_topk[1]
            result_dict={} # {"top k": {"Species":"라벨 이름", "percent":~, "plantNo":"카테고리 인덱스", "plantImgs":[샘플파일이름]}}
            
        
            #idx=self.cat_info[self.label] #class index number
            idx2class={v:k for k,v in self.cat_info.items()}
            
            #topk_dict[self.label]=[(batch_scores[0][i].item(),idx2class[batch_indices[0][i].item()]) for i in range(k)] #수정
            #result_dict['url']=self.path # input image path
            #result_dict[f'top{k}_plants']={f'top{n+1}':(batch_scores[0][n].item(),idx2class[batch_indices[0][n].item()]) for n in range(k)}
            infer_imgs=[]
            for n in range(k):
                result_dict[f'top{n+1}']={}
                result_dict[f'top{n+1}']["Species"]=idx2class[batch_indices[0][n].item()] #라벨
               
                result_dict[f'top{n+1}']["Percent"]=batch_scores[0][n].item() #스코어의 소맥 결괏값
                result_dict[f'top{n+1}']["PlantNo"]=self.cat_info[result_dict[f'top{n+1}']["Species"]] #라벨의 인덱스
                                                            
                infer_path="/home/files/datasets/livinglab_cp/val/"+idx2class[batch_indices[0][n].item()] #추론 카테고리 파일 경로
                imgs,sample_paths=self.bring_imgs(infer_path, img_num=infer_per_num, size=224) #샘플링
                infer_imgs+=imgs #추론한 사진
                result_dict[f'top{n+1}']["plantImgs"]=sample_paths #추론한 사진 경로
            
            img_table=self.make_table(infer_imgs,(k,infer_per_num))
            plt.axis("off")
            plt.imshow(img_table)
            
            return result_dict
        
        #test mode(check model's acc)
        else:
            with torch.no_grad():
                dataloader=torch.utils.data.DataLoader(
                self.dataset,batch_size)
                num_data=len(dataloader.dataset)
                correct=0
                for X,y in tqdm(dataloader):
                    X=X.to(self.device)
                    y=y.to(self.device)
                    model=self.model.to(self.device)
                    output=model(X)
                    correct += (output.argmax(1) == y).type(torch.float).sum().item()
                    acc=correct/num_data
                    
                return acc
            
    def bring_imgs(self,path:str,img_num:int, size:int=224):

        img_list=os.listdir(path) #이미지가 들어있는 경로 내의 모든 사진을 받아옴
        original=img_num
        if img_num > len(img_list):
            print('이미지의 갯수가 입력값보다 적어서 폴더 내 모든 사진을 받아옵니다. 사진 갯수: {0}'.format(len(img_list)))
            img_num=len(img_list)
        sampling_list = np.array(random.sample(img_list,img_num)) # 해당 카테고리 사진들중 랜덤하게 img_num개 뽑아옴
        images=[0]*img_num
        img_path=[]
        for i in range(img_num):
            images[i]=os.path.join(path,sampling_list[i])
            img_path.append(images[i])
            img = np.array(Image.open(images[i]))
            if img.shape[2]>3:
                img=img[...,:3] #4채널 이미지 보정 
            
            
            img = cv2.resize(img, (size, size))
            img = np.float32(img) / 255
            images[i]=img
        
        if original!=img_num:
            margin_num=original-img_num
            for i in range(margin_num):
                white_pic=np.ones(img.shape)

                images.append(white_pic)
        
        return images, img_path #(224,224,3) 인 이미지들들을 리스트로 묶어서 반환시킴 / image path 리스트 반환 추가
            
    def make_table(self,images:list,shape:tuple): #images 는 이미지들 담겨있는 리스트임
        """1. 행개수씩 이미지 리스트를 뽑아서 image들 hstack 해줌 (가로사이즈가 5면 인덱스를 0~4, 5~9 ... 가져옴)
        2. hstack 한 이미지를 row_list에 담아줌  
        3. 담은 row이미지들을 튜플로 묶어서 vstack 해줌"""
        #image_table=images[0]
        if (shape[0])*(shape[1])!=len(images):
            raise(ShapeError)

        try:    
            row_list=[]

            for row_idx in range(shape[0]): #row_idx 는 0,1,2
                image_table=images[row_idx*shape[1]] #이러면 images[0] [5] [10] 가져옴 
                #맨처음 받는 image_table 이 행의 앞단이니까 여기에 원본 사진을 받아주면된다.
                #
                for col_idx in range((row_idx*shape[1])+1,(row_idx+1)*(shape[1])):
                    image_table=np.hstack((image_table, images[col_idx]))
                row_list.append(image_table)
            image_table=np.vstack(tuple(row_list))
            #plt.imshow(image_table)
            #plt.show()
            return image_table
        
        except ShapeError as e:
            print(e)  
    
class ShapeError(Exception):
    def __str__(self):
        return "테이블 크기와 입력 이미지 갯수가 맞지 않습니다"