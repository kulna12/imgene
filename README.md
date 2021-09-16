## Generate Pixels with imgene
<p align="center">
<img width="400px" height="400px" src="input/ss.jpg"  />
</p>

*Get the Code by Clonging repo*
```
git clone https://github.com/xadhrit/imgene.git

cd imgene
```

*Install requirements by running*

```bash
python3 -m pip install -r requirements.txt

```
**Generate**

*First Put you images in input folder and run change_pixel.py script for changing images size and formats(which is necessary).*


``` bash 
python3 change_pixel.py
```
As a result you 'll have a resized folder . So  remove input folder and rename resized folder to input.


``` bash
rm -rf input/

mv resized/  input/
```
Now start Jupyter-Notebook by commanding

``` bash
jupyter-notebook
```
and generator images.
