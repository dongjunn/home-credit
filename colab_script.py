import os
os.environ['KAGGLE_USERNAME']= "junjordan"
os.environ['KAGGLE_KEY']="43f107879795cb44e5809b1e0e212d7b"
!kaggle competitions download -c home-credit-default-risk
if not os.path.exists("/content/competitions/home-credit-default-risk"):
    os.makedirs("/content/competitions/home-credit-default-risk")
os.chdir('/content/competitions/home-credit-default-risk')
for file in os.listdir():
    zip_ref = zipfile.ZipFile(file, 'r')
    zip_ref.extractall()
    zip_ref.close()


!git clone https://github.com/dongjunn/home-credit.git
os.chdir('home-credit')
!pip3 install -r requirements.txt
