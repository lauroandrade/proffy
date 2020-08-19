from flask import Flask, render_template, request, redirect, url_for


def give_classes_function():
    req = request.args

    if any(request.query_string):
        # verificar informações específicas para proteção
        proffy_info = {
            'name': req.get('name'),
            'avatar': req.get('avatar'),
            'whatsapp': req.get('whatsapp'),
            'bio': req.get('bio'),
            'subject': convert_subject(req.get('subject', type=int)),
            'cost': req.get('cost'),
            'weekday': req.getlist('weekday[]'),
            'time_from': req.getlist('time_from[]'),
            'time_to': req.getlist('time_to[]')
        }       
        proffys_data.append(proffy_info)
        return redirect(url_for('study'))