# Instructions to install C extension to your virtual environment

1. Navigate to the directory where the setup.py file is located using the command line. In this case, it is assumed to be in the "lab6" directory.
```bash
cd lab6
```
2. Run the following command to build a wheel file:
```bash
python setup.py bdist_wheel
```
3. Once the wheel file has been created, navigate to the dist folder within the "lab6" directory.
```bash
cd dist
```
4. Use pip to install the wheel file, replacing name-of-wheel-file with the actual name of the generated wheel file:
```bash
pip install name-of-wheel-file.whl --force-reinstall
```
That's it! Your C extension should now be installed and ready to use in your virtual environment.