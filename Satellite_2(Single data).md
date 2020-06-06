```python
import pandas as pd
import numpy as np
import sys

import os
import matplotlib.pyplot as plt
from dplython import *

from scipy.stats import linregress
from IPython.display import Image

from mpl_toolkits.basemap import Basemap

from matplotlib.colors import Normalize
import matplotlib
import matplotlib.cm as cm
import seaborn as sns
from matplotlib import rcParams
from netCDF4 import Dataset

import struct
import binascii
from mpl_toolkits.basemap import addcyclic
from netCDF4 import num2date, date2num, date2index
import datetime

from pyhdf.SD import SD, SDC
import h5py
import glob

%matplotlib inline
```

    C:\Users\hahw9\Anaconda3\envs\cuda\lib\importlib\_bootstrap.py:219: RuntimeWarning: numpy.ufunc size changed, may indicate binary incompatibility. Expected 192 from C header, got 216 from PyObject
      return f(*args, **kwds)
    C:\Users\hahw9\Anaconda3\envs\cuda\lib\importlib\_bootstrap.py:219: RuntimeWarning: numpy.ufunc size changed, may indicate binary incompatibility. Expected 192 from C header, got 216 from PyObject
      return f(*args, **kwds)
    C:\Users\hahw9\Anaconda3\envs\cuda\lib\importlib\_bootstrap.py:219: RuntimeWarning: numpy.ufunc size changed, may indicate binary incompatibility. Expected 192 from C header, got 216 from PyObject
      return f(*args, **kwds)
    C:\Users\hahw9\Anaconda3\envs\cuda\lib\importlib\_bootstrap.py:219: RuntimeWarning: numpy.ufunc size changed, may indicate binary incompatibility. Expected 192 from C header, got 216 from PyObject
      return f(*args, **kwds)
    


```python
Dataset = glob.glob('dataset/*.hdf')
print(len(Dataset))
```

    16
    


```python
list_index = 15
# 0 <= list_index < len(Dataset)
```


```python
for data_name in Dataset:
    print(data_name)
```

    dataset\GOCI_Yonsei_Aerosol_V2_20110301001642.hdf
    dataset\GOCI_Yonsei_Aerosol_V2_20110301011642.hdf
    dataset\GOCI_Yonsei_Aerosol_V2_20110301021642.hdf
    dataset\GOCI_Yonsei_Aerosol_V2_20110301031642.hdf
    dataset\GOCI_Yonsei_Aerosol_V2_20110301041642.hdf
    dataset\GOCI_Yonsei_Aerosol_V2_20110301051642.hdf
    dataset\GOCI_Yonsei_Aerosol_V2_20110301061642.hdf
    dataset\GOCI_Yonsei_Aerosol_V2_20110301071642.hdf
    dataset\GOCI_Yonsei_Aerosol_V2_20110302001640.hdf
    dataset\GOCI_Yonsei_Aerosol_V2_20110302011640.hdf
    dataset\GOCI_Yonsei_Aerosol_V2_20110302021640.hdf
    dataset\GOCI_Yonsei_Aerosol_V2_20110302031640.hdf
    dataset\GOCI_Yonsei_Aerosol_V2_20110302041640.hdf
    dataset\GOCI_Yonsei_Aerosol_V2_20110302051640.hdf
    dataset\GOCI_Yonsei_Aerosol_V2_20110302061640.hdf
    dataset\GOCI_Yonsei_Aerosol_V2_20110302071640.hdf
    


```python
hdffile = Dataset[list_index]
hdffile_sd = SD(hdffile, SDC.READ)

print(hdffile_sd.info())


dataset_dic = hdffile_sd.datasets()
for idx, info in enumerate(dataset_dic):
    print(idx, info)
    temp = hdffile_sd.select(info)
    data = temp.get()
    print(data.shape)
```

    (15, 2)
    0 Longitude
    (473, 463)
    1 Latitude
    (473, 463)
    2 Observation_Minute_UTC
    (473, 463)
    3 Land_Ocean_Mask
    (473, 463)
    4 Aerosol_Optical_Depth_550nm
    (473, 463)
    5 Fine_Mode_Fraction_550nm
    (473, 463)
    6 Single_Scattering_Albedo_440nm
    (473, 463)
    7 Angstrom_Exponent_440_870nm
    (473, 463)
    8 Aerosol_Type
    (473, 463)
    9 Multiple_Prognostic_Expected_Error_AOD550
    (473, 463)
    10 Flag
    (473, 463)
    11 No_of_Used_500m_Pixels_for_One_6km_Product_Pixel
    (473, 463)
    12 NDVI_from_TOA_Reflectance_660_865nm
    (473, 463)
    13 Dust_Aerosol_Index_from_412_443nm
    (473, 463)
    14 Difference_660nm_for_Ocean_Turbidity_Check
    (473, 463)
    


```python
temp = hdffile_sd.select('Longitude')
lon2d = temp.get()
temp = hdffile_sd.select('Latitude')
lat2d = temp.get()
temp = hdffile_sd.select('Aerosol_Optical_Depth_550nm')
AOD = temp.get()

print(lon2d.shape, lat2d.shape, AOD.shape)
```

    (473, 463) (473, 463) (473, 463)
    


```python
df_lon = pd.DataFrame(lon2d)
df_lat = pd.DataFrame(lat2d)
```


```python
df_lon
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>8</th>
      <th>9</th>
      <th>...</th>
      <th>453</th>
      <th>454</th>
      <th>455</th>
      <th>456</th>
      <th>457</th>
      <th>458</th>
      <th>459</th>
      <th>460</th>
      <th>461</th>
      <th>462</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>111.370544</td>
      <td>111.450150</td>
      <td>111.529762</td>
      <td>111.609383</td>
      <td>111.689011</td>
      <td>111.768654</td>
      <td>111.848305</td>
      <td>111.927971</td>
      <td>112.007637</td>
      <td>112.087326</td>
      <td>...</td>
      <td>147.840744</td>
      <td>147.920471</td>
      <td>148.000183</td>
      <td>148.079880</td>
      <td>148.159576</td>
      <td>148.239258</td>
      <td>148.318939</td>
      <td>148.398605</td>
      <td>148.478256</td>
      <td>148.557892</td>
    </tr>
    <tr>
      <th>1</th>
      <td>111.389893</td>
      <td>111.469414</td>
      <td>111.548950</td>
      <td>111.628494</td>
      <td>111.708046</td>
      <td>111.787613</td>
      <td>111.867188</td>
      <td>111.946770</td>
      <td>112.026367</td>
      <td>112.105972</td>
      <td>...</td>
      <td>147.822144</td>
      <td>147.901794</td>
      <td>147.981430</td>
      <td>148.061066</td>
      <td>148.140671</td>
      <td>148.220291</td>
      <td>148.299881</td>
      <td>148.379471</td>
      <td>148.459045</td>
      <td>148.538605</td>
    </tr>
    <tr>
      <th>2</th>
      <td>111.409172</td>
      <td>111.488617</td>
      <td>111.568077</td>
      <td>111.647545</td>
      <td>111.727020</td>
      <td>111.806511</td>
      <td>111.886009</td>
      <td>111.965515</td>
      <td>112.045029</td>
      <td>112.124557</td>
      <td>...</td>
      <td>147.803604</td>
      <td>147.883179</td>
      <td>147.962738</td>
      <td>148.042297</td>
      <td>148.121826</td>
      <td>148.201355</td>
      <td>148.280884</td>
      <td>148.360382</td>
      <td>148.439896</td>
      <td>148.519379</td>
    </tr>
    <tr>
      <th>3</th>
      <td>111.428398</td>
      <td>111.507767</td>
      <td>111.587151</td>
      <td>111.666534</td>
      <td>111.745941</td>
      <td>111.825348</td>
      <td>111.904770</td>
      <td>111.984200</td>
      <td>112.063644</td>
      <td>112.143089</td>
      <td>...</td>
      <td>147.785126</td>
      <td>147.864624</td>
      <td>147.944107</td>
      <td>148.023575</td>
      <td>148.103043</td>
      <td>148.182495</td>
      <td>148.261932</td>
      <td>148.341370</td>
      <td>148.420792</td>
      <td>148.500214</td>
    </tr>
    <tr>
      <th>4</th>
      <td>111.447563</td>
      <td>111.526855</td>
      <td>111.606155</td>
      <td>111.685471</td>
      <td>111.764793</td>
      <td>111.844131</td>
      <td>111.923477</td>
      <td>112.002831</td>
      <td>112.082191</td>
      <td>112.161568</td>
      <td>...</td>
      <td>147.766708</td>
      <td>147.846130</td>
      <td>147.925537</td>
      <td>148.004929</td>
      <td>148.084320</td>
      <td>148.163696</td>
      <td>148.243057</td>
      <td>148.322418</td>
      <td>148.401764</td>
      <td>148.481094</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>468</th>
      <td>116.417877</td>
      <td>116.476929</td>
      <td>116.535980</td>
      <td>116.595024</td>
      <td>116.654060</td>
      <td>116.713089</td>
      <td>116.772118</td>
      <td>116.831139</td>
      <td>116.890160</td>
      <td>116.949173</td>
      <td>...</td>
      <td>142.996948</td>
      <td>143.055939</td>
      <td>143.114929</td>
      <td>143.173935</td>
      <td>143.232925</td>
      <td>143.291946</td>
      <td>143.350952</td>
      <td>143.409973</td>
      <td>143.468994</td>
      <td>143.528030</td>
    </tr>
    <tr>
      <th>469</th>
      <td>116.423233</td>
      <td>116.482262</td>
      <td>116.541290</td>
      <td>116.600304</td>
      <td>116.659325</td>
      <td>116.718330</td>
      <td>116.777336</td>
      <td>116.836342</td>
      <td>116.895332</td>
      <td>116.954323</td>
      <td>...</td>
      <td>142.991821</td>
      <td>143.050797</td>
      <td>143.109772</td>
      <td>143.168747</td>
      <td>143.227722</td>
      <td>143.286713</td>
      <td>143.345703</td>
      <td>143.404694</td>
      <td>143.463699</td>
      <td>143.522705</td>
    </tr>
    <tr>
      <th>470</th>
      <td>116.428566</td>
      <td>116.487572</td>
      <td>116.546577</td>
      <td>116.605576</td>
      <td>116.664574</td>
      <td>116.723557</td>
      <td>116.782539</td>
      <td>116.841522</td>
      <td>116.900497</td>
      <td>116.959465</td>
      <td>...</td>
      <td>142.986725</td>
      <td>143.045670</td>
      <td>143.104614</td>
      <td>143.163574</td>
      <td>143.222534</td>
      <td>143.281494</td>
      <td>143.340469</td>
      <td>143.399445</td>
      <td>143.458420</td>
      <td>143.517395</td>
    </tr>
    <tr>
      <th>471</th>
      <td>116.433884</td>
      <td>116.492874</td>
      <td>116.551857</td>
      <td>116.610832</td>
      <td>116.669800</td>
      <td>116.728767</td>
      <td>116.787727</td>
      <td>116.846687</td>
      <td>116.905640</td>
      <td>116.964584</td>
      <td>...</td>
      <td>142.981628</td>
      <td>143.040558</td>
      <td>143.099487</td>
      <td>143.158417</td>
      <td>143.217346</td>
      <td>143.276291</td>
      <td>143.335236</td>
      <td>143.394196</td>
      <td>143.453156</td>
      <td>143.512115</td>
    </tr>
    <tr>
      <th>472</th>
      <td>116.439194</td>
      <td>116.498154</td>
      <td>116.557114</td>
      <td>116.616074</td>
      <td>116.675018</td>
      <td>116.733963</td>
      <td>116.792908</td>
      <td>116.851837</td>
      <td>116.910767</td>
      <td>116.969696</td>
      <td>...</td>
      <td>142.976562</td>
      <td>143.035461</td>
      <td>143.094360</td>
      <td>143.153275</td>
      <td>143.212189</td>
      <td>143.271103</td>
      <td>143.330032</td>
      <td>143.388962</td>
      <td>143.447906</td>
      <td>143.506836</td>
    </tr>
  </tbody>
</table>
<p>473 rows × 463 columns</p>
</div>




```python
df_lat
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>8</th>
      <th>9</th>
      <th>...</th>
      <th>453</th>
      <th>454</th>
      <th>455</th>
      <th>456</th>
      <th>457</th>
      <th>458</th>
      <th>459</th>
      <th>460</th>
      <th>461</th>
      <th>462</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>46.970455</td>
      <td>46.981075</td>
      <td>46.991650</td>
      <td>47.002178</td>
      <td>47.012661</td>
      <td>47.023098</td>
      <td>47.033489</td>
      <td>47.043835</td>
      <td>47.054131</td>
      <td>47.064384</td>
      <td>...</td>
      <td>47.073742</td>
      <td>47.063530</td>
      <td>47.053276</td>
      <td>47.042973</td>
      <td>47.032627</td>
      <td>47.022232</td>
      <td>47.011791</td>
      <td>47.001305</td>
      <td>46.990772</td>
      <td>46.980190</td>
    </tr>
    <tr>
      <th>1</th>
      <td>46.916790</td>
      <td>46.927399</td>
      <td>46.937962</td>
      <td>46.948479</td>
      <td>46.958950</td>
      <td>46.969372</td>
      <td>46.979752</td>
      <td>46.990082</td>
      <td>47.000366</td>
      <td>47.010609</td>
      <td>...</td>
      <td>47.019951</td>
      <td>47.009754</td>
      <td>46.999512</td>
      <td>46.989223</td>
      <td>46.978886</td>
      <td>46.968506</td>
      <td>46.958076</td>
      <td>46.947605</td>
      <td>46.937084</td>
      <td>46.926517</td>
    </tr>
    <tr>
      <th>2</th>
      <td>46.863136</td>
      <td>46.873730</td>
      <td>46.884281</td>
      <td>46.894783</td>
      <td>46.905239</td>
      <td>46.915653</td>
      <td>46.926018</td>
      <td>46.936337</td>
      <td>46.946609</td>
      <td>46.956837</td>
      <td>...</td>
      <td>46.966171</td>
      <td>46.955986</td>
      <td>46.945755</td>
      <td>46.935478</td>
      <td>46.925156</td>
      <td>46.914787</td>
      <td>46.904369</td>
      <td>46.893909</td>
      <td>46.883404</td>
      <td>46.872849</td>
    </tr>
    <tr>
      <th>3</th>
      <td>46.809483</td>
      <td>46.820065</td>
      <td>46.830605</td>
      <td>46.841095</td>
      <td>46.851540</td>
      <td>46.861938</td>
      <td>46.872288</td>
      <td>46.882595</td>
      <td>46.892857</td>
      <td>46.903072</td>
      <td>...</td>
      <td>46.912392</td>
      <td>46.902222</td>
      <td>46.892002</td>
      <td>46.881741</td>
      <td>46.871429</td>
      <td>46.861073</td>
      <td>46.850670</td>
      <td>46.840221</td>
      <td>46.829727</td>
      <td>46.819187</td>
    </tr>
    <tr>
      <th>4</th>
      <td>46.755836</td>
      <td>46.766407</td>
      <td>46.776932</td>
      <td>46.787411</td>
      <td>46.797840</td>
      <td>46.808228</td>
      <td>46.818569</td>
      <td>46.828861</td>
      <td>46.839111</td>
      <td>46.849312</td>
      <td>...</td>
      <td>46.858624</td>
      <td>46.848465</td>
      <td>46.838257</td>
      <td>46.828007</td>
      <td>46.817707</td>
      <td>46.807365</td>
      <td>46.796974</td>
      <td>46.786537</td>
      <td>46.776058</td>
      <td>46.765530</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>468</th>
      <td>21.835442</td>
      <td>21.843287</td>
      <td>21.851095</td>
      <td>21.858870</td>
      <td>21.866610</td>
      <td>21.874313</td>
      <td>21.881983</td>
      <td>21.889616</td>
      <td>21.897215</td>
      <td>21.904778</td>
      <td>...</td>
      <td>21.911680</td>
      <td>21.904148</td>
      <td>21.896582</td>
      <td>21.888981</td>
      <td>21.881344</td>
      <td>21.873672</td>
      <td>21.865965</td>
      <td>21.858223</td>
      <td>21.850447</td>
      <td>21.842634</td>
    </tr>
    <tr>
      <th>469</th>
      <td>21.780140</td>
      <td>21.787983</td>
      <td>21.795792</td>
      <td>21.803566</td>
      <td>21.811304</td>
      <td>21.819006</td>
      <td>21.826674</td>
      <td>21.834307</td>
      <td>21.841904</td>
      <td>21.849466</td>
      <td>...</td>
      <td>21.856367</td>
      <td>21.848837</td>
      <td>21.841272</td>
      <td>21.833672</td>
      <td>21.826036</td>
      <td>21.818365</td>
      <td>21.810659</td>
      <td>21.802919</td>
      <td>21.795143</td>
      <td>21.787331</td>
    </tr>
    <tr>
      <th>470</th>
      <td>21.724823</td>
      <td>21.732666</td>
      <td>21.740473</td>
      <td>21.748245</td>
      <td>21.755983</td>
      <td>21.763685</td>
      <td>21.771351</td>
      <td>21.778982</td>
      <td>21.786579</td>
      <td>21.794140</td>
      <td>...</td>
      <td>21.801039</td>
      <td>21.793510</td>
      <td>21.785946</td>
      <td>21.778347</td>
      <td>21.770714</td>
      <td>21.763044</td>
      <td>21.755339</td>
      <td>21.747599</td>
      <td>21.739824</td>
      <td>21.732014</td>
    </tr>
    <tr>
      <th>471</th>
      <td>21.669493</td>
      <td>21.677334</td>
      <td>21.685141</td>
      <td>21.692911</td>
      <td>21.700647</td>
      <td>21.708347</td>
      <td>21.716013</td>
      <td>21.723644</td>
      <td>21.731239</td>
      <td>21.738798</td>
      <td>...</td>
      <td>21.745697</td>
      <td>21.738171</td>
      <td>21.730608</td>
      <td>21.723009</td>
      <td>21.715376</td>
      <td>21.707708</td>
      <td>21.700005</td>
      <td>21.692265</td>
      <td>21.684490</td>
      <td>21.676682</td>
    </tr>
    <tr>
      <th>472</th>
      <td>21.614147</td>
      <td>21.621986</td>
      <td>21.629793</td>
      <td>21.637562</td>
      <td>21.645298</td>
      <td>21.652996</td>
      <td>21.660662</td>
      <td>21.668291</td>
      <td>21.675884</td>
      <td>21.683443</td>
      <td>...</td>
      <td>21.690342</td>
      <td>21.682816</td>
      <td>21.675253</td>
      <td>21.667656</td>
      <td>21.660025</td>
      <td>21.652357</td>
      <td>21.644653</td>
      <td>21.636917</td>
      <td>21.629143</td>
      <td>21.621336</td>
    </tr>
  </tbody>
</table>
<p>473 rows × 463 columns</p>
</div>




```python

lon1d = np.reshape(lon2d, (1, np.product(lon2d.shape)))[0]
lat1d = np.reshape(lat2d, (1, np.product(lat2d.shape)))[0]
aod1d = np.reshape(AOD, (1, np.product(AOD.shape)))[0]

print(lon1d.shape, lat1d.shape, aod1d.shape)
```

    (218999,) (218999,) (218999,)
    


```python
data = pd.DataFrame(np.column_stack([lat1d, lon1d, aod1d]), columns = ['lat','lon','aod'])
data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>lat</th>
      <th>lon</th>
      <th>aod</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>46.970455</td>
      <td>111.370544</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>46.981075</td>
      <td>111.450150</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>46.991650</td>
      <td>111.529762</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>47.002178</td>
      <td>111.609383</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>47.012661</td>
      <td>111.689011</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
data.isnull().sum()
```




    lat         0
    lon         0
    aod    200896
    dtype: int64




```python
print(min(data.lat), max(data.lat))
print(min(data.lon), max(data.lon))
print(min(data.aod), max(data.aod))
```

    21.614147186279297 48.20196533203125
    111.37054443359375 148.55789184570312
    nan nan
    


```python
aod_data = data['aod']
aod_data.head()
```




    0   NaN
    1   NaN
    2   NaN
    3   NaN
    4   NaN
    Name: aod, dtype: float32




```python
dataset = data.fillna(0)
dataset
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>lat</th>
      <th>lon</th>
      <th>aod</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>46.970455</td>
      <td>111.370544</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>46.981075</td>
      <td>111.450150</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>46.991650</td>
      <td>111.529762</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>47.002178</td>
      <td>111.609383</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>47.012661</td>
      <td>111.689011</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>218994</th>
      <td>21.652357</td>
      <td>143.271103</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>218995</th>
      <td>21.644653</td>
      <td>143.330032</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>218996</th>
      <td>21.636917</td>
      <td>143.388962</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>218997</th>
      <td>21.629143</td>
      <td>143.447906</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>218998</th>
      <td>21.621336</td>
      <td>143.506836</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
<p>218999 rows × 3 columns</p>
</div>




```python
aod_dataset = dataset['aod']
aod_dataset
```




    0         0.0
    1         0.0
    2         0.0
    3         0.0
    4         0.0
             ... 
    218994    0.0
    218995    0.0
    218996    0.0
    218997    0.0
    218998    0.0
    Name: aod, Length: 218999, dtype: float32




```python
aod_dataset != 0
```




    0         False
    1         False
    2         False
    3         False
    4         False
              ...  
    218994    False
    218995    False
    218996    False
    218997    False
    218998    False
    Name: aod, Length: 218999, dtype: bool




```python
aod_pre = aod_dataset[aod_dataset != 0]
aod_pre.head()
```




    39497    0.197949
    39961    0.173366
    43155    0.603535
    43620    0.256907
    43621    0.268059
    Name: aod, dtype: float32




```python
aod_mean = aod_pre.mean()
aod_std = aod_pre.std()
print(aod_mean, aod_std)
```

    0.28004268 0.30609804
    


```python
dataset['AOD'] = (dataset['aod'] - aod_mean) / aod_std
dataset.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>lat</th>
      <th>lon</th>
      <th>aod</th>
      <th>AOD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>46.970455</td>
      <td>111.370544</td>
      <td>0.0</td>
      <td>-0.914879</td>
    </tr>
    <tr>
      <th>1</th>
      <td>46.981075</td>
      <td>111.450150</td>
      <td>0.0</td>
      <td>-0.914879</td>
    </tr>
    <tr>
      <th>2</th>
      <td>46.991650</td>
      <td>111.529762</td>
      <td>0.0</td>
      <td>-0.914879</td>
    </tr>
    <tr>
      <th>3</th>
      <td>47.002178</td>
      <td>111.609383</td>
      <td>0.0</td>
      <td>-0.914879</td>
    </tr>
    <tr>
      <th>4</th>
      <td>47.012661</td>
      <td>111.689011</td>
      <td>0.0</td>
      <td>-0.914879</td>
    </tr>
  </tbody>
</table>
</div>




```python
dataset = dataset.replace(dataset['AOD'][1], np.NaN)
dataset
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>lat</th>
      <th>lon</th>
      <th>aod</th>
      <th>AOD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>46.970455</td>
      <td>111.370544</td>
      <td>0.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>46.981075</td>
      <td>111.450150</td>
      <td>0.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>46.991650</td>
      <td>111.529762</td>
      <td>0.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>47.002178</td>
      <td>111.609383</td>
      <td>0.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>47.012661</td>
      <td>111.689011</td>
      <td>0.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>218994</th>
      <td>21.652357</td>
      <td>143.271103</td>
      <td>0.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>218995</th>
      <td>21.644653</td>
      <td>143.330032</td>
      <td>0.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>218996</th>
      <td>21.636917</td>
      <td>143.388962</td>
      <td>0.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>218997</th>
      <td>21.629143</td>
      <td>143.447906</td>
      <td>0.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>218998</th>
      <td>21.621336</td>
      <td>143.506836</td>
      <td>0.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>218999 rows × 4 columns</p>
</div>




```python
plt.figure(figsize = (12, 6))
#plt.style.use('seaborn-darkgrid')
plt.rc("font", size = 22)
plt.rcParams['font.family'] = 'Times New Roman'
m = Basemap(projection='cyl', lon_0 = 111.37, lat_0 = 21.614,
           llcrnrlon = 115, llcrnrlat = 26,
           urcrnrlon = 133, urcrnrlat = 45,
           resolution = 'c')

X, Y = m(dataset.lon.values, dataset.lat.values)
VAL = dataset.AOD.values
cmap_color = 'YlOrRd'
m.scatter(X, Y, c = VAL, s = 1.0, marker = "s", zorder = 1, vmin = 0, vmax = 1, cmap = plt.cm.get_cmap(cmap_color), alpha = 1.0)
# pass_color : YlOrBr, YlOrRd
'''
cmap_color_list = ['Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds',
            'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu',
            'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn','rainbow','RdYlGn']
'''            
m.colorbar(location='bottom', label = 'Aerosol Optical Depth', pad = 0.5)
m.drawcoastlines(color = 'black')
m.drawcountries(color = 'black')
m.drawmapboundary(fill_color = 'white')
m.drawparallels(np.arange(-150,120,5), labels=[1,0,0,0], dashes = [2,2], color = 'black')
m.drawmeridians(np.arange(-180,180,5), labels=[0,0,0,1], dashes = [2,2], color = 'black')

plt.title(Dataset[list_index-1].split('_')[-1] + "\n",color = 'black')
plt.show()
```


![output_21_0](https://user-images.githubusercontent.com/49590432/83952351-4a54d380-a873-11ea-8189-9a1fbf5c7987.png)


## 폰트 찾기


```python
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
```


```python
font_list = fm.findSystemFonts(fontpaths=None, fontext='ttf')

# ttf 폰트 전체갯수
print(len(font_list)) 
```

    383
    


```python
f = [f.name for f in fm.fontManager.ttflist]
print(len(font_list))
# 10개의 폰트명 만 출력
f[:10]
```

    383
    




    ['STIXNonUnicode',
     'STIXNonUnicode',
     'STIXSizeThreeSym',
     'DejaVu Sans Mono',
     'cmex10',
     'DejaVu Sans Mono',
     'DejaVu Serif',
     'STIXGeneral',
     'DejaVu Sans',
     'cmsy10']




```python
[(f.name, f.fname) for f in fm.fontManager.ttflist if 'New' in f.name]
```




    [('Times New Roman', 'C:\\Windows\\Fonts\\timesbi.ttf'),
     ('NewJumja', 'C:\\Windows\\Fonts\\JUMJA.TTF'),
     ('Courier New', 'C:\\Windows\\Fonts\\courbi.ttf'),
     ('Times New Roman', 'C:\\Windows\\Fonts\\timesi.ttf'),
     ('Times New Roman', 'C:\\Windows\\Fonts\\times.ttf'),
     ('Courier New', 'C:\\Windows\\Fonts\\courbd.ttf'),
     ('Microsoft New Tai Lue', 'C:\\Windows\\Fonts\\ntailub.ttf'),
     ('Courier New', 'C:\\Windows\\Fonts\\cour.ttf'),
     ('New Gulim', 'C:\\Windows\\Fonts\\NGULIM.TTF'),
     ('Microsoft New Tai Lue', 'C:\\Windows\\Fonts\\ntailu.ttf'),
     ('Times New Roman', 'C:\\Windows\\Fonts\\timesbd.ttf'),
     ('Courier New', 'C:\\Windows\\Fonts\\couri.ttf')]




```python

```
