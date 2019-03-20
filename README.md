# Programming vacancies compare

It's App analyze mention word(you choose this word) in Vkontakte. After collect statistics would be created Bar plot,
using plotly.ly service.

### How to install

1. You need to register in [plotly Api](https://plot.ly/Auth/login/?action=signup&next=%2Fsettings%2Fapi#/).
2. Create .env file and add:
    * login=plotly username
    * api_key=plotly api-key [Api-key here](https://plot.ly/settings/api#/)

3. Install dependencies (written below)

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### Program output example
```
python main.py
>>Статистика собрана!
>>High five! You successfully sent some data to your account on plotly. View your plot in your browser at https://plot.ly/~xdass/0 or inside your plot.ly account where it is named 'basic-line'

```
## Bar plot example
<img src="https://i.ibb.co/tZrQskR/Plotly.png" alt="Plotly" border="0">

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).