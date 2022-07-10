# pyVisa 利用方法

## 概要

- 計測機器を VISA を使って操作する
- pyVISA というライブラリを使って PC からリモート操作
- 利便性を上げるため下記の機器用のモジュールを作成
  - 発信機、オシロスコープ、ステージコントローラー

## モジュール説明

```python
!pip install pyvisa
import devise
```

上記を行うことで、発信機、オシロスコープ、ステージコントローラーのクラスが使用可能

## クラス説明

### FunctionGenerater クラス

#### メソッド一覧

- move_plus(axis,pulsecount):
  - #移動量指定(正方向移動)　パルス数で指定(三軸ごとに 1 パルスの移動量が違うので)
- move_minus(axis,pulsecount):
  - #移動量指定(負方向移動)　パルス数で指定(三軸ごとに 1 パルスの移動量が違うので)
- to_zero():
  - #原点復帰
- set_zero():
  - #原点指定
- move_to(1 軸 pulsecount,2 軸,3 軸,4 軸):
  - #移動場所指定

### oscilloscope クラス

#### メソッド一覧

- fetch(channel): return time, Volts
  - #波形を取得するチャンネル名指定，例 fetch(1)
- average(count): return ave_count
  - #averaging 数指定

### functionGenerater
