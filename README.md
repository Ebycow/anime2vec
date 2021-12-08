# anime2vec
[MyAnimeList Database 2020](https://github.com/Hernan4444/MyAnimeList-Database) により学習されたアニメ作品の埋め込み表現

## Embedding Projector
https://projector.tensorflow.org/?config=https://raw.githubusercontent.com/Ebycow/anime2vec/main/anime2vec_projector_config.json

![projector](https://raw.githubusercontent.com/Ebycow/anime2vec/main/projector.png)

## predict.py (sample)
類似作品の表示
```
showSimilar("34798") # MAL_IDを指定 anime.csv もしくはMyAnimeListから取得
```
```
['ゆるキャン△']
['宇宙よりも遠い場所'] ('35839', 0.8266942501068115)
['少女終末旅行'] ('35838', 0.7220398783683777)
['SHIROBAKO'] ('25835', 0.6536941528320312)
['小林さんちのメイドラゴン'] ('33206', 0.6493433117866516)
['こみっくがーるず'] ('35756', 0.6196874976158142)        
['ゾンビランドサガ'] ('37976', 0.612119734287262)
['あそびあそばせ'] ('37171', 0.6104506850242615)
['ブレンド・S'] ('34618', 0.5939446687698364)
['ヒナまつり'] ('36296', 0.5884111523628235)
['ゆるキャン△'] ('37341', 0.5867951512336731)
```

## 作成方法
[MyAnimeList Database 2020](https://github.com/Hernan4444/MyAnimeList-Database) データセットを用いてword2vecにより作成  
作品評価データ(rating_complete.csv)より、ユーザごとに同評価値の作品を1sentenceとして学習

学習パラメータとして、vector_size=100, epochs=100, window=1000, min_count=0