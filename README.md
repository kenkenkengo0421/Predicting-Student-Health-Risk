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
|カロリー消費量|[calorie_expenditure.ipynb](https://github.com/kenkenkengo0421/Predicting-Student-Health-Risk/blob/main/sub/calorie_expenditure.ipynb)|1400以下は不健康の傾向あり1400kcalは一般的に、運動を含めた1日の摂取カロリーの目安 それ以下の方たちが不健康の傾向あり|
|ステップ数|[step_count.ipynb](https://github.com/kenkenkengo0421/Predicting-Student-Health-Risk/blob/main/sub/step_count.ipynb)|水色と赤色（不健康・リスクあり）が 5000より下|
|運動時間|[exercise_duration.ipynb](https://github.com/kenkenkengo0421/Predicting-Student-Health-Risk/blob/main/sub/exercise_duration.ipynb)|40時間以上運動者は健康的な傾向あり|
|水分摂取量|[water_intake.ipynb](https://github.com/kenkenkengo0421/Predicting-Student-Health-Risk/blob/main/sub/water_intake.ipynb)|水分摂取量はあまり関連性がなさそう|
|食事タイプ|[diet_type.ipynb](https://github.com/kenkenkengo0421/Predicting-Student-Health-Risk/blob/main/sub/diet_type.ipynb)|野菜中心、バランスの取れた食生活の方が健康的|
|ストレスレベル|[stress_level.ipynb](https://github.com/kenkenkengo0421/Predicting-Student-Health-Risk/blob/main/sub/stress_level.ipynb)|High : 不健康の割合高い、健康の割合がかなり低い、medium : 不健康の割合低い、健康の割合がかなり低い、予備軍高い、low : 不健康の割合低い、健康の割合がかなり高い|
|睡眠の質|[sleep_quality.ipynb](https://github.com/kenkenkengo0421/Predicting-Student-Health-Risk/blob/main/sub/sleep_quality.ipynb)|average 平均的：　健康的、good 良い ： 不健康的、poor 良くない ：　健康的|
|身体活動レベル|[physical_activity_level.ipynb](https://github.com/kenkenkengo0421/Predicting-Student-Health-Risk/blob/main/sub/physical_activity_level.ipynb)|sedentary：座りがち、運動量が少ない、moderate：適度な運動量、平均的、active：活発、よく運動する 運動する人でも不健康な方がそれなりにいるが比率は健康が多い|
|喫煙・飲酒|[smoking_alcohol.ipynb](https://github.com/kenkenkengo0421/Predicting-Student-Health-Risk/blob/main/sub/smoking_alcohol.ipynb)|yes：習慣がある（よく吸う・飲む）、no：習慣がない（吸わない・飲まない）、occasional：たまに（時々）吸う・飲む 吸う人、たまに吸う人が不健康の傾向あり|
|性別|[gender.ipynb](https://github.com/kenkenkengo0421/Predicting-Student-Health-Risk/blob/main/sub/gender.ipynb)|male：男性の方がやや健康傾向あり、female：女性　不健康傾向あり、other：その他　不健康傾向あり|
|運動の強度|[exercise_strength.ipynb](https://github.com/kenkenkengo0421/Predicting-Student-Health-Risk/blob/main/sub/exercise_strength.ipynb)|$$\text{運動強度} = \frac{\text{消費カロリー}}{(\text{運動時間} + 0.1) \times \text{BMI}}$$|
|健康、不健康スコア|[score.ipynb.ipynb](https://github.com/kenkenkengo0421/Predicting-Student-Health-Risk/blob/main/sub/score.ipynb)|内部参照|
|ストレス係数:ストレスレベル/睡眠時間|[stress_per_sleep.ipynb](https://github.com/kenkenkengo0421/Predicting-Student-Health-Risk/blob/main/sub/stress_per_sleep.ipynb)|$$ \text{ストレス指数} = \frac{\text{ストレスレベル}}{\text{睡眠時間}} $$|

</details>


# スコアの履歴

<details><summary>スコアリスト</summary> 

### [Balanced Accuracy（均衡正解率）](https://github.com/kenkenkengo0421/learning-math/blob/main/Balanced%20Accuracy/Balanced%20Accuracy.md)


|バージョン|結果|コンペ結果|備考|
|-----|-----|-----|-----|
|v0.0  | 0.95011 | 0.94639 |2026_07_12 852位|
|v0.1 | 0.95007 | 0.94639 |2026_07_12 960位|
|v0.2|0.95018|0.94668|2026_07_17 1221位|
|v0.3|0.95016|0.94844|2026_07_17 1156位|
|v0.4|0.95032|0.94877|2026_07_18 1135位|
|v0.5|0.95021|0.94916|2026_07_18 1088位|
|v0.6|0.95036|0.94936|2026_07_18 1032位|
|v0.7|0.95041|0.94901|2026_07_19 1085位|
|v0.8|0.95015|0.94927|2026_07_20 1151位|
|v0.9|0.95016|0.94861|2026_07_21 1163位|
|v1.0|0.95002|0.94875|2026_07_21 1186位|

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
