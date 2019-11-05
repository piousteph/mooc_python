def store_email(liste_mails):
    res = {}
    for addr in liste_mails:
        n = addr.split('@')
        if n[1] not in res:
            res[n[1]] = []
        res[n[1]].append(n[0])
        res[n[1]].sort()
    return res



print(store_email(["ludo@prof.ur", "andre.colon@stud.ulb",
             "thierry@profs.ulb", "sébastien@prof.ur",
             "eric.ramzi@stud.ur", "bernard@profs.ulb",
             "jean@profs.ulb" ]))

# {
#  'prof.ur' : ['ludo', 'sébastien']
#  'stud.ulb' : ['andre.colon']
#  'profs.ulb' : ['bernard', 'jean', 'thierry']
#  'stud.ur' : ['eric.ramzi']
# }

# {'prof.ur': ['ludo', 'sébastien'], 'stud.ulb': ['andre.colon'], 'profs.ulb': ['thierry', 'bernard', 'jean'], 'stud.ur': ['eric.ramzi']}
# {'prof.ur': ['ludo', 'sébastien'], 'stud.ulb': ['andre.colon'], 'profs.ulb': ['bernard', 'jean', 'thierry']; 'stud.ur': ['eric.ramzi']}