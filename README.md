# Boundary Detection and Morphological Operators

### Contributors:

* [Alexis Baudron] (abe3897)

---

### Installing all dependencies 

Ubuntu 16.04 Linux machine with python3.5 or +

$ python3 -m venv venv 
$ unset PYTHONPATH
$ source venv/bin/activate
$ pip install -r requirements.txt 

### Run the code

Activate virtual environment ($ source venv/bin/activate)
$ python morph.py

### Algorithm 

Python implementation of the basic morphological operators covered in class as well as Boundary detection. There are 5 functions covered in the morph.py file:

1. Erosion
2. Dilation
3. Closing: 
	This algorithm consists of first performing dilation and then erosion with the same kernel
4. Opening
	This algorithm consists of first performing erosion and then dilation with the same kernel
5. Boundary
	

Analysis of the performance along with pictures of the performance are provided below

### Results Analysis

