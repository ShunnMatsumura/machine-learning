# ニューラルネットワーク
## 活性化関数hの登場。
`y = h(b + w1x1 + w2x2)`
hは活性化関数と呼ばれる関数で、入力信号の総和を出力信号に変換する関数。

これが0を超えたら1を返し、そうでなければ0を返す。
「ステップ関数」や「階段関数」とも呼ばれる。

## シグモイド関数
```python
a = np.array(
    [1.0, 2.0, 3.0]
)
y = a > 0 # これで各要素に対して評価される
=> [True, True, True]

これをnumpyのtypesにcastする

y = y.astype(np.int_)

# see types https://numpy.org/doc/stable/user/basics.types.html

活性化関数では線形関数を用いない。用いる意味がない。
why
h = cxとすると、
- h(h(h(x))) = c^3 * h(x) となり、結局定数倍の変化となり線形になる。
よって隠れ層の意味がなくなるので使用しない。

## ReLU関数(Rectified Linear Unit)（正規化線形ユニット）
入力が0を超えていればそのまま出力し、0以下なら0を出力する。


