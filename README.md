
# [Predicting Student Health Risk](https://www.kaggle.com/competitions/playground-series-s6e7/overview)

# コンペの概要

 
  
* **目標** : 学生の健康リスクを予測すること
* **最終提出期限**：2026年7月31日



# 評価



提出された内容は、予測されたクラスと観測されたターゲットとの間の [ balanced_accuracy_score ](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.balanced_accuracy_score.html) に基づいて評価されます



# 提出ファイル



テストセット内の各IDについて、health_condition変数にラベル（リスクあり、不健康、健康）を予測する必要があります。ファイルにはヘッダーが含まれ、以下の形式である必要があります。
```
id,health_condition 
690088,at-risk 
690089,at-risk 
690090,at-risk 
etc.
```


# 特徴



```
id : id
health_condition : 健康状態  (y)
sleep_duration : 睡眠時間
heart_rate : 心拍数
bmi : BMI
calorie_expenditure :  カロリー消費量
step_count : ステップ数
exercise_duration : 運動時間
water_intake : 水分摂取量
diet_type : 食事タイプ
stress_level : ストレスレベル
sleep_quality : 睡眠の質
physical_activity_level : 身体活動レベル
smoking_alcohol : 喫煙・飲酒
gender : 性別
```


* 現在の加工データ : [submit_x_x_x_x_x_x.csv](https://github.com/kenkenkengo0421/Predicting-Student-Health-Risk/blob/main/submit_x_x_x_x_x_x.csv)
  
* メモ : [memo.md](https://github.com/kenkenkengo0421/Predicting-Student-Health-Risk/blob/main/memo.md)



# 調査、分析

<details><summary>調査リスト</summary> 

|名称|URLリンク|備考欄|
|-----|-----|-----|
|睡眠時間|[sleep_duration.ipynb](https://github.com/kenkenkengo0421/Predicting-Student-Health-Risk/blob/main/sub/sleep_duration.ipynb)|睡眠時間が短い（5〜6時間）と不健康な人が多く、しっかり寝ている（7〜8時間）と健康な人が多い|
|心拍数|[heart_rate.ipynb](https://github.com/kenkenkengo0421/Predicting-Student-Health-Risk/blob/main/sub/heart_rate.ipynb)|心拍数はあまり関連性がなさそう|
|BMI|[bmi.ipynb](https://github.com/kenkenkengo0421/Predicting-Student-Health-Risk/blob/main/sub/bmi.ipynb)|27以降が不健康な傾向にある。19以下は健康、不健康な人がほぼいない。|
|カロリー消費量|[calorie_expenditure.ipynb](https://github.com/kenkenkengo0421/Predicting-Student-Health-Risk/blob/main/sub/)|1400以下は不健康の傾向あり1400kcalは一般的に、運動を含めた1日の摂取カロリーの目安 それ以下の方たちが不健康の傾向あり|
|ステップ数|未調査||
|運動時間|未調査||
|水分摂取量|未調査||
|食事タイプ|未調査||
|ストレスレベル|未調査||
|睡眠の質|未調査||
|身体活動レベル|未調査||
|喫煙・飲酒|未調査||
|性別|未調査||

</details>

# スコアの履歴

<details><summary>スコアリスト</summary> 

### [Balanced Accuracy（均衡正解率）](https://github.com/kenkenkengo0421/learning-math/blob/main/Balanced%20Accuracy/Balanced%20Accuracy.md)


|バージョン|結果|コンペ結果|備考|
|-----|-----|-----|-----|
|v0.0  | 0.95011 | 0.94639 |2026_07_12 852位|
|v0.1 | 0.95007 | 0.94639 |2026_07_12 960位|

</details>

# 環境構築( windows )

<details><summary></summary>

cloneする
```PowerShell
git clone https://github.com/kenkenkengo0421/Predicting-Student-Health-Risk.git

```

<br>

zip解凍
```PowerShell
 Expand-Archive -Path .\data.zip
```

<br>

venv構築
```PowerShell
py -m venv .venv
```
<br>

venv有効化
```PowerShell
.\.venv\Scripts\Activate.ps1
```
<br>

必要pipinstall
```PowerShell
pip install -r requirements.txt
```

<br>

nb起動
```PowerShell
jupyter lab
```

</details>
