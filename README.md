# Chicken-Disease-Classification
#Create Virtaul ENV
#conda create -n chicken python=3.10.8 -y
#Activate ENv
#conda activate chicken
#pip install -r requirements.txt
#conda upgrade existing env : conda install python==3.8.5

#zsh: illegal hardware instruction  python
#conda install -n chicken ipykernel --update-deps --force-reinstall
# to resolve this install tensorflow using conda 
# use one of below command 
# conda install -c "conda-forge/label/broken" tensorflow
# conda install -c apple tensorflow-deps
#https://ajeygore.in/content/TensorFlow2-on-macOS-M1-Machines
#if you still face issue use 
#https://www.youtube.com/watch?v=o4-bI_iZKPA
#% conda env create -f tensorflow-apple-metal.yml -n tensorflow
# if you see errors like ModuleNotFoundError: No module named 'cnnClassifier'
# then activa conda envionmet


## Workflows

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the dvc.yaml

#how to see logs
% tensorboard --logdir artifacts/prepare_callbacks/tensorboard_log_dir

#dvc
dvc init
dvc repro