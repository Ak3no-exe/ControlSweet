# Installe le widget Sweet_Control dans ton projet Capacitor.
# Usage : copie ce dossier dans ton projet puis, à la racine du projet :  python install.py
import os, shutil, re, subprocess, sys

here = os.path.dirname(os.path.abspath(__file__))
root = os.getcwd()
main = os.path.join(root, "android", "app", "src", "main")
if not os.path.isdir(main):
    sys.exit("Erreur : lance ce script à la racine de ton projet Capacitor (le dossier qui contient 'android').")

# 1. Copie des fichiers du widget
for sub in ("res/xml", "res/layout", "java/com/sweetcontrol/app"):
    src = os.path.join(here, "android", "app", "src", "main", *sub.split("/"))
    dst = os.path.join(main, *sub.split("/"))
    os.makedirs(dst, exist_ok=True)
    for f in os.listdir(src):
        shutil.copy2(os.path.join(src, f), os.path.join(dst, f))
        print("copié :", f)

# 2. Nouveau index.html (historique, graphique, synchro)
www = os.path.join(root, "www")
if os.path.isdir(www):
    shutil.copy2(os.path.join(here, "www", "index.html"), os.path.join(www, "index.html"))
    print("copié : www/index.html")
else:
    print("Dossier www introuvable : copie www/index.html à la main.")

# 3. Déclaration du widget dans AndroidManifest.xml
mf = os.path.join(main, "AndroidManifest.xml")
s = open(mf, encoding="utf-8").read()
if ".ScWidget" in s:
    print("Manifest déjà modifié.")
else:
    block = '''
        <receiver android:name=".ScWidget" android:exported="true">
            <intent-filter>
                <action android:name="android.appwidget.action.APPWIDGET_UPDATE" />
            </intent-filter>
            <meta-data android:name="android.appwidget.provider"
                       android:resource="@xml/sc_widget_info" />
        </receiver>
'''
    s = s.replace("</application>", block + "    </application>", 1)
    open(mf, "w", encoding="utf-8").write(s)
    print("Manifest modifié.")

# 4. Plugin Preferences + sync Capacitor
shell = os.name == "nt"
for cmd in (["npm", "i", "@capacitor/preferences"], ["npx", "cap", "sync", "android"]):
    print(">", " ".join(cmd))
    subprocess.run(cmd, cwd=root, shell=shell)

print("\nTerminé. Ouvre Android Studio (npx cap open android) puis Build > Build APK(s).")
