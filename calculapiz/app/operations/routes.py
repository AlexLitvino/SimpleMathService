"""Routes that implements service operations"""
import time

from flask import jsonify, request

from app.config import STATISTICS_PATH
from app.operations import bp
from app.statistics_utils import log_statistics
from .operations import Operations


@bp.route('/add')
def add():
    args = request.args
    now = time.time()
    accuracy = 3
    try:
        op1 = float(args['op1'])
        op2 = float(args['op2'])
        result = op1 + op2
        result = round(result, accuracy)
        response = {'op1': op1, 'op2': op2, 'operation': Operations.ADD.value, 'result': result}
        stat_data = [now, 'SUCCESS', Operations.ADD.value, op1, op2, result]
        status_code = 200
    except Exception as e:
        response = {'error': 'Everything goes wrong:('}
        stat_data = [now, 'CRITICAL', e]
        status_code = 400
    finally:
        log_statistics(STATISTICS_PATH, stat_data)
        return jsonify(response), status_code


@bp.route('/sub')
def sub():
    args = request.args
    now = time.time()
    accuracy = 3
    try:
        op1 = float(args['op1'])
        op2 = float(args['op2'])
        result = op1 - op2
        result = round(result, accuracy)
        response = {'op1': op1, 'op2': op2, 'operation': Operations.SUB.value, 'result': result}
        stat_data = [now, 'SUCCESS', Operations.SUB.value, op1, op2, result]
    except Exception as e:
        response = {'error': 'Everything goes wrong:(', 'error_details': f'{e}'}
        stat_data = [now, 'CRITICAL', e]
    finally:
        log_statistics(STATISTICS_PATH, stat_data)
        return jsonify(response)


@bp.route('/mlp')
def mlp():
    args = request.args
    now = time.time()
    accuracy = 3
    try:
        op1 = float(args['op1'])
        op2 = float(args['op2'])
        result = op1 * op2
        result = round(result, accuracy)
        response = {'op1': op1, 'op2': op2, 'operation': Operations.MLP.value, 'result': result}
        stat_data = [now, 'SUCCESS', Operations.MLP.value, op1, op2, result]
    except Exception as e:
        response = {'error': 'Everything goes wrong:('}
        stat_data = [now, 'CRITICAL', e]
    finally:
        log_statistics(STATISTICS_PATH, stat_data)
        return jsonify(response)


@bp.route('/div')
def div():
    args = request.args
    now = time.time()
    accuracy = 3
    try:
        op1 = float(args['op1'])
        op2 = float(args['op2'])
        result = op1 / op2
        result = round(result, accuracy)
        response = {'a': op1, 'op2': op2, 'operation': Operations.DIV.value, 'result': result}
        stat_data = [now, 'SUCCESS', Operations.DIV.value, op1, op2, result]
    except Exception as e:
        response = {'error': 'Everything goes wrong:('}
        stat_data = [now, 'CRITICAL', e]
    finally:
        log_statistics(STATISTICS_PATH, stat_data)
        return jsonify(response)
