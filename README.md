### install.
git clone https://github.com/knote2019/pytorch-operator-extension
cd pytorch-operator-extension
pip install .

或者:
pip install git+https://github.com/knote2019/pytorch-operator-extension

### test.
python test.py

make sure import after torch, or it will raise error: "ImportError: libc10.so: cannot open shared object file: No such file or directory"
```python
import torch
import add_matrix_cuda
```

### reference.
https://github.com/kwea123/pytorch_cppcuda_practice
