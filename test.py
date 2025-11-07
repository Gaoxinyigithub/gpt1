# todo 手动编译是否可用
import tensorflow as tf

# Force a simple operation on the GPU
with tf.device("/GPU:0"):
    a = tf.random.normal([10000, 10000])
    b = tf.random.normal([10000, 10000])
    c = tf.matmul(a, b)

print("Result shape:", c.shape)
print("Device placement:", c.device)