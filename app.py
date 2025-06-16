from flask import Flask,request,render_template
from bs4 import BeautifulSoup

app=Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    scraped_data=[]


    if request.method =='POST':
        url=request.method['url']
        header={'User-Agent':'Mozilla/5.0'}
        response =response.get(url, header==header)
        soup=BeautifulSoup(response.text, 'html.parser')


        for link in soup.find_all('a'):
            href=link.get('href')
            text=link.text.strip()
            if href:
                scraped_data.append({'text':text ,'href':href})

    return render_template('index.html', data=scraped_data)

if __name__ == '__main__':
    app.run(debug=True)