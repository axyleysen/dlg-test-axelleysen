# dlg-test-axelleysen
DLG  Software Engineer Python Test


### To run:
Set up virtual environment and install requirements:
```bash
python3 -m virtualenv v-env
source v-env/bin/activate
pip3 install -r requirements.txt
```

Run application server:
```bash
python3 sum_list.py
```

Then in another terminal window, or browser, you can api calls. For example:
```bash
curl http://localhost:5000/total/0,1,2,3,4
curl http://localhost:5000/total/2,4
```

Or run the test script:
```bash
$ python3 tests.py
```

### Assumptions
- Input list is a comma separated string
- Input list contains integer numbers and no fractional numbers 
- Input list may contain positive and negative integers 