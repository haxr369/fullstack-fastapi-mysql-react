from core.config import settings
import torch
from ML.models.vit import vit_large_patch16
from ML.models.inferencer import Inferencer
import json

    
def load_model(device="cuda", pretrained=True):
    model=vit_large_patch16(num_classes=116,
            drop_path_rate=0.1,
            global_pool=False).to(device)
    
    if pretrained==True:
        ckpt_path= settings.ML_PARMS
        finetuned_weight=torch.load(ckpt_path)
        model.load_state_dict(finetuned_weight['model'])
    
    return model


def inference(model, path, k=3, num_samples=5):
    #bring cat_info
    with open(settings.CATEGORY_INFO, 'r') as fp:
        cat_info = json.load(fp)
    
    
    infer=Inferencer(model, path, cat_info)
    
    return infer(k, num_samples)

#Global model load

device = torch.device("cuda")
print(device)
if(device):
    MAE_Model = load_model(device='cuda')
    print("GPU 서비스 시작!!")
else: MAE_Model = load_model(device='cpu')

"""

checkPlants = ['자귀나무', '층층나무', '단풍나무', '병아리꽃나무','나무수국', 
                '산수국', '상수리나무', '명자나무', '살구나무', 
                '고광나무', '대왕참나무','영산홍', '박태기나무','측백나무', '메타세쿼이아',
                '모감주나무', '백당나무', '마가목', 
                '산사나무', '분꽃나무','붉은병꽃나무', '느티나무', '은행나무','중국단풍', 
                '실유카', '귀룽나무', '미선나무','산수유나무', '이팝나무', '스트로브잣나무']

import torchvision.transforms as transforms
from torchvision.datasets import ImageFolder

# 데이터셋의 루트 폴더 경로
data_dir = '/code/app/Sample_images/test'

# 이미지 전처리를 위한 transform 정의
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

# 데이터셋 로드
dataset = ImageFolder(data_dir, transform=transform)
print(dataset)
"""