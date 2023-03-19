import subprocess
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField
from wtforms.validators import InputRequired, NumberRange
import shlex

app = Flask(__name__)


class InputForm(FlaskForm):
    code = StringField(validators=[InputRequired()])
    time = IntegerField(validators=[NumberRange(min=1, max=30)])


@app.route('/run_code', methods=['POST'])
def remote_code_usage():
    in_put = InputForm()

    if in_put.validate_on_submit():
        code = in_put.code.data
        time = in_put.time.data
        command = shlex.split(f'prlimit --nproc=1:1 python3 -c "{code}"')
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        flag_kill = False
        try:
            output, errors = process.communicate(timeout=time)
        except subprocess.TimeoutExpired:
            process.kill()
            output, errors = process.communicate()
            flag_kill = True
        return f'Output: {output.decode()}, errors: {errors.decode()}, process was killed by timeout: {flag_kill}'
    return f'Invalid input: {in_put.errors}', 400


if __name__ == '__main__':
    app.config['WTF_CSRF_ENABLED'] = False
    app.run(debug=True)
