# Vérificateur de dossier Canada - Par Hugo
dossier = {
  "IELTS": False,
  "TCF": False,
  "WES": False,
  "GitHub": True
}

print("--- Vérification Canada ---")
manque = 0

for doc, ok in dossier.items():
  if ok == False:
    print(f"❌ Il manque: {doc}")
    manque = manque + 1
  else:
    print(f"✅ OK: {doc}")

if manque == 0:
  print("🎉 Dossier complet ! Prêt pour Canada")
else:
  print(f"Il te reste {manque} documents à faire")
