# NAO Challenge 2023

---

###### _Master of Artificial Intelligence - Fundamentals of Artificial Intelligence and Knowledge Representation_

Team: <br/>
Jana Nikolovska [unibo email](jana.nikolovska@studio.unibo.it) 
| [github profile](https://github.com/jananikolovska)<br/>
Carlo Merola [unibo email](carlo.merola@studio.unibo.it) 
| [github profile](https://github.com/carlomerola)<br/>

![img](meta_data/NaoTequila.png)

## ▶️ Run the program
1. Install python2.7
2. Install [Choregraphe](https://www.aldebaran.com/en/support/nao-6/downloads-softwares) and [PythonSDK (Naoqi)](http://doc.aldebaran.com/2-5/dev/python/install_guide.html)
3. Create and activate a virtual environment
```
python2.7 -m pip install virtualenv
python2.7 -m virtualenv guskaNao
guskaNao\Scripts\activate
```
4. Clone the repository and run the following code in the project directory:
```
pip install -r requirements.txt
```
5. Open Choreoraphe and connect to a virtual robot. Get the IP and PORT values
![img1](meta_data/ConnectVirtualRobot.png)
![img2](meta_data/FindIPPORT.png)
6. Run the program in command line using the IP and PORT as arguments (see example below 👇)<br/>
_Default values for IP and PORT are specified in the config.ini file_
```
python main.py ip port
```
##### 📌 Example
```
python main.py "127.0.0.1" 53860
```

## 📝 Repository Structure
* __main.py__ - run main program
* __nao.py__ - define classes and search problem
* __utils.py__ - helper functions
* __find_conflicts.py__ - attempt to find move preconditions/postconditions automatically
* __meta_data__ 
* __create_metafile.py__ - create a metadata file with details about moves (duration, mandatory, pre- and post-conditionsp)
* __dance_moves__
* __aima__ - Code for Artificial Intelligence: A Modern Approach (AIMA) 4th edition by Peter Norvig and Stuart Russel.
* __tequila.mp3__ - music choice
* __requirements.txt__
* __config.ini__

