from core.config import settings
import torch
from ML.models.vit import vit_large_patch16
from ML.models.inferencer import Inferencer
import json

    
def load_model(device="cuda", pretrained=True):
    model=vit_large_patch16(num_classes=44,
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
    
    infer(k, num_samples)
    print(infer(k, num_samples))
#Global model load
device = torch.device("cuda")
if(device):
    MAE_Model = load_model(device='cuda')
    print("GPU 서비스 시작!!")
else: MAE_Model = load_model(device='cpu')