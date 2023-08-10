from flask import Flask,render_template,request
app=Flask(__name__,template_folder='template')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate',methods=["POST","GET"])
def calculate():
    weigth1=request.form.get('weigth')
    heigth1=request.form['heigth']
    
    weigth1=float(weigth1)
    heigth1=float(heigth1)
    heigth1=heigth1/100

    BMI=weigth1/(heigth1*heigth1)

    BMI=round(BMI,2)
    
    if BMI>0 and BMI<31:
        if BMI<=16:
            return render_template('cal.html',pres=f'You are sever underweigth BMI:{BMI} 😖')
        elif BMI<=18.5:
            return render_template('cal.html',pres=f'You are underweigth BMI:{BMI} 😕')
        elif BMI<=25:
            return render_template('cal.html',pres=f'You are normal BMI:{BMI} 🙂')
        elif BMI<=30:
            return render_template('cal.html',pres=f'You are overweigth BMI:{BMI} 🙄')
        else:
            return render_template('cal.html',pres=f'You are very overweigth BMI:{BMI} 😱')
    else:
        return render_template('cal.html',pres='Enter correct 😒')
    

if __name__=='__main__':
    app.run(debug=True)