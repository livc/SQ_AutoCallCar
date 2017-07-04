# 首汽约车自动叫车

首汽约车每次叫车会持续两分钟，没有车的话需要重新手动下单，非常影响正常的工作效率。这个脚本可以在进行简单的配置后，实现自动叫车的功能。

## 配置

`config.py` 为需要自定义的配置，具体包括：

### Cookie

Cookie 需要在[首汽 Web 界面](http://m.01zhuanche.com/touch/h5Home/wxpub/n_jishi)下单，通过抓包获取。

![](http://ww1.sinaimg.cn/large/9cd77f2ely1fh85oobf1rj20zc0ay0wg.jpg)

### 预约时间

`BookTime = '%Y-%m-%d 21:10:36'` 默认为当日的 21:10 分。

如果是即时用车，只需把 `#curr_ime = str(int(time.time()))` 一行取消注释即可。

### 上下车位置

这里需要填上下车位置的中文名字，会显示在 APP 的订单上。

### 上下车经纬度坐标

上下车的坐标需要使用**高德地图**来获取，坐标拾取的地址是<http://lbs.amap.com/console/show/picker>。

注意不能使用其他地图，因为各个地图的经纬度有一些差距，我不会说我最开始用百度地图拾的坐标，司机差点给我开到高速上去了。。。

## 开始使用

Enjoy！

```python
python call.py
```
