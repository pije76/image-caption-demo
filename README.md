# image-caption-demo
[![MIT License](https://img.shields.io/github/license/mashape/apistatus.svg)](https://opensource.org/licenses/MIT)
[![Torch7](https://img.shields.io/badge/torch-7-orange.svg)](http://torch.ch/)
[![neuraltalk2](https://img.shields.io/badge/neuraltalk-2-blue.svg)](https://github.com/karpathy/neuraltalk2)
[![Django1.9](https://img.shields.io/badge/Django-1.9-yellowgreen.svg)](https://github.com/django/django)  
A basic image caption project based on [torch](https://github.com/torch/torch7), [neuraltalk2](https://github.com/karpathy/neuraltalk2)  and [django](https://github.com/django/django).  

# Requirement
 1. torch7  
	installing tutorial: <http://torch.ch/docs/getting-started.html#_>
 2. neuraltalk2  
	installing tutorial: <https://github.com/karpathy/neuraltalk2>
 3. Django  
	install using `pip`: `sudo pip install Django`
 4. Pretrained models 
	Read tutorial in neuraltalk2 to get the pretrained models.


# Running
 1. After you download pretained models, put them in the folder `model` in `video_cap` subdirectory.
 2. Get into root directory of this repository, run commands below:  
 ```shell
	cd ./video_cap/
	python manage.py runserver 0.0.0.0:8000
 ``` 
 Then you will see the website running on the Internet!


#Author
 Yunfeng Wang([vra](https://github.com/vra))  
 Qing Li([liqing-ustc](https://github.com/liqing-ustc))  
 Yiding Liu([xck36](https://github.com/xck36))  
 Junfu Pu([Jevin754](https://github.com/Jevin754))  

#License
 MIT
