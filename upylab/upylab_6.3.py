def substitue(message, abreviation):
    for a in abreviation:
        message = message.replace(a, abreviation[a])
    return message


print(substitue('C. N. cpt 2 to inf', {'C.' : 'Chuck',
                                 'N.' : 'Norris',
                                 'cpt' : 'counted',
                                 '2' : 'two times',
                                 'inf' : 'infinity'}))