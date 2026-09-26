# verificateur_canada_v3.py - Par Hugo - Jour 5

def verifier_dossier(nom_personne, dossier):
    print(f"--- Vérification pour {nom_personne} ---")
    manque = 0
    for doc, ok in dossier.items():
        if not ok:
            print(f"❌ Il manque: {doc}")
            manque += 1
        else:
            print(f"✅ OK: {doc}")
    
    if manque == 0:
        return f"🎉 {nom_personne}, dossier complet ! Prêt pour le Canada !"
    else:
        return f"Il te reste {manque} documents, {nom_personne}"

# --- On teste pour 2 personnes ---

dossier_hugo = {
    "IELTS": False,
    "TCF": False,
    "WES": False,
    "GitHub": True
}

dossier_ami = {
    "IELTS": True,
    "TCF": True,
    "WES": True,
    "GitHub": True
}

print(verifier_dossier("Hugo", dossier_hugo))
print("")
print(verifier_dossier("Mon ami du Ghana", dossier_ami))
