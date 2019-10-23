# GetSvImgs

Automatically collect images around the specified latitude and longitude from Google Street View.  
Various parameters such as size can be set for the image.  
Intended for use in machine learning.  
Population density, land prices, urbanity, etc.  
指定された緯度と経度の周りの画像をGoogle Street Viewから自動的に収集します。  
サイズをはじめとしたさまざまなパラメータが設定可能です。  
機械学習での使用を想定しています。  
人口密度、地価、都会度など  

## Demo

35.170915,136.8815369 ±5km  
<img src="https://github.com/satoki/getsvimgs/blob/images/N_i.png" width=70%>  

35.17197185210667,136.88454288022737 (400x400)  
North  
<img src="https://github.com/satoki/getsvimgs/blob/images/N_35.17197185210667%2C136.88454288022737.jpg" width=30%>  
South  
<img src="https://github.com/satoki/getsvimgs/blob/images/S_35.17197185210667%2C136.88454288022737.jpg" width=30%>  
East  
<img src="https://github.com/satoki/getsvimgs/blob/images/E_35.17197185210667%2C136.88454288022737.jpg" width=30%>  
West  
<img src="https://github.com/satoki/getsvimgs/blob/images/W_35.17197185210667%2C136.88454288022737.jpg" width=30%>  

## Usage

Set all variables starting with "\_" such as _api_key in the main function.  
main関数内の_api_keyなど"\_"から始まる変数を設定してください。  

```console
$ pip3 install tqdm
$ python3 GetSvImgs.py
```

## Author

[Satoki](https://github.com/satoki)  