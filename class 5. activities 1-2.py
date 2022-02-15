Python 3.9.7 (v3.9.7:1016ef3790, Aug 30 2021, 16:39:15) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import tensorflow as tf
>>> help(tf)

>>> help(tf.keras)
Help on package keras.api._v2.keras in keras.api._v2:

NAME
    keras.api._v2.keras - Public API for tf.keras namespace.

PACKAGE CONTENTS
    __internal__ (package)
    activations (package)
    applications (package)
    backend (package)
    callbacks (package)
    constraints (package)
    datasets (package)
    estimator (package)
    experimental (package)
    initializers (package)
    layers (package)
    losses (package)
    metrics (package)
    mixed_precision (package)
    models (package)
    optimizers (package)
    premade (package)
    preprocessing (package)
    regularizers (package)
    utils (package)
    wrappers (package)

VERSION
    2.6.0

FILE
    /Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/keras/api/_v2/keras/__init__.py


>>> x=tf.constant([[5,2],[1,3]])
>>> x
<tf.Tensor: shape=(2, 2), dtype=int32, numpy=
array([[5, 2],
       [1, 3]], dtype=int32)>
>>> print(x)
tf.Tensor(
[[5 2]
 [1 3]], shape=(2, 2), dtype=int32)
>>> x.numpy()
array([[5, 2],
       [1, 3]], dtype=int32)
>>> x.dtype
tf.int32
>>> x.shape
TensorShape([2, 2])
>>> x.backing_device
'/job:localhost/replica:0/task:0/device:CPU:0'
>>> tf.ones(shape=(3,3))
<tf.Tensor: shape=(3, 3), dtype=float32, numpy=
array([[1., 1., 1.],
       [1., 1., 1.],
       [1., 1., 1.]], dtype=float32)>
>>> tf.zeros(shape=(2,3))
<tf.Tensor: shape=(2, 3), dtype=float32, numpy=
array([[0., 0., 0.],
       [0., 0., 0.]], dtype=float32)>
>>> tf.random.normal(shape=(2,3))
<tf.Tensor: shape=(2, 3), dtype=float32, numpy=
array([[ 0.09832349, -0.7032827 , -1.0964618 ],
       [ 0.24554513, -0.6020301 ,  0.01505683]], dtype=float32)>
>>> tf.random.normal(shape=(2,3),mean=5,stddev=3)
<tf.Tensor: shape=(2, 3), dtype=float32, numpy=
array([[6.421172 , 9.09531  , 6.0903907],
       [3.3741374, 8.513558 , 3.9523368]], dtype=float32)>
>>> xvar=tf.random.normal(shape=(3,3))
>>> xvar
<tf.Tensor: shape=(3, 3), dtype=float32, numpy=
array([[ 0.94698554, -0.41857463, -1.084111  ],
       [ 0.6477034 , -0.17856488,  0.17043167],
       [-0.14349377,  0.56877255,  0.5643608 ]], dtype=float32)>
>>> a=tf.Variable(xvar)
>>> a
<tf.Variable 'Variable:0' shape=(3, 3) dtype=float32, numpy=
array([[ 0.94698554, -0.41857463, -1.084111  ],
       [ 0.6477034 , -0.17856488,  0.17043167],
       [-0.14349377,  0.56877255,  0.5643608 ]], dtype=float32)>
>>> a.assign(tf.random.normal(shape=(3,3)))
<tf.Variable 'UnreadVariable' shape=(3, 3) dtype=float32, numpy=
array([[ 0.5197064 , -0.36648807,  1.4359951 ],
       [ 0.57693905, -1.1241388 ,  0.9599325 ],
       [-0.32702813,  0.43587163, -1.6489292 ]], dtype=float32)>
>>> xvar_t_add=tf.random.normal(shape=(3,3))
>>> xvar_t_add
<tf.Tensor: shape=(3, 3), dtype=float32, numpy=
array([[-0.61482733, -0.21164237, -1.5352191 ],
       [ 0.15296054, -0.31049472,  1.2469252 ],
       [ 0.29268157,  0.27959663,  0.23733062]], dtype=float32)>
>>> a.assign_add(xvar_t_add)
<tf.Variable 'UnreadVariable' shape=(3, 3) dtype=float32, numpy=
array([[-0.09512091, -0.5781304 , -0.09922397],
       [ 0.7298996 , -1.4346335 ,  2.2068577 ],
       [-0.03434655,  0.7154683 , -1.4115987 ]], dtype=float32)>
>>> a.assign_sub(xvar_t_add)
<tf.Variable 'UnreadVariable' shape=(3, 3) dtype=float32, numpy=
array([[ 0.5197064 , -0.36648804,  1.4359951 ],
       [ 0.57693905, -1.1241388 ,  0.95993245],
       [-0.32702813,  0.43587166, -1.6489294 ]], dtype=float32)>
>>> new_value=tf.random.normal(shape=(3,3))
>>> new_value
<tf.Tensor: shape=(3, 3), dtype=float32, numpy=
array([[-1.4102173 , -0.12351689, -0.88861126],
       [-1.07831   ,  0.57625717, -0.3157859 ],
       [-0.1492991 ,  0.48657718, -1.0254041 ]], dtype=float32)>
>>> a
<tf.Variable 'Variable:0' shape=(3, 3) dtype=float32, numpy=
array([[ 0.5197064 , -0.36648804,  1.4359951 ],
       [ 0.57693905, -1.1241388 ,  0.95993245],
       [-0.32702813,  0.43587166, -1.6489294 ]], dtype=float32)>
>>> a.assign_add(new_value)
<tf.Variable 'UnreadVariable' shape=(3, 3) dtype=float32, numpy=
array([[-0.89051086, -0.49000493,  0.54738384],
       [-0.50137097, -0.54788166,  0.64414656],
       [-0.47632724,  0.9224489 , -2.6743336 ]], dtype=float32)>
>>> b=tf.random.normal(shape=(3,3))
>>> b
<tf.Tensor: shape=(3, 3), dtype=float32, numpy=
array([[ 0.53528106, -0.1598266 , -1.2477301 ],
       [-0.09021463, -0.41506147,  0.50981635],
       [-2.0001512 , -0.02189791, -0.05779134]], dtype=float32)>
>>> c=a+b
>>> c
<tf.Tensor: shape=(3, 3), dtype=float32, numpy=
array([[-0.3552298 , -0.64983153, -0.7003463 ],
       [-0.5915856 , -0.96294314,  1.1539629 ],
       [-2.4764783 ,  0.90055096, -2.7321248 ]], dtype=float32)>
>>> d=tf.square(c)
>>> d
<tf.Tensor: shape=(3, 3), dtype=float32, numpy=
array([[0.1261882 , 0.42228103, 0.49048492],
       [0.3499735 , 0.9272595 , 1.3316302 ],
       [6.132945  , 0.81099206, 7.464506  ]], dtype=float32)>
>>> e=tf.exp(c)
>>> e
<tf.Tensor: shape=(3, 3), dtype=float32, numpy=
array([[0.7010123 , 0.5221337 , 0.49641338],
       [0.55344903, 0.38176763, 3.1707332 ],
       [0.08403866, 2.4609587 , 0.06508086]], dtype=float32)>
>>> with tf.GradientTape() as tape:
	tape.watch(a)
	f=tf.sqrt(tf.squqre(a)+tf.square(b))
	df_da=tape.gradient(f,a)
	print(df_da)

	
Traceback (most recent call last):
  File "<pyshell#43>", line 3, in <module>
    f=tf.sqrt(tf.squqre(a)+tf.square(b))
AttributeError: module 'tensorflow' has no attribute 'squqre'
>>> with tf.GradientTape() as tape:
	tape.watch(a)
	f=tf.sqrt(tf.square(a)+tf.square(b))
	df_da=tape.gradient(f,a)
	print(df_da)

	
tf.Tensor(
[[-0.85707885 -0.95070565  0.40174383]
 [-0.98419434 -0.7970924   0.78412473]
 [-0.23166692  0.99971837 -0.9997666 ]], shape=(3, 3), dtype=float32)
>>> 