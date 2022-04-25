from flask import Flask, request, render_template
import tensorflow as tf
app=Flask(__name__)
def get_prediction(params):
    model=tf.keras.models.load_model('DNN_model')
    y_pred=model.predict(params)
    return f'Рекомендуемое cоотношение матрица-наполнитель для введенных параметров: {y_pred}'
@app.route('/', methods=['post', 'get'])
def processing():
    message = ''
    if request.method == 'POST':
        plot = request.form.get('plot')
        mup = request.form.get('mup')
        ko = request.form.get('ko')
        seg = request.form.get('seg')
        tv = request.form.get('tv')
        pp = request.form.get('pp')
        mupr = request.form.get('mupr')
        pr = request.form.get('pr')
        ps = request.form.get('ps')
        un = request.form.get('un')
        shn = request.form.get('shn')
        pln = request.form.get('pln')
        params = [plot, mup, ko, seg, tv, pp, mupr, pr, ps, un, shn, pln]
        params = [float(i) for i in params]
        message = get_prediction(params)
    return render_template('matrix.html', message=message)
if __name__ == "__main__":
    app.run()