# GetSvImgs

Automatically collect images around the specified latitude and longitude.  
Various parameters such as size can be set for the image.  
Intended for use in machine learning.  
Population density, land prices, urbanity, etc.  
指定された緯度と経度の周りの画像を自動的に収集します。  
画像はサイズをはじめとしたさまざまなパラメータが設定可能です。  
機械学習での使用を想定しています。  
人口密度、地価、都会度など  

## Demo

35.170915,136.8815369 ±5km
<img src="https://github.com/satoki/getsvimgs/blob/images/N_i.png" width=70%>  

35.17197185210667,136.88454288022737  
400x400  
North
<img src="https://github.com/satoki/getsvimgs/blob/images/N_35.17197185210667%2C136.88454288022737.jpg" width=60%>  
South
<img src="https://github.com/satoki/getsvimgs/blob/images/S_35.17197185210667%2C136.88454288022737.jpg" width=60%>  
East
<img src="https://github.com/satoki/getsvimgs/blob/images/E_35.17197185210667%2C136.88454288022737.jpg" width=60%>  
West
<img src="https://github.com/satoki/getsvimgs/blob/images/W_35.17197185210667%2C136.88454288022737.jpg" width=60%>  

## Usage

Set a variable starting with "_" and APIKEY in the main function.  
main関数内の"_"から始まる変数とAPIKEYを設定してください。  

```console
$ pip3 install tqdm
$ python3 GetSvImgs.py
```

## Author

[Satoki](https://github.com/satoki)  